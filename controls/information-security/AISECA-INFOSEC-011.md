---
id: AISECA-INFOSEC-011
title: "Training data poisoning"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Resource Development – Poison Training Data (AML.T0020); AI Attack Staging – Manipulate AI Model (AML.T0018); Impact – Erode Dataset Integrity (AML.T0059); Impact – Erode AI Model Integrity (AML.T0031)"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-INFOSEC-011 — Training data poisoning

**Risk.** Malicious, misleading, or manipulated data is introduced to influence how an AI model behaves.

**Scenario.** A financial services firm fine-tunes a general-purpose LLM on internal compliance documentation, past audit findings, and regulatory guidance to create a compliance advisory assistant. An insider with access to the fine-tuning data pipeline introduces subtly modified versions of regulatory documents that consistently understate capital reserve thresholds and mischaracterize reporting obligations for a specific asset class. The poisoned training data causes the model to systematically provide incorrect compliance guidance on these topics. Business units relying on the assistant's recommendations fail to meet actual regulatory requirements, and the breach is only identified during an external regulatory examination.

https://layerxsecurity.com/generative-ai/data-poisoning/

https://www.anthropic.com/research/small-samples-poison

## Tier 1 — Define & Constrain

Define trusted data source requirements for all AI training and fine-tuning pipelines, specifying approved data sources, required provenance documentation, and chain-of-custody controls that ensure training data integrity from ingestion through model deployment. Establish access controls and approval workflows for training data pipelines that restrict who can contribute, modify, or approve data for inclusion in model training, with elevated controls on internally-contributed data and content sourced from external or third-party repositories. Require that all training datasets include a documented data lineage record covering source, collection methodology, preprocessing steps, and known quality or bias concerns, reviewed and approved by the responsible AI governance function prior to use in training.

## Tier 2 — Enforce & Monitor

Enforce training data integrity through automated anomaly detection applied to datasets prior to model training, including statistical analysis for distributional drift, duplicate and near-duplicate detection for targeted document substitution, and consistency checks that flag documents contradicting established ground-truth references. Implement version-controlled data pipelines with tamper-evident logging that records all contributions, modifications, and approvals, enabling full provenance reconstruction for any trained model. Monitor model outputs post-deployment for behavioral drift that may indicate poisoning effects, including systematic inaccuracy on specific topics, inconsistency with authoritative reference sources, and statistically anomalous confidence patterns on targeted subject matter.

## Tier 3 — Validate & Adapt

Continuously test training pipeline integrity using adversarial data injection simulations that introduce poisoned samples at various pipeline stages and measure detection rates across anomaly detection mechanisms. Track metrics including poisoned sample detection rate, time-to-detection for post-deployment behavioral drift, data provenance coverage rate, and human review coverage for high-risk data contributions. Conduct periodic audits of training data lineage records to verify chain-of-custody integrity, and red team exercises targeting training pipelines through insider threat and supply chain compromise scenarios. Adapt data validation controls, access review cadences, and behavioral drift monitoring thresholds based on findings and emerging attack patterns.

## Tooling landscape

**Categories.** MLSecOps / AI Supply Chain Security; Data Quality & Observability; AI-SPM

**Poisoning detection & data validation**

- IBM Adversarial Robustness Toolbox (ART) (poisoning attacks & defenses) — https://github.com/Trusted-AI/adversarial-robustness-toolbox
- Google TensorFlow Data Validation (schema/drift/anomaly checks on training data) — https://github.com/tensorflow/data-validation
- DataHub (LinkedIn-originated) (lineage to trace tainted sources) — https://github.com/datahub-project/datahub
- Sigstore cosign (OpenSSF) (signing of approved datasets) — https://github.com/sigstore/cosign
