---
id: AISECA-IP-003
title: "Model inversion"
domain: "Intellectual Property"
severity: High
nist_ai_rmf: ["MAP-2", "MAN-4"]
mitre_atlas: "Direct: Exfiltration – Exfiltration via AI Inference API (AML.T0024)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://arxiv.org/pdf/2507.04478
---

# AISECA-IP-003 — Model inversion

**Risk.** Someone uses AI outputs to recover sensitive information that was present in training data.

**Scenario.** An attacker queries a financial services' firm's AI agent with targeted inputs, analyzing confidence scores across responses to reverse-engineer whether non-public historical M&A transaction records records were included in the model's training data.

## Tier 1 — Define & Constrain

Publish a data governance policy defining which datasets (PII, confidential client records, etc.) are prohibited or restricted for use in training and fine-tuning. Hold privacy impact assessment before sensitive data is used, if at all. Prefer retrieval-augmented approaches over fine-tuning for confidential content. Apply data minimization, de-identification, and other privacy techniques before training. Restrict external deployment of models trained on highly sensitive information to authenticated, approved, and scoped use cases.

## Tier 2 — Enforce & Monitor

Enforce rate limits and query quotas per user and key. Apply output filters that detect and block responses containing memorized training artifacts such as verbatim records or unique identifiers. Log all queries with user attribution and monitor for indications of inversion such as including repeated duplicate probes with thresholds that trigger throttling, key revocation, or escalation.

## Tier 3 — Validate & Adapt

Conduct periodic exercises against deployed models, and measure leakage. Benchmark models for memorization of sensitive records before release and make deployment continget on results. Audit training pipelines to confirm data minimization and privacy techniques are applied and feed findings into updated training practices, model selection, and gatekeeping rules. Integrate inversion incidents into enterprise risk reporting, privacy reviews, and regulatory disclosures where applicable.

## Tooling landscape

**Categories.** PEC; AI TRiSM (model privacy); AI Red Teaming (privacy attack testing)

**Privacy attack testing & DP training**

- IBM Adversarial Robustness Toolbox (ART) (model inversion & membership-inference modules) — https://github.com/Trusted-AI/adversarial-robustness-toolbox
- Google TensorFlow Privacy (DP-SGD) — https://github.com/tensorflow/privacy
- Microsoft SmartNoise (OpenDP) — https://github.com/opendp/smartnoise-sdk
- IBM ai-privacy-toolkit (model anonymization) — https://github.com/IBM/ai-privacy-toolkit
