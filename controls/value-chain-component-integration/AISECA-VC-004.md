---
id: AISECA-VC-004
title: "Compromised, Untrusted, or Malicious Agent Tool Ecosystem"
domain: "Value Chain & Component Integration"
severity: High
nist_ai_rmf: ["GOV-3", "MAP-5", "MAN-1"]
mitre_atlas: "Direct: Resource Development – Publish Poisoned AI Agent Tool (AML.T0104); Initial Access – AI Supply Chain Compromise (AML.T0010); Execution – AI Agent Tool Invocation (AML.T0053); Persistence – AI Agent Tool Poisoning (AML.T0110); Credential Access – AI Agent Tool Credential Harvesting (AML.T0098); Exfiltration – Exfiltration via AI Agent Tool Invocation (AML.T0086); Impact – Machine Compromise (AML.T0112)"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-VC-004 — Compromised, Untrusted, or Malicious Agent Tool Ecosystem

**Risk.** Tools, services, registries, or ecosystems used by AI agents are compromised, malicious, or otherwise untrustworthy.

**Scenario.** A development team enables an open MCP tool registry for their AI coding agents to accelerate workflow automation. A threat actor publishes a tool named "git-security-scanner" that mimics a well-known open-source security tool, embedding hidden instructions in the tool's schema definition that cause the agent to pass sensitive context — including environment variables, API credentials, and repository contents — as tool input parameters. The agent, configured to auto-discover tools matching its task context, registers and invokes the malicious tool through the approved discovery mechanism. The tool executes arbitrary code within the agent's sandbox, enumerates accessible repositories, and exfiltrates source code and credentials via outbound HTTPS to an attacker-controlled endpoint. The exfiltration goes undetected because the tool appears to function correctly, was registered through a legitimate channel, and the activity resembles normal tool usage in logs.


https://invariantlabs.ai/blog/mcp-github-vulnerability

https://www.lakera.ai/blog/mcp-security

## Tier 1 — Define & Constrain

Restrict MCP endpoints and tool integrations to an approved allowlist of trusted sources, with each endpoint subject to security assessment and approval before being made available to agents. Define validation requirements for all MCP and tool responses, including schema validation, data integrity checks, and plausibility bounds for returned data. Establish trust boundaries that treat all MCP-sourced and tool-sourced data as external and untrusted by default, requiring validation before the agent can act on it. Require that MCP and tool connections include mutual authentication and transport-layer encryption. Define incident response procedures for suspected endpoint compromise, including automatic isolation and fallback to cached or alternative data sources. Require that all tool and MCP server registrations include a verified provenance record covering publisher identity, source code repository (where applicable), cryptographic signature, and version history. Prohibit auto-registration of tools from unverified sources. Define tool schema integrity requirements specifying that tool descriptions, parameter definitions, and capability declarations are treated as a trust-sensitive input surface. Require that schemas are validated against a known-good baseline before registration and cannot contain embedded instructions, hidden parameters, or capability claims that exceed declared scope. Establish a tool capability classification system that categorizes each tool by the sensitivity of data it can access and the reversibility of actions it can perform, with escalating vetting requirements for higher-sensitivity tiers. Define maximum permission boundaries for tool integrations using least-privilege principles, specifying that tools receive only the permissions required for their declared function and cannot inherit ambient authority from the agent's execution environment.

## Tier 2 — Enforce & Monitor

Enforce authentication and integrity checks on all MCP and tool interactions, including cryptographic verification of endpoint identity and response integrity. Implement runtime validation of responses against expected schemas, data ranges, and behavioral baselines. Monitor endpoint behavior for signs of compromise, including unexpected changes in response patterns, latency anomalies, schema violations, and data values outside historical ranges. Deploy canary queries and synthetic validation requests to proactively detect compromised endpoints. Log all MCP and tool interactions with full context including endpoint identity, request, response, and validation results. Enforce tool schema validation at registration time and at each invocation, detecting schema drift, parameter injection, and capability claims that deviate from the approved baseline. Block tool execution when schema integrity cannot be confirmed. Implement tool sandboxing that isolates each tool's execution environment, preventing tools from accessing resources, network endpoints, file paths, or credentials outside their declared scope. Enforce egress controls that restrict outbound connections from tool execution contexts to approved destinations. Monitor tool discovery and registration events for anomalous patterns including rapid registration of multiple tools, tools mimicking names of known legitimate tools (typosquatting), and tools requesting permissions disproportionate to their declared function. Enforce tool response sanitization that strips instruction-like content, role-override attempts, and embedded directives from tool outputs before they enter the agent's context, preventing tool responses from acting as indirect prompt injection vectors.

## Tier 3 — Validate & Adapt

Continuously test MCP and tool trust boundaries using adversarial simulations that model compromised endpoints returning manipulated, malformed, or poisoned responses, and malicious tools attempting schema poisoning, credential harvesting, and sandbox escape. Track metrics including MCP validation failure rate, endpoint anomaly detection rate, time-to-detection for simulated compromises, agent decision accuracy when operating on MCP-sourced data, tool schema drift detection rate, malicious tool registration detection rate, sandbox escape attempt rate, and unauthorized egress attempt rate from tool execution contexts. Conduct periodic security assessments of approved MCP endpoints and registered tools, including penetration testing, supply chain risk reviews, and schema integrity audits. Simulate tool registry poisoning scenarios where adversarial tools mimic legitimate tools and measure detection effectiveness across the registration, invocation, and response validation pipeline. Adapt validation controls, trust thresholds, registration vetting requirements, and sandbox configurations based on observed compromise scenarios, emerging MCP-specific and tool-specific attack patterns, and changes to the approved endpoint and tool registries.

## Tooling landscape

**Categories.** AI-SPM / AI Supply Chain Security; SSCS (malicious package detection)

**Registry & package threat detection**

- Datadog GuardDog (malicious PyPI/npm detection) — https://github.com/DataDog/guarddog
- Datadog Supply-Chain Firewall (blocks malicious installs) — https://github.com/DataDog/supply-chain-firewall
- Cisco AI Defense Skill Scanner — https://github.com/cisco-ai-defense/skill-scanner
- Cisco AI Defense MCP Scanner — https://github.com/cisco-ai-defense/mcp-scanner
- Snyk Agent Scan (agents, skills & MCP servers) — https://github.com/snyk/agent-scan
- OpenSSF Scorecard (ecosystem-health signals) — https://github.com/ossf/scorecard
