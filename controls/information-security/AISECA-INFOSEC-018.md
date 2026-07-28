---
id: AISECA-INFOSEC-018
title: "Abuse of Legitimate Agency"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Execution / Privilege Escalation – AI Agent Tool Invocation (AML.T0053); Conditional: Exfiltration – Exfiltration via AI Agent Tool Invocation (AML.T0086); Impact – External Harms (AML.T0048)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://bytetrending.com/2025/08/22/best-mcp-prompt-injection-techniques-2024/
---

# AISECA-INFOSEC-018 — Abuse of Legitimate Agency

**Risk.** AI agents use legitimately assigned tools or permissions to perform unintended, unauthorized, or harmful actions.

**Scenario.** An AI agent misuses legitimate permissions to perform unintended or harmful actions.

## Tier 1 — Define & Constrain

Define intent-aware authorization requirements that distinguish between an agent using legitimate permissions for their intended purpose versus using those same permissions to execute attacker-directed objectives. Require that all agent deployments document the intended use cases for each granted permission, and establish policies constraining agent actions to those use cases even when underlying permissions technically permit broader access.

## Tier 2 — Enforce & Monitor

Enforce intent-based access controls through behavioral monitoring that detects agent use of legitimate permissions in patterns inconsistent with defined operational purpose — including accessing resources not required by the current task, data volumes disproportionate to task scope, and sequences of authorized actions that collectively constitute unauthorized exfiltration.

## Tier 3 — Validate & Adapt

Continuously test for abuse of legitimate agency using adversarial scenarios that inject attacker objectives into agent workflows via trusted input channels, including repository content, retrieved documents, and API responses. Track metrics including out-of-scope use of authorized permissions, task-purpose alignment rate, and detection rate for legitimate-agency exploitation patterns. Adapt behavioral baselines based on findings.

## Tooling landscape

**Categories.** Agentic AI Security / AI Agent Governance; Externalized Authorization; AIDR

- AWS Cedar (per-action authorization with human-approval policies) — https://github.com/cedar-policy/cedar
- Microsoft AutoGen (human-in-the-loop gates for high-impact actions) — https://github.com/microsoft/autogen
- Meta LlamaFirewall (AlignmentCheck goal-hijack detection) — https://github.com/meta-llama/PurpleLlama
- Falco (Sysdig/CNCF) — https://github.com/falcosecurity/falco
- OpenTelemetry (CNCF) (audit trails for post-hoc review) — https://opentelemetry.io
