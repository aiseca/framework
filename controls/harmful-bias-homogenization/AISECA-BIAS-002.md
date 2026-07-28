---
id: AISECA-BIAS-002
title: "Exclusionary recommendations"
domain: "Harmful Bias & Homogenization"
severity: Medium
nist_ai_rmf: ["MAP-3", "MEA-2", "MAN-3"]
mitre_atlas: "No Direct Mapping"
stakeholders: ["Leadership"]
references:
  - https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G/
---

# AISECA-BIAS-002 — Exclusionary recommendations

**Risk.** AI recommends, prioritizes, or excludes people in ways that unfairly limit access to opportunities, services, or resources.

**Scenario.** An AI-powered recommendation system consistently suggests candidates, vendors, or content that reflect a narrow demographic profile, excluding qualified individuals or perspectives and reinforcing systemic bias in decision-making processes.

## Tier 1 — Define & Constrain

Define fairness and inclusion requirements for AI outputs, including constraints that prevent exclusionary or biased recommendations based on protected or sensitive attributes, and establish guidelines for representative and diverse outputs.

## Tier 2 — Enforce & Monitor

Implement bias detection and mitigation controls within model outputs and recommendation logic, including fairness checks, diversity constraints, and monitoring for skewed outcomes across demographic groups. Track and investigate disparities, and enforce corrective actions when bias thresholds are exceeded.

## Tier 3 — Validate & Adapt

Continuously evaluate system fairness using adversarial testing, representative datasets, and quantitative fairness metrics. Monitor trends in exclusionary outcomes, validate mitigation effectiveness, and refine models and controls to address emerging bias patterns and maintain equitable performance across populations.

## Tooling landscape

**Categories.** Responsible AI / AI Governance (fairness auditing); AI TRiSM

**Fairness auditing of rankings/decisions**

- Microsoft Fairlearn (group fairness metrics & mitigation) — https://github.com/fairlearn/fairlearn
- IBM AI Fairness 360 — https://github.com/Trusted-AI/AIF360
- LinkedIn Fairness Toolkit (LiFT) — https://github.com/linkedin/LiFT
- Google What-If Tool (counterfactual review) — https://github.com/PAIR-code/what-if-tool
