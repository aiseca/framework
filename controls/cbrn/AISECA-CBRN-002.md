---
id: AISECA-CBRN-002
title: "Dual-use misuse"
domain: "CBRN (Chemical, Biological, Radiological, Nuclear)"
severity: Medium
nist_ai_rmf: ["GOV-1", "MAP-3", "MAN-3"]
mitre_atlas: "Conditional: Resource Development – Obtain Capabilities (AML.T0016); Impact – External Harms (AML.T0048)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc
---

# AISECA-CBRN-002 — Dual-use misuse

**Risk.** AI capabilities intended for legitimate purposes are used to support harmful, dangerous, or prohibited activities.

**Scenario.** A Day Porter looks up what cleaning chemicals not to mix. The AI outputs a list of dangerous combinations and explains what toxic gases can be produced.

## Tier 1 — Define & Constrain

Define review requirements for sensitive dual-use queries by formally identifying the categories of CBRN-adjacent content such as synthesis routes, weaponization methods, dispersal mechanisms, and acquisition pathways that require elevated scrutiny, and establishing clear criteria for what constitutes meaningful uplift versus legitimate educational or research use. Constrain the system by implementing hard refusal boundaries for the highest-risk query types regardless of stated intent, restricting access to detailed technical content in CBRN domains to verified use cases, and requiring legal and safety review before any AI application is deployed in contexts where CBRN dual-use queries are foreseeable.

## Tier 2 — Enforce & Monitor

Enforce review and response workflows by deploying classifiers that detect CBRN-relevant queries in real time, routing flagged inputs through human review or automated refusal pipelines before a response is generated, and maintaining a tiered response framework that distinguishes between queries requiring redirection, partial response, or hard refusal. Monitor by logging all flagged queries and outcomes to build an auditable record, tracking patterns in dual-use query attempts to identify coordinated or escalating misuse, and establishing reporting obligations to relevant authorities where queries indicate credible threat intent.

## Tier 3 — Validate & Adapt

Continuously validate effectiveness of safeguards by conducting structured red-team exercises that probe CBRN refusal boundaries using both direct and indirect query strategies, measuring whether classifiers and refusal policies hold against novel phrasing, multi-step elicitation, and context manipulation attempts. Adapt by updating detection classifiers and refusal criteria as new attack vectors and dual-use query patterns emerge, aligning controls with evolving biosecurity, export control, and AI safety regulations, and incorporating findings from red-teaming and incident reviews into a continuous improvement cycle for CBRN safeguards.

## Tooling landscape

**Categories.** AI Guardrails (AI TRiSM); AIDR (misuse monitoring); AI Red Teaming (AEV)

**Misuse detection & policy enforcement**

- NVIDIA NeMo Guardrails (tiered response flows) — https://github.com/NVIDIA/NeMo-Guardrails
- Meta Llama Guard 3 — https://github.com/meta-llama/PurpleLlama
- IBM Granite Guardian — https://github.com/ibm-granite/granite-guardian
Adversarial probing of refusal boundaries:
- Microsoft PyRIT (multi-turn attack orchestration) — https://github.com/Azure/PyRIT
- NVIDIA garak — https://github.com/NVIDIA/garak
