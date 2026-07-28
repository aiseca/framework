---
id: AISECA-INTG-002
title: "Output manipulation"
domain: "Information Integrity"
severity: Medium
nist_ai_rmf: ["MAP-3", "MEA-1", "MAN-2"]
mitre_atlas: "Direct: Execution – LLM Prompt Injection (AML.T0051); Persistence – RAG Poisoning (AML.T0070); Persistence – AI Agent Context Poisoning (AML.T0080); Defense Evasion – False RAG Entry Injection (AML.T0071); Impact – Erode AI Model Integrity (AML.T0031)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://arxiv.org/abs/2302.12173
---

# AISECA-INTG-002 — Output manipulation

**Risk.** An attacker, user, or external influence alters AI outputs to achieve unintended or harmful outcomes.

**Scenario.** An attacker injects malicious or biased data into a retrieval source or prompt context, causing the AI system to generate manipulated outputs that mislead users or influence decision-making.

## Tier 1 — Define & Constrain

Define trust boundaries for input sources and model context, restricting the model from treating unverified or external content as authoritative without validation, and establishing guidelines for safe handling of dynamic or user-supplied inputs.

## Tier 2 — Enforce & Monitor

Implement controls such as input validation, source attribution, and integrity checks for retrieved or injected content. Monitor for signs of prompt injection, data poisoning, or anomalous context manipulation, and enforce safe-response patterns or isolation when integrity cannot be assured.

## Tier 3 — Validate & Adapt

Continuously test resilience against output manipulation using adversarial scenarios (e.g., prompt injection, poisoned retrieval corpora). Track metrics such as manipulation success rate and detection coverage, and refine trust frameworks, validation mechanisms, and monitoring based on evolving attack techniques.

## Tooling landscape

**Categories.** AI Guardrails / AI Firewall; AIDR; SSCS (artifact signing)

**Output integrity & manipulation defense**

- Palo Alto Networks LLM Guard (Protect AI) (output scanners) — https://github.com/protectai/llm-guard
- Meta LlamaFirewall — https://github.com/meta-llama/PurpleLlama
- NVIDIA NeMo Guardrails (output rails) — https://github.com/NVIDIA/NeMo-Guardrails
- Sigstore cosign (OpenSSF) (signing of published artifacts) — https://github.com/sigstore/cosign
Adversarial testing:
- Microsoft PyRIT — https://github.com/Azure/PyRIT
