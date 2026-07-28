---
id: AISECA-INFOSEC-008
title: "Model extraction or abuse"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: AI Model Access – AI Model Inference API Access (AML.T0040); Exfiltration – Exfiltration via AI Inference API (AML.T0024); Impact – External Harms (AML.T0048)"
stakeholders: ["Leadership"]
references: []
---

# AISECA-INFOSEC-008 — Model extraction or abuse

**Risk.** An AI model is copied, stolen, abused, or used in ways not authorized by its owner.

**Scenario.** A competitor makes carefully crafted queries to a company's customer-facing AI agent, systematically mapping its responses to reconstruct proprietary fine-tuning data and replicate the model's specialized behavior.

https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained

https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use

## Tier 1 — Define & Constrain

Publish a policy defining which models, fine-tuned capabilities, and training datasets are considered intellectual property, and restrict external-facing deployments of highly specialized or sensitive models. Require authentication for model access and prohibit anonymous or unbounded querying. Configure rate limits, query quotas, and response-length caps. Scope system prompts to minimize disclosure of proprietary instructions or data, and apply terms of service that explicitly prohibit scraping, extraction, and derivative model training.

## Tier 2 — Enforce & Monitor

Deploy controls that enforce per-user/per-key rate limits, block suspicious query volumes. Log all queries and responses with user attribution, and monitor for indications of extraction. Trigger automated throttling, key revocation, or escalation when extraction patterns or abuse indicators breach defined thresholds.

## Tier 3 — Validate & Adapt

Conduct periodic exercises simulating extraction attacks. Measure how much proprietary behavior can be reconstructed. Benchmark detection rules against known extraction research and update signatures accordingly. Audit access patterns for anomalous clients and review whether rate limits and output filters hold under realistic load. Feed findings into updated gateway rules, model deployment decisions, and contractual enforcement, and integrate extraction incidents into enterprise risk reporting and threat intelligence sharing.

## Tooling landscape

**Categories.** AIDR (model abuse detection); API Security / WAAP (rate limiting); AI Red Teaming (AEV)

**Extraction testing & API abuse controls**

- IBM Adversarial Robustness Toolbox (ART) (extraction attack simulation & defenses) — https://github.com/Trusted-AI/adversarial-robustness-toolbox
- Envoy (Lyft-originated/CNCF) (authentication + rate limiting on model endpoints) — https://github.com/envoyproxy/envoy
- Microsoft Counterfit — https://github.com/Azure/counterfit
- NVIDIA garak — https://github.com/NVIDIA/garak
