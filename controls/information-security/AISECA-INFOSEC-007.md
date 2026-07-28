---
id: AISECA-INFOSEC-007
title: "Prompt & instruction manipulation"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Execution – LLM Prompt Injection (AML.T0051); Defense Evasion – LLM Jailbreak (AML.T0054); Persistence – AI Agent Context Poisoning (AML.T0080); Persistence – RAG Poisoning (AML.T0070)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay
---

# AISECA-INFOSEC-007 — Prompt & instruction manipulation

**Risk.** An attacker manipulates prompts or instructions to bypass controls or alter intended AI behavior.

**Scenario.** Someone emails you a PDF you want summarized. The PDF has hidden white on white text with instructions you can't see. Those instructions guide your AI tool to leverage your Gmail MCP to deliver  the full contents of your chat conversation to a threat actor.

## Tier 1 — Define & Constrain

Define system vs. user instruction boundaries by formally documenting which prompt structures, instruction types, and user roles are permitted, and establishing a threat model that covers known manipulation vectors such as prompt injection, jailbreaking, role-play exploits, and indirect instruction override via retrieved or external content. Constrain the system by enforcing strict separation between system-level instructions and user-supplied input, limiting the model's ability to act on instructions embedded in untrusted content, restricting output modalities and tool access to only what the intended use case requires, and requiring all system prompts to be reviewed and approved before deployment.

## Tier 2 — Enforce & Monitor

Enforce separation by deploying prompt filtering layers that detect and block known manipulation patterns and implementing output guardrails that prevent the model from producing responses that violate defined behavioral boundaries regardless of how the prompt is constructed. Monitor manipulation by logging all inputs, instructions, and outputs with sufficient context to reconstruct interaction chains, configuring anomaly detection to flag unusual prompt structures, repeated boundary-probing attempts, or outputs that deviate significantly from expected behavior, and establishing clear escalation paths for suspected manipulation events.

## Tier 3 — Validate & Adapt

Continuously test defenses through regular adversarial red-teaming that systematically attempts prompt injection, instruction hijacking, and jailbreak techniques against deployed systems, using findings to assess whether defined constraints are holding under real-world attack conditions and whether monitoring controls are detecting manipulation attempts with sufficient accuracy. Adapt defenses by updating prompt filtering rules, system prompt structures, and output guardrails in response to newly discovered attack techniques, aligning controls with emerging regulatory guidance on AI robustness, and feeding red-team and incident findings into a continuous improvement cycle so that defenses evolve alongside the manipulation threat landscape.

## Tooling landscape

**Categories.** AI Guardrails / AI Firewall; AIDR; AI Red Teaming (AEV)

**Prompt injection / jailbreak defense**

- Meta Prompt Guard 2 — https://github.com/meta-llama/PurpleLlama
- IBM Granite Guardian (jailbreak detector) — https://github.com/ibm-granite/granite-guardian
- NVIDIA NeMo Guardrails (input rails) — https://github.com/NVIDIA/NeMo-Guardrails
- Palo Alto Networks LLM Guard (Protect AI) — https://github.com/protectai/llm-guard
Testing:
- Microsoft PyRIT — https://github.com/Azure/PyRIT
- NVIDIA garak — https://github.com/NVIDIA/garak
