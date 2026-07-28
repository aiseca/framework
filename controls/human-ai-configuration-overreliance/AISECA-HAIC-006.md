---
id: AISECA-HAIC-006
title: "Uncontrolled Agent Delegation Chains"
domain: "Human–AI Configuration & Overreliance"
severity: Medium
nist_ai_rmf: ["GOV-2", "MAP-4", "MAN-2"]
mitre_atlas: "Conditional: Privilege Escalation – AI Agent Tool Invocation (AML.T0053); Lateral Movement – Use Alternate Authentication Material (AML.T0091); Collection – Data from AI Services (AML.T0085)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://cloudsecurityalliance.org/blog/2026/03/25/control-the-chain-secure-the-system-fixing-ai-agent-delegation
---

# AISECA-HAIC-006 — Uncontrolled Agent Delegation Chains

**Risk.** An AI agent delegates tasks to other agents or systems in ways that become difficult to control or oversee.

**Scenario.** An enterprise deploys a multi-agent system where a Manager Agent delegates tasks to specialized sub-agents. A user asks the Manager Agent to compile a quarterly business review. The Manager Agent delegates data gathering to an Analytics Agent, which delegates sub-queries to a Database Agent, which delegates specific computations to a Code Execution Agent. The Code Execution Agent, now four levels deep in the delegation chain, executes a query that accesses sensitive HR compensation data — data the original user was never authorized to see. No single agent in the chain validated whether the delegation was appropriate, and the initiating user's access permissions were never propagated through the chain.

## Tier 1 — Define & Constrain

Define explicit limits on agent delegation depth and breadth, restricting the number of levels an agent-to-agent delegation chain can reach and the total number of agents that can be invoked in a single workflow. Require that all delegation events include propagation of the initiating user's identity and authorization context, ensuring that no delegated agent can exceed the permissions of the original requestor. Establish an approved registry of agent-to-agent delegation paths, specifying which agents are permitted to delegate to which other agents and under what conditions.

## Tier 2 — Enforce & Monitor

Enforce delegation controls through runtime mechanisms that validate each delegation event against the approved registry, checking delegation depth, target agent authorization, and propagation of the initiating identity. Implement delegation chain tracking that maintains a complete record of the full chain from initiating user through every delegated agent, with each link recording the delegating agent, the delegated agent, the task description, and the permissions passed. Monitor for delegation anomalies including excessive chain depth, circular delegation, delegation to unregistered agents, and permission escalation across delegation boundaries. Trigger alerts and automatic chain termination when violations are detected.

## Tier 3 — Validate & Adapt

Continuously test delegation boundaries using adversarial scenarios designed to exploit multi-agent delegation, including attempts to bypass permission propagation, create circular delegation loops, and escalate privileges through deep chains. Track metrics including average and maximum delegation depth, delegation chain failure rate, permission escalation incidents, and circular delegation detections. Review and adapt delegation policies based on operational experience, emerging multi-agent attack patterns, and changes to the agent registry. Conduct periodic audits of delegation logs to verify that identity and authorization context is consistently preserved across all delegation events.

## Tooling landscape

**Categories.** Agentic AI Security; NHI / Machine IAM; AI Observability (distributed tracing)

**Delegation control & cross-agent tracing**

- Google Agent2Agent (A2A) protocol (authenticated, auditable agent-to-agent exchange) — https://github.com/a2aproject/A2A
- Cisco AI Defense A2A Scanner — https://github.com/cisco-ai-defense
- OpenTelemetry (CNCF) (distributed tracing across agent hops) — https://opentelemetry.io
- AWS Cedar (policies limiting delegable scopes) — https://github.com/cedar-policy/cedar
