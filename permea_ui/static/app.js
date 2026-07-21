/* Drylab client.

   RENDER-ONLY. This file does no arithmetic on evaluation output -- no rounding, no
   deriving a percentage from a ratio, no recomputing a delta from two metrics. Numbers are
   stringified exactly as the engine emitted them. The narration guardrail requires every
   number in prose to trace back to a report field; a client that quietly reformatted those
   fields would break that trace without anything raising. `fmt` below is the whole of the
   number handling on purpose. */

const $ = (sel) => document.querySelector(sel);
const el = (tag, cls, text) => {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (text !== undefined && text !== null) n.textContent = String(text);
  return n;
};

/* Engine values pass through untouched; only null/undefined get a placeholder. */
const fmt = (v) => (v === null || v === undefined ? "—" : String(v));

let DEFAULTS = null;
let busy = false;

/* ------------------------------------------------------------------ bootstrap */
async function boot() {
  const [status, catalog] = await Promise.all([
    fetch("/api/status").then((r) => r.json()),
    fetch("/api/warnings").then((r) => r.json()),
  ]);
  DEFAULTS = status.defaults;
  $("#s-seeds").value = DEFAULTS.seeds;
  $("#s-k").value = DEFAULTS.k;
  $("#s-nboot").value = DEFAULTS.n_boot;
  $("#example-label").textContent = status.example_label;
  if (!status.narration_available) {
    setStatus("Idle — no narration provider configured, so runs will show findings only.");
  }
  renderCatalog(catalog.codes);
}

function renderCatalog(codes) {
  const host = $("#catalog");
  host.replaceChildren();
  for (const [status, heading] of [
    ["active", "Active — these can fire from an evaluation run"],
    ["reserved", "Reserved — catalogued, no firing logic yet"],
  ]) {
    const group = el("div", "cat-group");
    group.append(el("h3", null, heading));
    const list = el("div", "cat-list");
    for (const c of codes.filter((c) => c.status === status)) {
      const item = el("div", `cat-item ${status}`);
      item.append(el("code", null, c.code));
      item.append(el("span", "t", c.title));
      item.title = c.fire_condition;
      list.append(item);
    }
    group.append(list);
    host.append(group);
  }
}

/* ------------------------------------------------------------------ input UI */
document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((t) => t.classList.remove("active"));
    document.querySelectorAll(".tabpane").forEach((p) => p.classList.remove("active"));
    tab.classList.add("active");
    $(`#pane-${tab.dataset.tab}`).classList.add("active");
  });
});

const settings = () => ({
  seeds: $("#s-seeds").value,
  k: $("#s-k").value,
  n_boot: $("#s-nboot").value,
  declare_identity: $("#s-identity").checked,
});

function setBusy(on) {
  busy = on;
  document.querySelectorAll(".run-example, #run-upload").forEach((b) => (b.disabled = on));
}

document.querySelectorAll(".run-example").forEach((btn) => {
  btn.addEventListener("click", async () => {
    if (busy) return;
    const q = new URLSearchParams({ clustering: btn.dataset.clustering, ...settings() });
    await start(fetch(`/api/jobs/example?${q}`, { method: "POST" }));
  });
});

$("#run-upload").addEventListener("click", async () => {
  if (busy) return;
  const ds = $("#f-dataset").files[0];
  const cl = $("#f-clusters").files[0];
  if (!ds || !cl) {
    setStatus("Select both a dataset CSV and a cluster TSV.", "error");
    return;
  }
  const body = new FormData();
  body.append("dataset", ds);
  body.append("clusters", cl);
  const q = new URLSearchParams(settings());
  await start(fetch(`/api/jobs?${q}`, { method: "POST", body }));
});

function setStatus(text, cls) {
  const line = $("#status-line");
  line.textContent = text;
  line.className = cls || "idle";
}

async function start(request) {
  setBusy(true);
  $("#result").replaceChildren();
  setStatus("Submitting…", "busy");
  try {
    const res = await request;
    if (!res.ok) {
      /* Rejections here are contract violations in the uploaded files, surfaced by the
         server's pre-flight. Show the message itself — it names the missing column or the
         unassigned ids, which is the whole of what the user needs to fix it. */
      const body = await res.json().catch(() => null);
      throw new Error(body?.detail || `${res.status} ${res.statusText}`);
    }
    const { job_id } = await res.json();
    await poll(job_id);
  } catch (err) {
    setStatus(err.message, "error");
  } finally {
    setBusy(false);
  }
}

/* Poll rather than stream: a run is ~10s and the server holds one worker, so a 1s tick is
   both cheap and accurate enough to show the evaluating -> narrating transition. */
const STAGE_TEXT = {
  queued: "Queued…",
  starting: "Starting…",
  evaluating: "Evaluating (cross-validation + paired bootstrap)…",
  narrating: "Generating interpretation…",
};

async function poll(jobId) {
  for (;;) {
    const job = await fetch(`/api/jobs/${jobId}`).then((r) => r.json());
    if (job.status === "done") {
      setStatus("Complete", "idle");
      renderResult(job.result);
      return;
    }
    if (job.status === "failed") {
      setStatus("Run failed", "error");
      $("#result").append(el("pre", "trace", job.error));
      return;
    }
    setStatus(STAGE_TEXT[job.stage] || "Working…", "busy");
    await new Promise((r) => setTimeout(r, 1000));
  }
}

/* ------------------------------------------------------------------ rendering */
function renderResult(result) {
  const host = $("#result");
  host.replaceChildren();
  const { diagnosis, narration } = result;

  host.append(renderContext(diagnosis.context, result));
  host.append(renderSummary(diagnosis.summary));
  host.append(renderFindings(diagnosis.fired));
  host.append(renderVoice(narration));
}

function renderContext(ctx, result) {
  const grid = el("dl", "context-grid");
  const cells = [
    ["Dataset", result.dataset_name],
    ["Clusters", result.clusters_name],
    ["Sequences (n)", ctx.n],
    ["Positive / negative", `${fmt(ctx.pos)} / ${fmt(ctx.neg)}`],
    ["Clusters", ctx.n_clusters],
    ["Representation", ctx.representation],
    ["Headline condition", ctx.headline_condition],
    ["Resample unit", ctx.resample_unit],
    ["CI level", ctx.ci_level_pct === null ? "—" : `${ctx.ci_level_pct}%`],
    ["Identity definition", ctx.identity_definition ? JSON.stringify(ctx.identity_definition) : "not declared"],
    ["Data sha256", ctx.data_sha256],
  ];
  for (const [k, v] of cells) {
    const cell = el("div", "cell");
    cell.append(el("dt", null, k), el("dd", null, fmt(v)));
    grid.append(cell);
  }
  return grid;
}

function renderSummary(summary) {
  const row = el("div", "summary-row");
  if (summary.total === 0) {
    row.append(el("span", "pill clean", "No warnings fired"));
    return row;
  }
  for (const sev of ["critical", "warn", "info"]) {
    if (summary[sev] > 0) row.append(el("span", `pill ${sev}`, `${summary[sev]} ${sev}`));
  }
  return row;
}

/* Evidence keys are shown only when the engine set them. All eleven are always present in
   the payload and mostly null for any given code; printing the nulls would bury the two or
   three numbers that actually fired the warning. */
const EVIDENCE_LABELS = {
  model: "model",
  metric: "metric",
  delta_point: "delta (B − A)",
  ci_lo: "CI lower",
  ci_hi: "CI upper",
  ci_excludes_zero: "CI excludes zero",
  n_clusters: "clusters",
  resample_unit: "resample unit",
  headline_condition: "headline condition",
  identity_definition_declared: "identity declared",
  threshold_used: "policy threshold applied",
};

function renderFindings(fired) {
  const wrap = el("div");
  if (!fired.length) {
    wrap.append(
      el("div", "clean-note",
        "No warning fired. That means none of the active rules matched — not that the " +
        "evaluation is free of every problem the registry describes. See the reserved codes below.")
    );
    return wrap;
  }
  for (const f of fired) {
    const card = el("div", `finding ${f.severity}`);
    const head = el("div", "finding-head");
    head.append(el("code", "code", f.code), el("span", "title", f.title));
    card.append(head);
    card.append(el("p", "evidence-str", f.evidence_str));

    const rows = Object.entries(f.evidence).filter(([, v]) => v !== null && v !== undefined);
    if (rows.length) {
      const table = el("table", "evidence");
      for (const [k, v] of rows) {
        const tr = el("tr");
        tr.append(el("td", null, EVIDENCE_LABELS[k] || k), el("td", null, fmt(v)));
        table.append(tr);
      }
      card.append(table);
    }
    wrap.append(card);
  }
  return wrap;
}

const VOICE_HEADINGS = {
  ok: "Interpretation",
  withheld: "Interpretation withheld",
  unavailable: "Interpretation unavailable",
  error: "Interpretation failed",
};

function renderVoice(n) {
  const box = el("div", `voice ${n.status === "ok" ? "" : "blocked"}`);
  const head = el("div", "voice-head");
  head.append(el("span", null, VOICE_HEADINGS[n.status] || "Interpretation"));
  head.append(el("span", "badge", "not authoritative"));
  box.append(head);

  if (n.status === "ok") {
    box.append(el("p", "voice-text", n.text));
    const meta = el("p", "voice-meta");
    /* The sha256 is the receipt binding this prose to the exact report above. It is the
       one piece of narration metadata worth showing; the model identity is not exposed. */
    meta.textContent =
      `provider: ${fmt(n.provider)}  ·  source report sha256: ${fmt(n.source_report_sha256)}`;
    box.append(meta);
  } else {
    box.append(el("p", "voice-text", n.detail || "No interpretation was produced."));
    if (n.status === "withheld") {
      box.append(
        el("p", "voice-meta",
          "Generated prose failed a guardrail check and was discarded rather than shown. " +
          "The findings above are unaffected.")
      );
    }
  }
  return box;
}

boot();
