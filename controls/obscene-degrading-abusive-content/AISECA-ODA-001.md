---
id: AISECA-ODA-001
title: "Sexually explicit outputs"
domain: "Obscene, Degrading, or Abusive Content"
severity: Low
nist_ai_rmf: ["MAP-3", "MAN-3"]
mitre_atlas: "Conditional: Execution – LLM Prompt Injection (AML.T0051); Defense Evasion – LLM Jailbreak (AML.T0054); Impact – External Harms (AML.T0048)"
stakeholders: ["Leadership"]
references:
  - https://en.wikipedia.org/wiki/Prompt_injection
---

# AISECA-ODA-001 — Sexually explicit outputs

**Risk.** AI generates sexually explicit content that is inappropriate, harmful, or violates policy or legal requirements.

**Scenario.** An AI system generates sexually explicit content in response to a user query or prompt. As a result, the system produces inappropriate material that can harm users, violate policy, or damage trust.

## Tier 1 — Define & Constrain

Define clear guardrails for what types of content are allowed is not allowed, including restrictions on sexually explicit material. Ensure these rules are consistently applied across all AI use cases and environments.

## Tier 2 — Enforce & Monitor

Enforce content controls that prevent the system from generating disallowed sexual content, including filtering inputs and outputs and applying safeguards during generation. Ensure the system consistently blocks or redirects inappropriate requests based on defined policies.

## Tier 3 — Validate & Adapt

Continuously adapt by testing the system against edge cases and monitoring outputs to identify gaps in content controls. Refine policies and safeguards over time to improve accuracy, reduce false negatives, and ensure consistent enforcement as usage evolves.

## Tooling landscape

**Categories.** Content Moderation (Trust & Safety); AI Guardrails

**Content moderation classifiers**

- Meta Llama Guard 3 (sexual-content categories) — https://github.com/meta-llama/PurpleLlama
- Meta Llama Guard 3 Vision (image inputs) — https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision
- Google ShieldGemma (sexually explicit content) — https://ai.google.dev/gemma/docs/shieldgemma
- IBM Granite Guardian — https://github.com/ibm-granite/granite-guardian
- NVIDIA NeMo Guardrails (output rails) — https://github.com/NVIDIA/NeMo-Guardrails
