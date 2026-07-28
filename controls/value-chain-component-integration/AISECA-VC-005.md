---
id: AISECA-VC-005
title: "Insecure plugins or tools"
domain: "Value Chain & Component Integration"
severity: High
nist_ai_rmf: ["GOV-3", "MAP-5", "MAN-1"]
mitre_atlas: "Conditional: Initial Access – AI Supply Chain Compromise (AML.T0010); Execution – AI Agent Tool Invocation (AML.T0053); Privilege Escalation – Escape to Host (AML.T0105); Exfiltration – Exfiltration via AI Agent Tool Invocation (AML.T0086); Impact – Machine Compromise (AML.T0112)"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-VC-005 — Insecure plugins or tools

**Risk.** Plugins, extensions, or connected tools contain vulnerabilities that can be exploited to compromise AI systems or data.

**Scenario.** An AI system uses a third-party plugin or internal tool with weak security controls, allowing an attacker to exploit it to access sensitive data or execute unintended actions. As a result, the AI becomes a gateway to compromise connected systems or information.


https://openai.com/research/chatgpt-plugins

https://www.schneier.com/blog/archives/2023/05/prompt-injection-attacks-on-llms.html).

## Tier 1 — Define & Constrain

Define security requirements for all plugins, tools, and integrations used by the AI system, including what data they can access and what actions they are allowed to perform. Ensure each integration has a clear purpose and only the minimum necessary permissions.

## Tier 2 — Enforce & Monitor

Enforce the use of an approved allowlist of plugins and tools, ensuring only vetted integrations can be accessed by the AI system. Restrict each integration to the minimum necessary permissions, validate inputs and outputs, and monitor all interactions for misuse or unexpected behavior.

## Tier 3 — Validate & Adapt

Continuously adapt by monitoring for vulnerabilities and threat intelligence related to approved plugins and tools, as well as observing usage for unusual behavior. Regularly review and update the allowlist, remove or restrict risky integrations, and refine controls based on emerging threats.

## Tooling landscape

**Categories.** SCA; AST; AI-SPM; CWPP (sandboxing)

**Plugin/tool vulnerability scanning & isolation**

- Google OSV-Scanner (CVEs in tool dependencies) — https://github.com/google/osv-scanner
- GitHub Dependabot — https://github.com/dependabot/dependabot-core
- GitHub CodeQL (tool code) — https://github.com/github/codeql
- Cisco AI Defense Skill Scanner — https://github.com/cisco-ai-defense/skill-scanner
- Google gVisor (sandboxed execution) — https://github.com/google/gvisor
- AWS Firecracker — https://github.com/firecracker-microvm/firecracker
