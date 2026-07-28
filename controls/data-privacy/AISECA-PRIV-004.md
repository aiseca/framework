---
id: AISECA-PRIV-004
title: "Re-identification risk"
domain: "Data Privacy"
severity: High
nist_ai_rmf: ["MAP-2", "MAN-4"]
mitre_atlas: "Conditional: Exfiltration – Exfiltration via AI Inference API (AML.T0024)"
stakeholders: ["Leadership"]
references:
  - https://www.nature.com/articles/s41467-019-10933-3
---

# AISECA-PRIV-004 — Re-identification risk

**Risk.** AI enables someone to identify an individual who was intended to remain anonymous.

**Scenario.** An AI model generates outputs that, when combined with external data, enable the re-identification of an individual from previously anonymized datasets, exposing sensitive personal information and creating regulatory and legal risk.

## Tier 1 — Define & Constrain

Define and enforce restrictions on the use, retention, and generation of sensitive or personal data, including policies that prohibit outputs that could directly or indirectly enable re-identification of individuals from anonymized or aggregated data.

## Tier 2 — Enforce & Monitor

Implement technical controls such as data minimization, de-identification techniques, and privacy-preserving mechanisms (e.g., filtering, access controls) to prevent re-identification risks. Monitor outputs for potential leakage of quasi-identifiers or sensitive attributes and trigger mitigation actions when risk thresholds are exceeded.

## Tier 3 — Validate & Adapt

Continuously evaluate re-identification risk through privacy testing methods (e.g., simulated linkage attacks, red teaming) and track metrics such as re-identification success rates and sensitive attribute exposure. Adapt data handling practices, model safeguards, and monitoring thresholds in response to evolving privacy risks and regulatory expectations.

## Tooling landscape

**Categories.** PEC (Privacy-Enhancing Computation); Privacy Management; AI TRiSM (model privacy)

**Anonymization & differential privacy**

- Microsoft Presidio — https://github.com/microsoft/presidio
- Microsoft SmartNoise (OpenDP) — https://github.com/opendp/smartnoise-sdk
- Google differential-privacy libraries — https://github.com/google/differential-privacy
- Google TensorFlow Privacy (DP-SGD training) — https://github.com/tensorflow/privacy
- IBM ai-privacy-toolkit — https://github.com/IBM/ai-privacy-toolkit
