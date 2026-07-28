---
id: AISECA-HAIC-002
title: "Unsafe agent autonomy"
domain: "Human–AI Configuration & Overreliance"
severity: High
nist_ai_rmf: ["GOV-2", "MAP-4", "MAN-2"]
mitre_atlas: "Conditional: Privilege Escalation – AI Agent Tool Invocation (AML.T0053); Impact – Data Destruction via AI Agent Tool Invocation (AML.T0101); Impact – Machine Compromise (AML.T0112)"
stakeholders: ["Builder / Maintainer"]
references:
  - https://www.giskard.ai/knowledge/a-cursor-ai-agent-wiped-a-production-database-in-9-seconds-excessive-agency-ai-failure
---

# AISECA-HAIC-002 — Unsafe agent autonomy

**Risk.** An AI agent takes actions independently that could create harm because appropriate safeguards or oversight are missing.

**Scenario.** A financial services firm deploys an AI coding agent to automate infrastructure changes. The agent, given a task to optimize database performance, autonomously decides to modify production database configurations, drop unused indexes, and reschedule backup jobs — actions far beyond its intended scope. The changes cause a cascading failure during peak trading hours, and because the agent acted without any human checkpoint, the team only discovers the root cause hours later during incident response.

## Tier 1 — Define & Constrain

Define clear autonomy boundaries for all AI agents, specifying which actions agents can take independently versus those requiring explicit human approval. Establish a classification system for agent actions based on impact and reversibility (e.g., read-only, low-impact write, high-impact write, irreversible), and map each classification to an appropriate level of human oversight. Require that all agent deployments include a documented scope of permitted autonomous behavior, approved by the responsible business owner, with explicit restrictions on actions that modify production state, access sensitive data, or interact with external systems.

## Tier 2 — Enforce & Monitor

Enforce autonomy boundaries through runtime controls that restrict agent actions to their permitted scope, including configurable approval gates for high-impact or irreversible operations. Implement scoped execution environments that sandbox agent capabilities based on their defined autonomy level. Monitor agent behavior in real time to detect actions that approach or exceed defined boundaries, logging all autonomous decisions with full context including intent, tools invoked, data accessed, and outcome. Trigger alerts and automatic suspension when agents attempt actions outside their permitted scope.

## Tier 3 — Validate & Adapt

Continuously test autonomy boundaries using adversarial scenarios and red teaming exercises that attempt to coerce agents into exceeding their permitted scope. Track metrics including autonomy boundary violation rate, human override frequency, and time-to-detection for scope exceedances. Regularly review and adapt autonomy boundaries based on operational experience, emerging threat patterns, and changes in business requirements. Validate that approval gates function correctly under load and edge conditions, and refine agent behavior policies based on observed decision patterns and incident post-mortems.

## Tooling landscape

**Categories.** Agentic AI Security / AI Agent Governance; AIDR; CWPP (sandboxing)

**Agent guardrails, sandboxing & human-in-the-loop**

- Meta LlamaFirewall (AlignmentCheck goal-deviation detection) — https://github.com/meta-llama/PurpleLlama
- Microsoft AutoGen (human-approval & termination controls) — https://github.com/microsoft/autogen
- NVIDIA NeMo Guardrails (action rails) — https://github.com/NVIDIA/NeMo-Guardrails
- Google gVisor — https://github.com/google/gvisor
- AWS Firecracker — https://github.com/firecracker-microvm/firecracker
- Falco (Sysdig/CNCF) (runtime detection) — https://github.com/falcosecurity/falco
