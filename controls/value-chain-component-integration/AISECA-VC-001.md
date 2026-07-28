---
id: AISECA-VC-001
title: "Third-party model risk"
domain: "Value Chain & Component Integration"
severity: High
nist_ai_rmf: ["GOV-3", "MAP-5", "MAN-1"]
mitre_atlas: "Conditional: Resource Development – Publish Poisoned Models (AML.T0058); Resource Development – Publish Poisoned Datasets (AML.T0019); Initial Access – AI Supply Chain Compromise (AML.T0010)"
stakeholders: ["Leadership"]
references:
  - https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face
---

# AISECA-VC-001 — Third-party model risk

**Risk.** A third-party AI model introduces security, reliability, privacy, or compliance risks that are outside the organization's direct control.

**Scenario.** An organization deploys a third-party foundation model that contains undisclosed vulnerabilities or biased behaviors, leading to security gaps, harmful outputs, or regulatory exposure that the organization cannot fully detect or control.

## Tier 1 — Define & Constrain

Define requirements for third-party model selection, including security, safety, and transparency criteria, and restrict use to approved vendors that meet baseline risk and compliance standards.

## Tier 2 — Enforce & Monitor

Implement evaluation and onboarding controls for third-party models, including security testing, performance validation, and contractual safeguards. Continuously monitor model behavior in production for deviations, unsafe outputs, or policy violations, and establish processes for incident response and vendor escalation.

## Tier 3 — Validate & Adapt

Continuously assess third-party model risk through ongoing testing, benchmarking, and comparative evaluations. Track metrics such as incident frequency, model performance drift, and compliance gaps, and adapt vendor selection, integration strategies, and fallback mechanisms to reduce dependency and improve resilience.

## Tooling landscape

**Categories.** AI-SPM / AI Supply Chain Security (model scanning); TPRM; MRM (model risk management)

**Model supply-chain scanning & provenance**

- Palo Alto Networks ModelScan (Protect AI) (unsafe serialization/pickle threats) — https://github.com/protectai/modelscan
- Cisco AI Defense Model Provenance Kit (base-model fingerprinting) — https://github.com/cisco-ai-defense/model-provenance-kit
- Cisco AI Defense Pickle Fuzzer — https://github.com/cisco-ai-defense
- picklescan (used by Hugging Face Hub) — https://github.com/mmaitre314/picklescan
- OpenSSF model-signing (Google/NVIDIA-backed) (signature verification) — https://github.com/sigstore/model-transparency
Pre-deployment evals:
- NVIDIA garak — https://github.com/NVIDIA/garak
- Microsoft PyRIT — https://github.com/Azure/PyRIT
