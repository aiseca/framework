---
id: AISECA-INTG-001
title: "Misinformation propagation"
domain: "Information Integrity"
severity: Medium
nist_ai_rmf: ["MAP-3", "MEA-1", "MAN-2"]
mitre_atlas: "Conditional: Resource Development – Publish Hallucinated Entities (AML.T0060); Impact – External Harms (AML.T0048)"
stakeholders: ["Leadership"]
references: []
---

# AISECA-INTG-001 — Misinformation propagation

**Risk.** AI creates, amplifies, or spreads false, misleading, or deceptive information.

**Scenario.** An asset manager deploys an internal AI assistant to help analysts draft market commentary and client-facing communications. An analyst asks the model to summarize recent regulatory guidance on capital reserve requirements. The model, lacking grounding to authoritative regulatory sources and last updated over a year ago, generates a plausible but inaccurate summary that mischaracterizes a pending rule's implementation timeline and applicability thresholds. Under deadline pressure, the analyst publishes the commentary to an institutional client distribution list without independent verification. Clients make portfolio adjustments based on the incorrect regulatory summary, resulting in compliance exposure and client relationship damage when the error is discovered.

https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5651130

https://www.theregreview.org/2025/11/25/smith-ai-and-the-future-of-market-manipulation/

## Tier 1 — Define & Constrain

Define information integrity requirements for AI systems used to generate factual claims, regulatory guidance, market commentary, or other content where accuracy directly affects business or client outcomes, requiring that outputs in these categories be grounded to authoritative and verifiable sources. Establish a taxonomy of high-stakes content categories where AI-generated content must be explicitly labeled as AI-assisted and subject to human verification before publication or external distribution, and prohibit AI systems from asserting factual certainty on topics outside their verified knowledge scope. Require that all AI deployments in information-sensitive contexts include documented grounding requirements, context on when model was last trained, approved source allowlists, and mandatory disclosure language reviewed by the responsible Legal and Compliance function.

## Tier 2 — Enforce & Monitor

Enforce information integrity controls through retrieval-augmented generation architectures that ground factual outputs to approved source corpora — including regulatory databases, official filings, and internal knowledge repositories — and through output monitoring that flags claims lacking traceable grounding citations. Implement confidence scoring and uncertainty disclosure mechanisms that surface low-confidence assertions before outputs are presented to users, and require that outputs exceeding defined uncertainty thresholds trigger human review workflows before distribution. Monitor for misinformation propagation patterns including outputs that contradict known-authoritative sources and outputs that assert specificity not supported by available grounding evidence.

## Tier 3 — Validate & Adapt

Continuously test information integrity controls using adversarial and out-of-distribution queries that probe for confident misinformation generation, including questions about recent regulatory changes, novel market events, and topics at the boundaries of the model's verified knowledge. Track metrics including grounding citation rate, factual accuracy rate on hold-out evaluation sets, human correction rate in review workflows, and downstream error rate for AI-assisted content that reaches distribution. Conduct periodic red team exercises targeting information integrity, including scenarios where source corpora are stale or incomplete, and adapt grounding architectures, confidence calibration, and human review thresholds based on observed failure patterns.

## Tooling landscape

**Categories.** Disinformation Security (provenance & watermarking); AI Guardrails

**Content provenance & watermarking**

- Google SynthID Text — https://github.com/google-deepmind/synthid-text
- c2patool / C2PA (Adobe-led, with Microsoft/Google/Intel) (content credentials) — https://github.com/contentauth/c2patool
- Meta Llama Guard 3 (output moderation) — https://github.com/meta-llama/PurpleLlama
- NVIDIA NeMo Guardrails (fact-check rails) — https://github.com/NVIDIA/NeMo-Guardrails
