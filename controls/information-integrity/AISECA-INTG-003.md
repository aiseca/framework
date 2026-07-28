---
id: AISECA-INTG-003
title: "Lack of provenance"
domain: "Information Integrity"
severity: Medium
nist_ai_rmf: ["MAP-3", "MEA-1", "MAN-2"]
mitre_atlas: "Conditional: Resource Development – Publish Poisoned Models (AML.T0058); Resource Development – Publish Poisoned Datasets (AML.T0019); Resource Development – Publish Poisoned AI Agent Tool (AML.T0104); Initial Access – AI Supply Chain Compromise (AML.T0010)"
stakeholders: ["Builder / Maintainer"]
references:
  - https://jnm.snmjournals.org/content/early/2025/11/06/jnumed.125.270653
---

# AISECA-INTG-003 — Lack of provenance

**Risk.** The origin, history, or source of information, decisions, or actions cannot be verified.

**Scenario.** A Generative AI tool used to support diagnostic analysis of medical images introduces phantom anomalies, such as a fracture-like line in an unbroken bone or a lesion in healthy tissue. This could directly impact health outcomes.

## Tier 1 — Define & Constrain

Define provenance requirements as a formal standard for all data entering AI systems, specifying that every dataset must have a documented origin, collection method, ownership status, and chain of custody before it is eligible for use in training, fine-tuning, or retrieval pipelines. Constrain the system by prohibiting the use of any data whose provenance cannot be verified, requiring all data sources to be registered in a governed catalog with lineage metadata, and mandating that third-party and vendor-supplied datasets include provenance documentation as a contractual condition of use.

## Tier 2 — Enforce & Monitor

Enforce provenance controls by implementing automated pipeline checks that validate lineage metadata at every data ingestion point, blocking datasets that lack verified origin records from entering AI workflows, and applying cryptographic hashing or digital watermarking to track data integrity from source through to model training. Monitor by maintaining a live data lineage graph that traces the journey of every dataset across ingestion, transformation, and training stages, alerting on any gaps, modifications, or unregistered data sources that appear in the pipeline.

## Tier 3 — Validate & Adapt

Validate by conducting regular lineage audits that reconcile what data was intended to be used against what was actually ingested, probing deployed models for outputs that suggest untraceable or suspect training sources, and cross-referencing provenance records against known high-risk datasets such as those with disputed rights or unverified collection practices. Adapt by updating provenance requirements as new data sources and AI pipeline patterns emerge, aligning standards with evolving regulatory obligations such as the EU AI Act's transparency and documentation requirements, and embedding provenance review into post-incident analysis so that each gap identified strengthens future controls.

## Tooling landscape

**Categories.** SSCS (signing, attestation, SBOM); Disinformation Security (content credentials); AI-SPM

**Provenance, signing & attestation**

- Sigstore cosign (OpenSSF) — https://github.com/sigstore/cosign
- OpenSSF model-signing (Google/NVIDIA-backed) — https://github.com/sigstore/model-transparency
- c2patool / C2PA (Adobe-led, with Microsoft/Google/Intel) — https://github.com/contentauth/c2patool
- GUAC (Google/OpenSSF) (supply-chain knowledge graph) — https://github.com/guacsec/guac
- SLSA provenance framework (Google/OpenSSF) — https://slsa.dev
- Cisco AI Defense Model Provenance Kit — https://github.com/cisco-ai-defense/model-provenance-kit
