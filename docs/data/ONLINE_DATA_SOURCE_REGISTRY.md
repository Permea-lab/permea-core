# Online Data Source Registry

Status: Public planning document

Date: 2026-06-11

## Purpose

This registry tracks online public data sources that may feed Permea benchmark
registry entries after access, license, provenance, and benchmark fit are
reviewed. It is a planning document only. No dataset has been downloaded,
scraped, packaged, or redistributed as part of this registry.

Each source should remain in source-card-only mode until the source card,
license/access status, provenance fields, and benchmark mapping are reviewed.

## Registry

| source_id | source_name | delivery_axis | biological_scope | likely_data_type | acquisition_mode | license/access status | provenance strength | benchmark mapping | priority | current status | next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b3pdb | B3PDB | blood-brain barrier | blood-brain barrier penetrating peptides | peptide sequences, source-defined BBB labels, literature/source metadata | manual source-card review first; downloader only if permitted | to verify; no redistribution until confirmed | medium to high if original source identifiers, papers, and label context are preserved | `bbb_b3pred_dataset3`; BBB peptide benchmark candidates | P0 | candidate source | verify public access path, license terms, fields, and source citation set |
| brainpeps | BrainPeps | blood-brain barrier | BBB peptide transport evidence | peptide records, positive and negative BBB-related source labels, assay/literature context | manual source-card review first | to verify; source-card-only until access and license are confirmed | high if positive/negative label source, assay context, PMID/DOI, and source method are preserved | BBB peptide benchmark candidates and evidence cards | P0 | candidate source | verify database availability, export posture, license/access terms, and citation fields |
| b3pred_dataset3 | B3Pred Dataset 3 | blood-brain barrier | benchmark-ready BBB peptide classification surface | peptide sequences and source-defined benchmark labels | already represented as a benchmark registry scaffold; do not redownload in this task | source attribution and redistribution require review | medium; must preserve source construction notes and label policy | `bbb_b3pred_dataset3` | P0 | benchmark registry entry exists | convert registry scaffold into dataset card proposal after source/license review |
| cppsite2 | CPPsite 2.0 | cell penetration / membrane penetration | experimentally reported cell-penetrating peptides | peptide sequences, CPP labels, cargo/context notes, literature metadata | manual source-card review first; lightweight downloader only if permitted | to verify; no redistribution until confirmed | high if original CPP entry identifiers, citations, cargo, modification, and assay fields are preserved | `cpp_cppsite2_placeholder`; CPP prototype benchmark | P1 | candidate source | verify current URL, license/access terms, downloadable fields, and original CPPsite citation |
| cppsite_original | CPPsite original | cell penetration / membrane penetration | original CPPsite database release | peptide sequences, CPP annotations, literature metadata | citation/source-card-only unless current access and terms are confirmed | to verify; likely historical source pointer | medium; useful for version lineage and provenance | CPP prototype benchmark lineage | P2 | candidate source | determine whether original release has distinct data or only citation lineage value |
| deeploc | DeepLoc dataset / DeepLoc service documentation | localization proxy | eukaryotic protein subcellular localization | protein sequences, localization labels, sorting-signal labels in related releases | source-card-only first; use public dataset links only if access and license permit | to verify for dataset redistribution; article and service pages are public | medium to high if UniProt accession, evidence code, localization label, and split origin are preserved | localization / targeting proxy roadmap | P1 | candidate source | verify dataset files, license posture, and whether use should be proxy-only |
| uniprot_subcellular_location | UniProt subcellular location annotations | localization proxy | curated protein subcellular location and topology annotations | protein accessions, sequences, location annotations, evidence/provenance fields | permitted metadata retrieval must be reviewed against UniProt terms; no bulk acquisition in this task | to verify from current UniProt license and terms | high if accession, release, annotation evidence, location vocabulary, and citation fields are preserved | localization / targeting proxy roadmap; evidence-card support | P1 | candidate source | verify allowed retrieval mode, release/version handling, and attribution requirements |
| signalp | SignalP public documentation and related training sources | targeting / protein export proxy | signal peptide and cleavage-site prediction | protein sequences, signal peptide labels, cleavage-site annotations where available | source-card-only until dataset access/license is confirmed | to verify; service/documentation public, training data posture requires review | medium if source accession, label type, organism group, and publication are preserved | targeting proxy roadmap | P2 | candidate source | verify whether a redistributable benchmark source exists or whether this remains a method/source pointer |
| pubmed | PubMed / NCBI literature metadata | literature evidence graph | delivery-related publications and source citations | bibliographic metadata, abstracts where permitted, PMID/DOI links | manual query notes first; later metadata harvester only under NCBI usage rules | metadata access public; article text and abstracts require copyright review | high for citation-level provenance; content reuse varies by record | evidence cards for BBB, CPP, localization, and benchmark source claims | P0 | candidate evidence source | define citation metadata fields and copyright-safe extraction policy |
| europe_pmc | Europe PMC | literature evidence graph | life-science literature and open-access full-text records | bibliographic metadata, open-access full-text links, annotations where permitted | manual source-card review first; API/metadata harvester only if compliant | to verify by record/license; OA full text varies by article | high if PMCID, PMID, DOI, license, source section, and access date are preserved | evidence-card support and source discovery | P1 | candidate evidence source | verify licensing fields, rate guidance, and whether Open Access subset records are needed |
| openalex | OpenAlex | literature metadata graph | scholarly metadata for delivery-related sources | work metadata, DOI, venue, authorship, citation links | metadata harvester candidate after terms review | metadata license appears permissive but must be confirmed at implementation time | medium for bibliographic graph; not a substitute for article-level evidence | evidence-card discovery and citation enrichment | P2 | candidate metadata source | verify current API/service terms, required attribution, and record-level metadata fields |

## Readiness Rules

- A source listed here is not automatically a benchmark dataset.
- A source remains source-card-only until access and license are confirmed.
- If redistribution rights are unclear, mark the source `no-redistribution`.
- If labels come from literature extraction, preserve PMID, DOI, source section,
  extraction note, and review status.
- If labels are positive-only, flag negative sampling risk before any benchmark
  task proposal.
- If a source is a localization, protein export, or targeting proxy rather than direct
  delivery evidence, mark it as a proxy/localization axis in any benchmark task.
