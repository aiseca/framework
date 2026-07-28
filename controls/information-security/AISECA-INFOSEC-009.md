---
id: AISECA-INFOSEC-009
title: "Indirect Prompt Injection"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Execution – LLM Prompt Injection (AML.T0051); Privilege Escalation – AI Agent Tool Invocation (AML.T0053); Exfiltration – Exfiltration via AI Agent Tool Invocation (AML.T0086)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://en.wikipedia.org/wiki/Prompt_injection
---

# AISECA-INFOSEC-009 — Indirect Prompt Injection

**Risk.** Instructions hidden within external content manipulate AI behavior without the user's awareness.

**Scenario.** An AI assistant retrieves external content while responding to a user request, but the content contains hidden malicious instructions that the model follows. As a result, the system’s behavior is manipulated or sensitive data is exposed without any direct attack in the user’s prompt.

## Tier 1 — Define & Constrain

Define trust boundaries for all external content and do not rely on the system to distinguish between data and instructions; restrict how external content can influence behavior, especially when sensitive data or actions are involved.

## Tier 2 — Enforce & Monitor

Enforce controls that prevent external content from directly triggering actions or accessing sensitive data, requiring all actions to go through defined checks and approvals. Isolate retrieved external content from system instructions, and restrict access to tools or data unless explicitly authorized; monitor for attempts to influence behavior or bypass controls.

## Tier 3 — Validate & Adapt

Continuously test the system against indirect prompt injection scenarios by simulating malicious or embedded instructions in external content. Monitor whether these influence system behavior or trigger unauthorized actions, and refine controls over time to ensure external content cannot bypass safeguards.

## Tooling landscape

**Categories.** AI Guardrails / AI Firewall (GenAI runtime defense); AI-SPM; AI Red Teaming (AEV)

**Untrusted-content scanning & isolation**

- Meta LlamaFirewall (Prompt Guard 2 on retrieved content) — https://github.com/meta-llama/PurpleLlama
- Palo Alto Networks LLM Guard (Protect AI) (input scanners) — https://github.com/protectai/llm-guard
- NVIDIA NeMo Guardrails (flows isolating untrusted context) — https://github.com/NVIDIA/NeMo-Guardrails
- Cisco AI Defense MCP Scanner (injected tool/resource content) — https://github.com/cisco-ai-defense/mcp-scanner
Validation:
- Microsoft PyRIT (indirect-injection (XPIA) attack modules) — https://github.com/Azure/PyRIT
