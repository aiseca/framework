---
id: AISECA-PRIV-002
title: "Sensitive data retention"
domain: "Data Privacy"
severity: High
nist_ai_rmf: ["MAP-2", "MAN-4"]
mitre_atlas: "Conditional: Collection – Data from AI Services (AML.T0085); Exfiltration – LLM Data Leakage (AML.T0057)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://mashable.com/article/samsung-chatgpt-leak-details
---

# AISECA-PRIV-002 — Sensitive data retention

**Risk.** Sensitive information remains stored, accessible, or recoverable longer than intended.

**Scenario.** An HR employee drafts termination letters containing SSNs and salary data. The context persists in logs which resurfaces when they are ingested by a centralized logging tool like Splunk which are indexed & searchable by any engineer with access.

## Tier 1 — Define & Constrain

Establish foundational policy that limits sensitive data exposure in unapproved AI systems. Include data handling policy that defines specific classifications (PII, PHI, Regulated Data, etc.) that are prohibited or restricts in AI prompts with clear guidance on approved alternatives (e.g. redaction). Configure AI service settings to observe retention policies, where available.

## Tier 2 — Enforce & Monitor

Translate policy into technical enforcement through data loss prevention, input sanitization/redaction, or other gates to regulate sensitive data exposure to unapproved AI services. Consolidate AI input, output, logging, and other telemetry into centralized logging or observability tools. Analyze ingested content for sensitive data classifications with thresholds that trigger escalation.

## Tier 3 — Validate & Adapt

Continuously test controls with sampling of production output at each gate to validate automated and human reviewers are catching sensitive data exfiltration. Periodically red-team control pipelines to ensure controls hold under realistic and evolving practices. Continuously adjust controls as regulation evolves.

## Tooling landscape

**Categories.** DSPM; Data Governance / retention management (ILM)

**Data discovery & lifecycle enforcement**

- Microsoft Presidio (find/redact stored PII in transcripts & logs) — https://github.com/microsoft/presidio
- OpenSearch Index State Management (AWS) (retention policies on conversation/log stores) — https://opensearch.org/docs/latest/im-plugin/ism/index/
- Elastic ILM — https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html
- DataHub (LinkedIn-originated) (retention & lineage metadata) — https://github.com/datahub-project/datahub
