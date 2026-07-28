---
id: AISECA-CBRN-001
title: "CBRN knowledge enablement"
domain: "CBRN (Chemical, Biological, Radiological, Nuclear)"
severity: Medium
nist_ai_rmf: ["GOV-1", "MAP-3", "MAN-3"]
mitre_atlas: "Conditional: Impact – External Harms (AML.T0048); Defense Evasion – LLM Jailbreak (AML.T0054)"
stakeholders: ["Leadership"]
references:
  - https://www.rand.org/pubs/research_reports/RRA2977-1.html
---

# AISECA-CBRN-001 — CBRN knowledge enablement

**Risk.** AI provides information that helps someone create, acquire, or use dangerous chemical, biological, radiological, or nuclear materials.

**Scenario.** An AI assistant provides step-by-step guidance that lowers the technical barrier for synthesizing a toxic chemical agent, enabling a user without formal training to progress from theoretical understanding to actionable capability.

## Tier 1 — Define & Constrain

Define and enforce strict content boundaries prohibiting the generation of actionable CBRN-related guidance, including synthesis methods, material acquisition, weaponization techniques, or procedural steps, while allowing only high-level, non-operational educational information with clear safety framing.

## Tier 2 — Enforce & Monitor

Implement and enforce policy-aligned detection and filtering mechanisms for CBRN-related prompts and outputs, including classification models, keyword/pattern controls, and contextual risk scoring. Monitor for attempts to elicit restricted knowledge (e.g., prompt chaining, obfuscation), trigger safe-response fallbacks, and route high-risk interactions to logging and incident response workflows.

## Tier 3 — Validate & Adapt

Continuously evaluate system resilience against adversarial probing using red teaming and automated test suites targeting CBRN knowledge extraction techniques. Track metrics such as policy evasion rate, unsafe response frequency, and detection coverage, and iteratively refine controls, detection models, and response strategies based on emerging threat patterns and misuse attempts.

## Tooling landscape

**Categories.** AI Guardrails / AI Firewall (GenAI runtime defense); AI TRiSM; AI Red Teaming (AEV)

**Content safety guardrails & CBRN red-teaming**

- Meta Llama Guard 3 (indiscriminate weapons/CBRN category) — https://github.com/meta-llama/PurpleLlama
- Google ShieldGemma — https://ai.google.dev/gemma/docs/shieldgemma
- NVIDIA NeMo Guardrails (topical rails) — https://github.com/NVIDIA/NeMo-Guardrails
- IBM Granite Guardian — https://github.com/ibm-granite/granite-guardian
Tier 3 validation:
- Microsoft PyRIT — https://github.com/Azure/PyRIT
- NVIDIA garak — https://github.com/NVIDIA/garak
