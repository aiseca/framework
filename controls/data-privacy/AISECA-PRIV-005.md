---
id: AISECA-PRIV-005
title: "Unauthorized training data use"
domain: "Data Privacy"
severity: High
nist_ai_rmf: ["MAP-2", "MAN-4"]
mitre_atlas: "No Direct Mapping"
stakeholders: ["Leadership"]
references: []
---

# AISECA-PRIV-005 — Unauthorized training data use

**Risk.** AI is trained using data without appropriate authorization, consent, or legal rights.

**Scenario.** A corporation trains an internal AI assistant on unfiltered HR records — including employee names, salaries, performance ratings, and medical leave history. When a manager later prompts the tool to suggest performance review language for employees who take frequent leave, the model surfaces details closely mirroring a specific employee's mental health history. The company now faces discrimination claims, HIPAA and ADA violations, and cannot simply delete the data — as it is embedded in the model's weights and would require a full, costly retraining to remediate.

## Tier 1 — Define & Constrain

Define a formal data classification schema that assigns sensitivity levels to all organizational data, explicitly designating the most restricted categories as off-limits for AI ingestion, and document this in a written AI acceptable use policy that covers both internal systems and third-party vendors with embedded AI features. Constrain access by enforcing role-based controls so AI systems cannot reach protected datastores, physically or logically segregating sensitive datasets from shared data lakes and AI pipelines, requiring vendor contracts to prohibit model training on your data, and mandating approved anonymization standards before any internal data can be considered for AI use.

## Tier 2 — Enforce & Monitor

Enforce protections by deploying automated ingestion gates that scan for classification tags and sensitive data patterns before any dataset enters a training or fine-tuning workflow, extending DLP policies to block restricted data from being input into AI tools or APIs, and requiring formal stakeholder sign-off before any internal dataset is approved for AI use. Monitor by enabling comprehensive audit logging on all AI data flows (capturing input source, user identity, and timestamp) and configuring anomaly detection on sensitive datastores to alert on bulk exports, unusual access patterns, or activity outside normal operational behavior.

## Tier 3 — Validate & Adapt

Validate by periodically auditing what data has actually been ingested into deployed models ncluding fine-tuned and retrieval-augmented systems and using targeted output probing to surface any memorized sensitive content, treating user-reported concerns as an additional validation signal. Adapt by maintaining a documented machine unlearning procedure for affected models, keeping an incident response playbook ready for data contamination events, aligning controls with applicable regulations such as GDPR, CCPA, and the EU AI Act, and reinforcing all controls with ongoing employee education on data boundaries and reporting obligations.

## Tooling landscape

**Categories.** Data & Analytics Governance (catalog/lineage); AI Governance

**Data governance & lineage**

- DataHub (LinkedIn-originated) (dataset lineage, ownership & consent metadata) — https://github.com/datahub-project/datahub
- Unity Catalog (Databricks) (access/usage governance) — https://github.com/unitycatalog/unitycatalog
- Google TensorFlow Data Validation (dataset intake checks) — https://github.com/tensorflow/data-validation
