---
id: AISECA-HAIC-001
title: "Automation bias"
domain: "Human–AI Configuration & Overreliance"
severity: Medium
nist_ai_rmf: ["GOV-2", "MAP-4", "MAN-2"]
mitre_atlas: "No Direct Mapping"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-HAIC-001 — Automation bias

**Risk.** People place too much trust in AI outputs and fail to apply appropriate human judgment or verification.

**Scenario.** A SOC team configures an AI agent to triage alerts. A genuine intrusion receives a low-priority alert by the model. Analysts, conditioned to trust its scoring, skip manual review and miss an active exploitation.

## Tier 1 — Define & Constrain

Establish policies that prevent uncritical reliance on AI outputs in high-stakes domains or other consequential decisions. Require role-based training on automation bias. Where available configure AI services to include model confidence, reasoning, known limitations, and other relevant contextual information alongside output. Avoid defaulting to the AI's recommendation in UI workflows. Preserve raw data so analysts can review source evidence without relying solely on model summaries.

## Tier 2 — Enforce & Monitor

Enforce human approval for critical actions. Require mandatory human review checkpoints for decisions above defined impact thresholds. Apply sampling rules that force manual review of a percentage of low-priority AI classifications to catch false negatives. Log reviewer actions and override rates. Monitor for signs of rubber-stamping such as near-zero review times or unusually high agreement rates. Trigger escalation when override patterns or missed-detection indicators breach defined thresholds, and feed exceptions into supervisory review.

## Tier 3 — Validate & Adapt

Conduct periodic exercises that inject known-malicious or high-severity cases misclassified as low priority, and measure whether analysts catch them. Track false negative rates for consequential categories or high-stakes domains. Audit reviewer calibration to confirm humans are adding judgment rather than deferring, and adjust thresholds, UI design, or training based on findings. Feed results into updated triage playbooks and model selection, and integrate automation bias incidents into enterprise risk reporting and lessons-learned sharing with industry peers.

## Tooling landscape

**Categories.** XAI / Responsible AI (explainability & uncertainty); AI Governance

**Explainability & uncertainty surfacing**

- IBM AI Explainability 360 — https://github.com/Trusted-AI/AIX360
- Microsoft InterpretML — https://github.com/interpretml/interpret
- Google Learning Interpretability Tool (LIT) — https://github.com/PAIR-code/lit
- IBM Uncertainty Quantification 360 (confidence display to prompt human verification) — https://github.com/IBM/UQ360
