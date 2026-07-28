---
id: AISECA-INFOSEC-015
title: "Recursive Prompt Injection (LLM-as-a-Judge)"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Execution – LLM Prompt Injection (AML.T0051); Conditional: Defense Evasion – LLM Trusted Output Components Manipulation (AML.T0067)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://medium.com/@instatunnel/prompt-injection-the-attack-that-makes-ai-do-your-bidding-9c8c672b6dec
---

# AISECA-INFOSEC-015 — Recursive Prompt Injection (LLM-as-a-Judge)

**Risk.** Malicious instructions manipulate an AI system that evaluates or approves other AI-generated outputs or actions.

**Scenario.** Malicious prompts manipulate AI-based evaluation, causing unsafe actions to be approved.

## Tier 1 — Define & Constrain

Define trust boundaries for LLM-as-a-Judge architectures, requiring that judge models treat all candidate inputs as untrusted data and cannot be directed by content within evaluated candidates. Establish policies prohibiting judge models from following instructions found in content they are evaluating, and require that judge prompts are isolated from evaluated content via structured separation.

## Tier 2 — Enforce & Monitor

Enforce context isolation in LLM-as-a-Judge pipelines through input sanitization that strips instruction-like content from evaluated candidates before presentation to the judge model. Implement secondary validation of judge outputs to detect anomalous scoring patterns, including uniform selection of a single candidate or scoring distributions inconsistent with stated criteria.

## Tier 3 — Validate & Adapt

Continuously test LLM-as-a-Judge implementations using adversarial candidate inputs that embed injection payloads designed to influence scoring, including instruction overrides, role manipulation, and criteria-subversion techniques. Track metrics including injection detection rate, judge output anomaly rate, and false-positive rate for legitimate candidates flagged. Adapt isolation controls based on findings.

## Tooling landscape

**Categories.** AI Guardrails / AI Firewall; AI Red Teaming (AEV)

- Meta LlamaFirewall (Prompt Guard 2 screening judge inputs) — https://github.com/meta-llama/PurpleLlama
- IBM Granite Guardian (jailbreak detection) — https://github.com/ibm-granite/granite-guardian
- NVIDIA NeMo Guardrails (isolate judge context from evaluated content) — https://github.com/NVIDIA/NeMo-Guardrails
- Microsoft PyRIT (multi-turn/Crescendo-style escalation testing) — https://github.com/Azure/PyRIT
- NVIDIA garak — https://github.com/NVIDIA/garak
