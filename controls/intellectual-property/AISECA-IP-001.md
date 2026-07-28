---
id: AISECA-IP-001
title: "Proprietary data leakage"
domain: "Intellectual Property"
severity: High
nist_ai_rmf: ["MAP-2", "MAN-4"]
mitre_atlas: "Direct: Exfiltration – LLM Data Leakage (AML.T0057); Exfiltration – Exfiltration via AI Inference API (AML.T0024); Exfiltration – Exfiltration via AI Agent Tool Invocation (AML.T0086); Impact – External Harms (AML.T0048)"
stakeholders: ["Leadership"]
references:
  - https://www.forbes.com/sites/siladityaray/2023/05/02/samsung-bans-chatgpt-and-other-chatbots-for-employees-after-sensitive-code-leak/
---

# AISECA-IP-001 — Proprietary data leakage

**Risk.** Sensitive or confidential information is exposed to unauthorized users, systems, or organizations.

**Scenario.** An AI system unintentionally generates outputs that reveal proprietary business information, such as internal documents, source code, or trade secrets, due to training data exposure or prompt-based extraction.

## Tier 1 — Define & Constrain

Define and enforce policies that prohibit the inclusion, retention, or generation of proprietary or confidential data in model outputs, including restrictions on training data sources and guidance for handling sensitive inputs.

## Tier 2 — Enforce & Monitor

Implement controls such as data loss prevention (DLP), output filtering, and access restrictions to prevent leakage of sensitive or proprietary information. Monitor for patterns indicative of data extraction attempts and enforce redaction, blocking, or safe-response mechanisms when risks are detected.

## Tier 3 — Validate & Adapt

Continuously test for data leakage risks using red teaming and extraction attack simulations. Track metrics such as leakage rate, sensitive data exposure, and effectiveness of filtering controls, and refine safeguards, training practices, and monitoring based on observed vulnerabilities and evolving threat techniques.

## Tooling landscape

**Categories.** DLP; DSPM; AI Guardrails (sensitive-data filtering)

**DLP for prompts, outputs & repos**

- Microsoft Presidio (detection/redaction) — https://github.com/microsoft/presidio
- Palo Alto Networks LLM Guard (Protect AI) (sensitive-data & secrets scanners) — https://github.com/protectai/llm-guard
- Yelp detect-secrets — https://github.com/Yelp/detect-secrets
- AWS git-secrets — https://github.com/awslabs/git-secrets
- OpenSearch (AWS) (egress-pattern monitoring) — https://opensearch.org
