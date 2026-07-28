---
id: AISECA-BIAS-001
title: "Discriminatory outputs"
domain: "Harmful Bias & Homogenization"
severity: Medium
nist_ai_rmf: ["MAP-3", "MEA-2", "MAN-3"]
mitre_atlas: "No Direct Mapping"
stakeholders: ["Leadership"]
references:
  - https://www.cnbc.com/2019/11/11/regulator-probing-goldmans-apple-card-no-room-for-bias-in-algorithms.html
---

# AISECA-BIAS-001 — Discriminatory outputs

**Risk.** AI produces outputs or decisions that unfairly disadvantage certain individuals or groups.

**Scenario.** A regional bank deploys an AI assistant to support loan officers in drafting preliminary credit assessment narratives for small business applications. The model, fine-tuned on historical loan documentation, generates significantly more skeptical and heavily qualified narratives for businesses owned by applicants from certain demographic backgrounds, using language that signals elevated credit risk without explicit reference to protected characteristics. Loan officers, treating the model's output as a neutral starting point, systematically finalize assessments that reflect the model's biased framing and don't manually review applications. The pattern surfaces only during a fair lending audit eighteen months after deployment, by which time hundreds of applications have been adversely affected.

## Tier 1 — Define & Constrain

Define fairness principles and prohibited bias patterns that apply to all AI systems used in decisions or communications that materially affect customers, employees, or counterparties, with explicit coverage of protected characteristics under applicable law and internal equity commitments. Require that AI deployments in high-stakes decision contexts — including credit assessment, fraud scoring, customer service routing, and compliance screening — include documented fairness requirements approved by the responsible Legal and Compliance function, specifying prohibited output patterns, required demographic parity thresholds, and human oversight requirements. Establish model documentation standards that require disclosure of training data demographic composition, known bias evaluations, and use case scope restrictions prior to deployment approval.

## Tier 2 — Enforce & Monitor

Enforce bias detection and mitigation controls through pre-deployment fairness evaluations that test model outputs across demographic subgroups defined by protected characteristics, and through runtime monitoring that tracks output disparities across population segments in production. Implement human review workflows for high-stakes decision contexts that require adjudication when model outputs exceed defined disparity thresholds or exhibit language patterns associated with historically biased framing. Log all model outputs in decision-relevant contexts with sufficient metadata to support retrospective fairness audits, and alert responsible stakeholders when disparity metrics drift beyond established baselines.

## Tier 3 — Validate & Adapt

Continuously validate fairness controls through scheduled bias evaluations using representative and adversarial test sets that probe for disparate output patterns across protected characteristics and intersectional subgroups. Track metrics including demographic parity ratios, equalized odds gaps, output sentiment disparity by subgroup, and human override rates by demographic segment. Conduct retrospective audits of production decisions to detect disparate impact patterns that may not be visible in per-output monitoring, and adapt model selection, fine-tuning, and prompt engineering in response to findings. Update fairness thresholds and evaluation criteria as regulatory requirements and internal equity standards evolve.

## Tooling landscape

**Categories.** Responsible AI / AI Governance (bias auditing); AI TRiSM

**Bias testing & mitigation**

- IBM AI Fairness 360 — https://github.com/Trusted-AI/AIF360
- Microsoft Fairlearn — https://github.com/fairlearn/fairlearn
- Google Fairness Indicators — https://github.com/tensorflow/fairness-indicators
Runtime output screening:
- IBM Granite Guardian (social-bias detector) — https://github.com/ibm-granite/granite-guardian
