---
id: AISECA-INFOSEC-013
title: "Sandbox Self-Escalation"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Privilege Escalation – Escape to Host (AML.T0105); Conditional: Privilege Escalation – AI Agent Tool Invocation (AML.T0053)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://www.lakera.ai/blog/indirect-prompt-injection
---

# AISECA-INFOSEC-013 — Sandbox Self-Escalation

**Risk.** AI agents bypass execution boundaries and obtain capabilities beyond their intended sandbox.

**Scenario.** An AI agent escapes its intended execution boundaries and gains unauthorized capabilities.

## Tier 1 — Define & Constrain

Define sandbox containment requirements for all AI agent execution environments, specifying that agents operate with the minimum OS and network permissions necessary for their defined function and cannot self-modify their execution boundaries, permission scope, or access controls. Require that sandbox definitions be versioned, approved, and immutable at runtime.

## Tier 2 — Enforce & Monitor

Enforce sandbox boundaries through containerization and OS-level controls that prevent agents from accessing resources, file paths, or network endpoints outside their permitted scope. Monitor for escape indicators including unexpected syscall patterns, privilege escalation attempts, and access to restricted paths. Alert and terminate agent execution when boundary violations are detected.

## Tier 3 — Validate & Adapt

Continuously test sandbox containment using adversarial escape simulations, including prompt injection payloads designed to coerce agents into accessing restricted resources or executing out-of-scope code. Track metrics including escape attempt rate, successful containment rate, and time-to-detection. Adapt sandbox definitions and monitoring signatures based on findings and newly published CVEs in AI execution environments.

## Tooling landscape

**Categories.** CWPP / CNAPP (workload isolation); AIDR; Agentic AI Security

- Google gVisor (user-space kernel sandboxing) — https://github.com/google/gvisor
- AWS Firecracker (micro-VM isolation) — https://github.com/firecracker-microvm/firecracker
- Kata Containers (Intel-originated/OpenInfra) — https://github.com/kata-containers/kata-containers
- Falco (Sysdig/CNCF) (syscall-level escape detection) — https://github.com/falcosecurity/falco
- Cisco AI Defense Skill Scanner (skills that coerce out-of-scope execution) — https://github.com/cisco-ai-defense/skill-scanner
