---
id: AISECA-INFOSEC-001
title: "Loss of identity attribution"
domain: "Information Security"
severity: Medium
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Conditional: Defense Evasion – Impersonation (AML.T0073); Defense Evasion – Masquerading (AML.T0074); Initial Access – Valid Accounts (AML.T0012)"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-INFOSEC-001 — Loss of identity attribution

**Risk.** The identity responsible for an action, decision, or output can no longer be reliably determined.

**Scenario.** An organization deploys multiple AI agents built on a shared orchestration platform to handle customer intake, billing, and records retrieval. All three agents execute under a single shared service account. When an auditor investigates an unauthorized access to restricted patient records, logs show only the shared account — making it impossible to determine which agent, workflow, or upstream user trigger was responsible for the behavior.

## Tier 1 — Define & Constrain

Identify or define data classifications that require traceable identity access during operations or workflows. Define ownership, naming, and lifecycle standards for non-human identities. Publish identity and access policy requiring distinct agentic identities in these areas and prohibit the use of shared or generic service accounts. Provision unique identities (e.g. machine identities, individual service accounts) scoped to specific data classifications or operations.

## Tier 2 — Enforce & Monitor

Require AI actions, tool call, and data accesses be logged with agent identity, invoking user, session, and workflow context. Reject requests missing attribution information. Monitor for shared-credential use, prohibited accesses, and other anomolous patterns per agent. Trigger escalation when agents act outside their scoped permissions or when attribution gaps appear in logs.

## Tier 3 — Validate & Adapt

Audit sample transactions end-to-end. Conduct exercises to identify gaps in enforcement mechanisms. Review non-human identity inventories for orphaned, over-privileged, or unattributed accounts. Integrate lessons learned into IR playbooks, enterprise risk reporting, and readiness assessments.

## Tooling landscape

**Categories.** NHI / Machine IAM; ITDR; SIEM (audit logging)

**Workload identity & audit logging**

- SPIFFE/SPIRE (CNCF; HPE-backed) (per-agent cryptographic identities) — https://github.com/spiffe/spire
- Keycloak (Red Hat) (authentication & audit events) — https://github.com/keycloak/keycloak
- OpenTelemetry (CNCF) (actor/trace attribution) — https://opentelemetry.io
- OpenSearch (AWS) (audit-log pipelines) — https://opensearch.org
