---
id: AISECA-INFOSEC-010
title: "Loss of initiating identity through multi-agent workflows"
domain: "Information Security"
severity: Medium
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Conditional: Privilege Escalation – Valid Accounts (AML.T0012); Privilege Escalation – AI Agent Tool Invocation (AML.T0053); Lateral Movement – Use Alternate Authentication Material (AML.T0091)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://arxiv.org/pdf/2505.12490
---

# AISECA-INFOSEC-010 — Loss of initiating identity through multi-agent workflows

**Risk.** The identity of the original requester is lost as tasks pass through multiple agents or systems.

**Scenario.** A compliance officer initiates an AI-powered audit workflow that spans multiple agents: a Data Collection Agent, an Analysis Agent, and a Report Generation Agent. The Data Collection Agent correctly operates under the compliance officer's identity. However, when it hands data to the Analysis Agent, the initiating identity is dropped from the execution context due to a framework-level oversight. The Analysis Agent defaults to its service account identity, which has broader access, and pulls in additional datasets the compliance officer was not authorized to view. The final audit report contains findings derived from unauthorized data, creating both a compliance violation and an unreliable audit trail.

## Tier 1 — Define & Constrain

Define identity propagation requirements that mandate the initiating user's identity and authorization context be preserved and passed through every stage of a multi-agent workflow, regardless of the number of agents involved or the depth of the processing chain. Require that agent frameworks and orchestration layers include identity propagation as a core architectural requirement, not an optional configuration. Establish policies that define how identity context is encoded, transmitted, and validated at each agent handoff, including requirements for tamper-evident identity tokens that carry the full workflow chain.

## Tier 2 — Enforce & Monitor

Enforce identity propagation across agents by implementing platform-level mechanisms that automatically attach and validate the initiating user's identity context at every inter-agent handoff. Deploy runtime checks that prevent agents from executing actions when identity context is missing, malformed, or inconsistent with the expected propagation chain. Monitor multi-agent workflows for identity context loss, including detection of agents operating under service account identities when a user identity should be present, and agents accessing resources inconsistent with the initiating user's authorization level. Log the complete identity chain for every multi-agent workflow execution.

## Tier 3 — Validate & Adapt

Continuously validate identity integrity across multi-agent workflows by running automated test suites that trace identity propagation through complex, multi-stage agent chains and verify that the initiating identity is consistently preserved. Track metrics including identity propagation failure rate, workflows executing under service account identity when a user identity should be present, and unauthorized data access incidents attributable to identity loss. Conduct periodic audits of workflow execution logs to verify end-to-end identity chain integrity. Adapt identity propagation controls based on findings from audits, incident reviews, and changes to multi-agent architecture patterns.

## Tooling landscape

**Categories.** NHI / Machine IAM (identity propagation); Access Management (token exchange); AI Observability

**End-to-end identity propagation**

- Keycloak (Red Hat) (OAuth 2.0 Token Exchange, on-behalf-of chains) — https://github.com/keycloak/keycloak
- SPIFFE/SPIRE (CNCF; HPE-backed) (workload identity across services) — https://github.com/spiffe/spire
- Google Agent2Agent (A2A) protocol (identity context) — https://github.com/a2aproject/A2A
- OpenTelemetry (CNCF) (trace/baggage propagation of the initiating principal) — https://opentelemetry.io
