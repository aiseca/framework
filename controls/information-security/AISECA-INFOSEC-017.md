---
id: AISECA-INFOSEC-017
title: "Semantic Context Shifting"
domain: "Information Security"
severity: Medium
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Persistence – AI Agent Context Poisoning (AML.T0080); Conditional: Defense Evasion – LLM Jailbreak (AML.T0054)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://www.cnn.com/2026/03/11/americas/ai-chatbots-help-teen-test-users-plan-violence-tests-intl-invs
---

# AISECA-INFOSEC-017 — Semantic Context Shifting

**Risk.** Gradual changes to conversational or operational context cause an AI system to misinterpret intent and behave unsafely.

**Scenario.** Gradual manipulation changes the AI's understanding of context, leading to unsafe decisions.

## Tier 1 — Define & Constrain

Define session-level behavioral integrity requirements for all conversational AI systems, establishing that harmful intent assessment must account for the full conversation trajectory and not evaluate individual messages in isolation. Require that all deployments include documented semantic drift detection policies specifying which conversation trajectory patterns constitute policy violations even when no single message is independently flagful.

## Tier 2 — Enforce & Monitor

Enforce session-level behavioral monitoring through conversation trajectory analysis that tracks cumulative semantic drift across turns, detecting escalation patterns including gradual persona assignment, incremental normalization of restricted topics, and multi-turn manipulation where individually-benign messages collectively constitute a policy violation.

## Tier 3 — Validate & Adapt

Continuously test semantic context shifting defenses using multi-turn adversarial conversations that simulate realistic gradual escalation, including topic normalization, persona adoption, and incremental boundary testing. Track metrics including trajectory-based detection rate, session-level false positive rate, and mean turns-to-detection. Adapt trajectory models and intervention thresholds based on findings.

## Tooling landscape

**Categories.** AI Guardrails (topic/dialog control); AIDR; AI Red Teaming (AEV)

- NVIDIA NeMo Guardrails (topical rails & dialog-flow constraints) — https://github.com/NVIDIA/NeMo-Guardrails
- Meta Prompt Guard 2 (evaluated per turn) — https://github.com/meta-llama/PurpleLlama
- IBM Granite Guardian — https://github.com/ibm-granite/granite-guardian
- Microsoft PyRIT (multi-turn/Crescendo drift testing) — https://github.com/Azure/PyRIT
