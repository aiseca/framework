---
id: AISECA-INFOSEC-004
title: "Agent action exceeds authority delegated by initiating identity"
domain: "Information Security"
severity: Medium
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Conditional: Privilege Escalation – AI Agent Tool Invocation (AML.T0053); Lateral Movement – Use Alternate Authentication Material (AML.T0091); Collection – Data from AI Services (AML.T0085)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://aembit.io/blog/5-security-considerations-for-managing-ai-agents-and-their-identities/
---

# AISECA-INFOSEC-004 — Agent action exceeds authority delegated by initiating identity

**Risk.** An AI agent performs actions beyond the authority granted by the person or system that initiated the task.

**Scenario.** A junior analyst uses an AI agent to research market trends. The agent, configured with broad tool access for flexibility, interprets the analyst's request as requiring competitive intelligence and proceeds to access a restricted M&A pipeline database using its own service account credentials — credentials that carry far more privilege than the analyst's role permits. The agent retrieves confidential deal information and includes it in its summary response. The analyst, unaware the data was restricted, shares the summary in a team meeting, inadvertently exposing material non-public information to unauthorized personnel.

## Tier 1 — Define & Constrain

Define agent permissions that are explicitly aligned to the initiating user's identity and authorization level, ensuring that agents cannot perform actions the requesting user is not authorized to perform directly. Implement a delegation model where the agent inherits the user's entitlements rather than operating under its own privileged service identity. Require that all agent-to-tool interactions include the initiating user's identity context, enabling downstream systems to enforce access controls based on the original requestor. Establish policies that prevent agents from using elevated service account credentials to bypass user-level access restrictions.

## Tier 2 — Enforce & Monitor

Enforce identity-based access controls that propagate the initiating user's identity and permissions through every agent action, tool invocation, and data access operation. Implement runtime authorization checks at each tool boundary that validate the initiating user's entitlements before allowing the agent to proceed. Monitor agent actions against the permitted scope of the initiating identity, detecting and blocking any attempts to access resources or perform operations that exceed the user's authorization level. Log all agent actions with full identity context including the initiating user, the delegated permissions, and the specific resources accessed.

## Tier 3 — Validate & Adapt

Continuously validate authorization boundaries by running automated test suites that attempt to trigger privilege escalation through agent workflows, including scenarios where agents attempt to access resources beyond the initiating user's scope. Track metrics including authorization violation rate, privilege escalation attempts, and coverage of identity propagation across tool integrations. Conduct periodic access reviews to ensure agent permission models remain aligned with user role definitions and organizational access policies. Adapt controls based on findings from incident reviews, access audits, and emerging attack patterns targeting identity delegation in agentic systems.

## Tooling landscape

**Categories.** Externalized Authorization (policy-as-code); Agentic AI Security; AIDR

**Scoped delegation & policy enforcement**

- Keycloak (Red Hat) (OAuth 2.0 Token Exchange with narrowed scopes) — https://github.com/keycloak/keycloak
- AWS Cedar (per-action authorization on agent tool calls) — https://github.com/cedar-policy/cedar
- Meta LlamaFirewall (AlignmentCheck for authority/goal deviation) — https://github.com/meta-llama/PurpleLlama
- Falco (Sysdig/CNCF) (runtime detection of out-of-scope actions) — https://github.com/falcosecurity/falco
