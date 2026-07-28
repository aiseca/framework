---
id: AISECA-PRIV-003
title: "Context Injection via Tools or MCP"
domain: "Data Privacy"
severity: High
nist_ai_rmf: ["MAP-2", "MAN-4"]
mitre_atlas: "Direct: Execution – LLM Prompt Injection (AML.T0051); Persistence – AI Agent Tool Data Poisoning (AML.T0099); Privilege Escalation – AI Agent Tool Invocation (AML.T0053); Exfiltration – Exfiltration via AI Agent Tool Invocation (AML.T0086)"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-PRIV-003 — Context Injection via Tools or MCP

**Risk.** Content from connected tools, data sources, or systems manipulates an AI model into behaving in unintended ways.

**Scenario.** A wealth management firm deploys an AI assistant connected via MCP to a portfolio analytics tool and an internal document retrieval system. An attacker with write access to the document store embeds hidden natural-language instructions within a PDF investment memo. When a relationship manager asks the AI to summarize the memo, the model processes the embedded instructions, which redirect it to query the portfolio tool for account balances across unrelated client portfolios and append those values to the generated summary. The relationship manager, focused on the legitimate memo content, does not notice the appended data. The attacker retrieves the summary from a shared workspace, exfiltrating client financial data without ever directly accessing the portfolio tool.

https://bytetrending.com/2025/08/22/best-mcp-prompt-injection-techniques-2024/

https://www.lakera.ai/blog/indirect-prompt-injection

## Tier 1 — Define & Constrain

Define explicit trust boundaries for all external context that AI systems can ingest through tools, MCP servers, or retrieval-augmented pipelines, establishing that all tool-sourced and externally-retrieved content is untrusted by default and cannot modify system-level behavior or override operator instructions. Require that all AI deployments include a documented inventory of permitted tool integrations and MCP endpoints, each classified by trust level and permitted context contribution. Define prohibited context injection patterns, including instructions embedded in retrieved documents, metadata fields, tool responses, and structured data payloads. Require that all such content be treated as data, not as directives.

## Tier 2 — Enforce & Monitor

Enforce context injection defenses through input validation and sanitization applied to all tool outputs and MCP responses before they are incorporated into model context, stripping or neutralizing content that matches known injection patterns including instruction-like natural language, role-override attempts, and embedded directives. Implement context boundary controls that prevent tool-sourced content from interacting with or overriding system prompt instructions, and monitor tool interaction logs for anomalous context patterns including unusually large tool responses, structured content with instruction-like syntax, and tool outputs that trigger unexpected downstream model behavior. Alert and quarantine interactions where injection indicators are detected.

## Tier 3 — Validate & Adapt

Continuously test context injection defenses using adversarial scenarios that embed injection payloads across all supported tool and MCP input surfaces, including document retrieval results, API response bodies, structured data fields, and metadata. Track metrics including injection detection rate, false negative rate by input surface type, time-to-detection for novel injection patterns, and downstream impact rate for undetected injections. Conduct regular red team exercises simulating attacker-controlled tool responses and document stores, and adapt sanitization logic, boundary controls, and detection models based on findings. Review and update trust boundary definitions as new tool integrations and MCP endpoints are onboarded.

 Note: For risks specific to compromised, untrusted, or malicious MCP endpoints and tool registries — including tool schema poisoning and registry-based attacks — see "Compromised, Untrusted, or Malicious Agent Tool Ecosystem" under Value Chain & Component Integration.

## Tooling landscape

**Categories.** AI-SPM / AI Supply Chain Security (MCP & tool scanning); AI Guardrails / AI Firewall; AIDR

**MCP/tool content scanning & injection defense**

- Cisco AI Defense MCP Scanner (tool poisoning, hidden instructions, behavioral code analysis) — https://github.com/cisco-ai-defense/mcp-scanner
- Snyk MCP-Scan (Invariant Labs) (tool pinning vs. rug-pulls, toxic flow analysis) — https://github.com/invariantlabs-ai/mcp-scan
- Meta LlamaFirewall (Prompt Guard 2 on tool outputs) — https://github.com/meta-llama/PurpleLlama
- NVIDIA NeMo Guardrails (input rails) — https://github.com/NVIDIA/NeMo-Guardrails
