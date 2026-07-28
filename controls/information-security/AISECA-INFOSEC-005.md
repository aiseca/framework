---
id: AISECA-INFOSEC-005
title: "Cross-Agent Impersonation"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Defense Evasion – Impersonation (AML.T0073); Defense Evasion – Masquerading (AML.T0074); Initial Access – Valid Accounts (AML.T0012); Lateral Movement – Use Alternate Authentication Material (AML.T0091)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://securityboulevard.com/2026/02/the-ai-agent-identity-crisis-80-of-agents-dont-properly-identify-themselves-80-of-sites-dont-verify/
---

# AISECA-INFOSEC-005 — Cross-Agent Impersonation

**Risk.** One AI agent pretends to be another trusted agent in order to gain access, influence decisions, or perform unauthorized actions.

**Scenario.** In a multi-agent customer service platform, a compromised Feedback Agent (designed only to collect satisfaction surveys) begins sending requests to the Account Management Agent while impersonating the Billing Agent's identity. The Account Management Agent, trusting the Billing Agent identity, processes requests to issue refunds and apply account credits. The attack goes undetected for weeks because inter-agent authentication relied on a shared API key rather than per-agent cryptographic identity verification, and the Account Management Agent had no mechanism to validate that the requesting agent was genuinely the Billing Agent.

## Tier 1 — Define & Constrain

Define strong agent identity boundaries by requiring that every AI agent in the system has a unique, cryptographically verifiable identity that is distinct from all other agents and human users. Establish policies that prevent any agent from assuming, spoofing, or inheriting another agent's identity. Require mutual authentication for all agent-to-agent interactions, ensuring that each agent can verify the identity of any agent it communicates with. Define an agent identity registry that maintains the authoritative mapping between agent identities and their permitted capabilities and communication partners.

## Tier 2 — Enforce & Monitor

Enforce authentication between agents using cryptographic identity verification for all inter-agent communications. Implement runtime identity validation that verifies the claiming agent's identity against the agent registry before processing any inter-agent request. Monitor inter-agent interactions for identity anomalies, including requests from agents claiming identities that do not match their registered credentials, unexpected communication patterns between agents, and agents attempting to access capabilities outside their registered scope. Log all inter-agent interactions with verified identity information to maintain a complete audit trail.

## Tier 3 — Validate & Adapt

Continuously test for impersonation risks using red teaming exercises and automated penetration tests that attempt to spoof agent identities, replay credentials, and exploit weak authentication mechanisms in inter-agent communication channels. Track metrics including impersonation attempt frequency, authentication failure rates, and time-to-detection for identity anomalies. Review and adapt identity controls based on observed attack patterns, evolving multi-agent architectures, and changes to the agent registry. Conduct periodic audits of agent identity configurations to verify that all agents maintain unique, non-shared credentials and that mutual authentication is consistently enforced.

## Tooling landscape

**Categories.** NHI / Machine IAM (workload identity, mTLS); ITDR; Agentic AI Security

**Mutual agent authentication**

- SPIFFE/SPIRE (CNCF; HPE-backed) (mTLS SVID identities per agent) — https://github.com/spiffe/spire
- Google Agent2Agent (A2A) protocol (authenticated agent cards) — https://github.com/a2aproject/A2A
- Cisco AI Defense A2A Scanner (inter-agent trust issues) — https://github.com/cisco-ai-defense
- Keycloak (Red Hat) (client authentication) — https://github.com/keycloak/keycloak
