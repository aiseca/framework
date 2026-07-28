---
id: AISECA-INFOSEC-016
title: "Multimodal Injection"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Execution – LLM Prompt Injection (AML.T0051); Conditional: Defense Evasion – LLM Prompt Obfuscation (AML.T0068)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
---

# AISECA-INFOSEC-016 — Multimodal Injection

**Risk.** Malicious instructions embedded in images, documents, audio, or other non-text inputs alter AI behavior.

**Scenario.** Hidden instructions in images, documents, or audio cause unintended AI behavior.

## Tier 1 — Define & Constrain

Define trust boundaries for all non-text modalities ingested by multimodal AI systems, establishing that visual, audio, and document inputs are untrusted by default and cannot override system prompt instructions or trigger privileged actions. Require that all multimodal AI deployments include a documented inventory of accepted input types with corresponding trust classification and processing restrictions.

## Tier 2 — Enforce & Monitor

Enforce multimodal input controls through per-modality sanitization pipelines that analyze non-text inputs for embedded instruction patterns before combining with text inputs in model context. Implement output monitoring that detects behavioral changes correlated with specific multimodal input events, and alert when model actions following multimodal input deviate from expected task scope.

## Tier 3 — Validate & Adapt

Continuously test multimodal injection defenses using adversarial inputs that embed payloads across all supported modalities — images with hidden text, audio with embedded instruction signals, documents with concealed directives. Track metrics including cross-modal injection detection rate and false negative rate by modality. Adapt sanitization controls based on findings and newly published cross-modal attack techniques.

## Tooling landscape

**Categories.** AI Guardrails (multimodal moderation); AI Red Teaming (AEV)

- Meta Llama Guard 3 Vision (joint image+text safety classification) — https://huggingface.co/meta-llama/Llama-Guard-3-11B-Vision
- Microsoft PyRIT (image-based attack modules) — https://github.com/Azure/PyRIT
- NVIDIA garak (visual jailbreak probes) — https://github.com/NVIDIA/garak
- NVIDIA NeMo Guardrails (input rails on content extracted from media) — https://github.com/NVIDIA/NeMo-Guardrails
