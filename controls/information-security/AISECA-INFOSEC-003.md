---
id: AISECA-INFOSEC-003
title: "Over-privileged AI identities"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Conditional: Privilege Escalation – Valid Accounts (AML.T0012); Privilege Escalation – AI Agent Tool Invocation (AML.T0053); Collection – Data from AI Services (AML.T0085); Exfiltration – Exfiltration via AI Agent Tool Invocation (AML.T0086)"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-INFOSEC-003 — Over-privileged AI identities

**Risk.** An AI system has more permissions or access than it requires to perform its intended function.

**Scenario.** A financial institution provisions an AI coding assistant for its software engineering teams, assigning it a service account with read access to the entire internal code repository and write access to development and staging environments to support automated testing workflows. The permissions are configured broadly for convenience and never scoped down as the assistant is rolled out to additional teams. An attacker exploits a prompt injection vulnerability in a developer's workflow to coerce the assistant into exfiltrating large volumes of IP source code, such as proprietary trading logic and internal API credentials embedded in configuration files, using the assistant's legitimate, over-privileged service account. The exfiltration goes undetected for weeks because the access pattern is indistinguishable from the assistant's normal, unrestricted behavior.


https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls

https://www.reco.ai/blog/ai-and-cloud-security-breaches-2025

## Tier 1 — Define & Constrain

Define least-privilege requirements for all AI system identities — including service accounts, API credentials, agent identities, and integration tokens — specifying that each AI deployment is provisioned with only the permissions required to perform its defined functions, with no standing access to data or systems outside its operational scope. Require that all AI identity provisioning requests include a documented justification mapping each requested permission to a specific functional requirement, reviewed and approved by the responsible security and system ownership functions. Establish a privilege tier classification for AI identities that reflects the sensitivity of accessible data, the reversibility of permitted actions, and the breadth of system access, with escalating oversight and review requirements for higher-privilege tiers.

## Tier 2 — Enforce & Monitor

Enforce least-privilege controls through automated provisioning workflows that apply scoped permission sets to AI identities based on approved role definitions, and through periodic access reviews that validate provisioned permissions remain aligned with current functional requirements. Implement runtime monitoring of AI identity activity that detects access patterns inconsistent with defined operational scope, including access to data categories not required by the AI's function, unusual query volumes, and access to systems outside the AI's registered integration set. Alert and automatically suspend AI identities exhibiting anomalous access behavior, and require re-authorization for any permission expansion beyond the approved baseline.

## Tier 3 — Validate & Adapt

Continuously validate AI identity permission boundaries by running automated access review tests that check provisioned permissions against current functional scope definitions, and by conducting adversarial exercises that attempt to exploit over-privileged identities through prompt injection, context manipulation, and tool misuse. Track metrics including over-provisioning rate at initial deployment, permission drift rate over time, anomalous access detection rate, and mean time to detect and contain unauthorized access via AI identity. Conduct periodic red team exercises simulating attacker exploitation of AI service accounts, and adapt provisioning controls, monitoring thresholds, and access review cadences based on findings and emerging attack patterns.

## Tooling landscape

**Categories.** CIEM; IGA; NHI (least privilege)

**Least-privilege analysis & right-sizing**

- Netflix Repokid (auto-removal of unused IAM permissions) — https://github.com/Netflix/repokid
- Netflix ConsoleMe — https://github.com/Netflix/consoleme
- Salesforce Policy Sentry (least-privilege policy authoring) — https://github.com/salesforce/policy_sentry
- Salesforce Cloudsplaining (IAM risk assessment) — https://github.com/salesforce/cloudsplaining
- AWS Cedar (fine-grained authorization) — https://github.com/cedar-policy/cedar
