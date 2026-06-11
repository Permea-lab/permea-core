# UniProt Subcellular Location Source Card

| Field | Value |
| --- | --- |
| source_id | uniprot_subcellular_location |
| source_name | UniProt subcellular location annotations |
| public URL or citation | https://www.uniprot.org/help/subcellular_location and UniProt release documentation, to verify |
| delivery axis | localization proxy |
| data expected | protein accessions, sequences, subcellular location annotations, topology annotations, evidence/provenance fields |
| label type | controlled-vocabulary localization annotations with evidence context where available |
| acquisition mode | source-card-only first; later metadata retrieval only after terms and attribution are reviewed |
| license/access status | to verify from current UniProt license and terms |
| redistribution risk | no-redistribution until current terms and record-level attribution requirements are confirmed |
| provenance fields to preserve | UniProt accession, release/version, annotation term, evidence code, citation, organism, sequence version, access date |
| expected benchmark use | localization / targeting proxy roadmap and evidence-card support |
| limitations | proxy task only; annotations may mix evidence strengths and should not be treated as direct delivery labels |
| immediate next action | verify license/access terms, retrieval mode, release/version recording, and evidence-code policy |

## Notes

UniProt subcellular location annotations are candidate metadata for proxy tasks.
Any future use must preserve accession, release, evidence, and attribution
fields so benchmark users can inspect source context.
