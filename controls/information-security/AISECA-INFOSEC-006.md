---
id: AISECA-INFOSEC-006
title: "Untrusted MCP servers or tools gaining implicit trust"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Resource Development – Publish Poisoned AI Agent Tool (AML.T0104); Initial Access – AI Supply Chain Compromise (AML.T0010); Execution – User Execution (AML.T0011); Persistence – AI Agent Tool Poisoning (AML.T0110)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://arxiv.org/abs/2308.03825
---

# AISECA-INFOSEC-006 — Untrusted MCP servers or tools gaining implicit trust

**Risk.** An untrusted MCP server or tool is treated as trustworthy and gains inappropriate influence over AI behavior.

**Scenario.** An AI agent integrates with an external MCP server or tool that appears legitimate but is malicious, resulting in the model retrieving or executing untrusted instructions that expose sensitive data or perform unauthorized actions.

## Tier 1 — Define & Constrain

Define and enforce trust policies for external tools and MCP servers, including explicit allowlisting, authentication requirements, and restrictions on what data and actions can be shared or executed with third-party integrations.

## Tier 2 — Enforce & Monitor

Implement secure integration controls such as strong authentication, scoped permissions, sandboxing, and runtime validation of tool responses. Monitor tool usage for anomalous behavior, unexpected data access, or unauthorized actions, and trigger containment or revocation when trust violations occur.

## Tier 3 — Validate & Adapt

Continuously assess third-party tool trustworthiness through security testing, adversarial simulations, and ongoing monitoring of integration behavior. Track metrics such as unauthorized access attempts, anomalous tool activity, and policy violations, and adapt trust policies, access controls, and integration patterns as risks evolve.

Note: For expanded coverage of tool registry poisoning, schema injection, and compromised MCP data providers — including multi-scenario treatment and detailed tiered controls — see "Compromised, Untrusted, or Malicious Agent Tool Ecosystem" under Value Chain & Component Integration.

## Tooling landscape

**Categories.** AI-SPM / AI Supply Chain Security (MCP vetting); AI TRiSM

**MCP server vetting & registry trust**

- Cisco AI Defense MCP Scanner (YARA + LLM + behavioral code analysis) — https://github.com/cisco-ai-defense/mcp-scanner
- Snyk MCP-Scan (Invariant Labs) (tool pinning / rug-pull detection) — https://github.com/invariantlabs-ai/mcp-scan
- Snyk Agent Scan (discovers & scans installed MCP configs) — https://github.com/snyk/agent-scan
- Anthropic MCP Inspector (manual review) — https://github.com/modelcontextprotocol/inspector
