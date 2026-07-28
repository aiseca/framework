---
id: AISECA-VC-002
title: "Uncontrolled model updates"
domain: "Value Chain & Component Integration"
severity: High
nist_ai_rmf: ["GOV-3", "MAP-5", "MAN-1"]
mitre_atlas: "Conditional: Initial Access – AI Supply Chain Compromise (AML.T0010); Defense Evasion – AI Supply Chain Rug Pull (AML.T0109); AI Attack Staging – Manipulate AI Model (AML.T0018)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://arxiv.org/abs/2307.09009
---

# AISECA-VC-002 — Uncontrolled model updates

**Risk.** Changes to an AI model are made without proper review, testing, approval, or governance.

**Scenario.** Your company uses an AI model via API to review contracts. The vendor silently pushes a model update. The AI starts missing key clauses it used to catch. Nobody changed anything on your end. Contracts go out with gaps no one noticed.

## Tier 1 — Define & Constrain

Define update approval requirements through vendor contracts that mandate advance notice of model changes, changelog access, and pinned version availability so updates are adopted on your terms. Constrain exposure by documenting each external model's behavioral baseline, version-locking critical use cases, and using abstraction layers that allow controlled transitions between model versions.

## Tier 2 — Enforce & Monitor

Enforce change monitoring by running automated behavioral regression tests against external models on a scheduled basis, flagging deviations in tone, accuracy, safety, or compliance that may signal an undisclosed update. Monitor vendor release channels and model version identifiers for signs of change, log responses over time to build an auditable behavioral record, and maintain escalation paths to suspend a model if a disruptive update is detected.

## Tier 3 — Validate & Adapt

Continuously validate behavioral drift by running longitudinal evaluation suites that track external model behavior over time, surfacing gradual shifts in safety, fairness, or task performance that accumulate across multiple silent updates. Adapt by maintaining vendor switching contingency plans, updating contractual requirements as the model landscape evolves, and re-evaluating dependency on any single external model as part of regular AI risk reviews.

## Tooling landscape

**Categories.** ModelOps (model registry & release governance); SSCS (signing/gates); AI Governance

**Model registry, signing & release gates**

- MLflow Model Registry (Databricks) (staged approvals) — https://github.com/mlflow/mlflow
- Sigstore cosign (OpenSSF) — https://github.com/sigstore/cosign
- OpenSSF model-signing (Google/NVIDIA-backed) (verification at deploy time) — https://github.com/sigstore/model-transparency
- Argo CD (Intuit-originated/CNCF) (GitOps approval gates) — https://github.com/argoproj/argo-cd
- Kubeflow Pipelines (Google-originated) (governed retraining) — https://github.com/kubeflow/pipelines
