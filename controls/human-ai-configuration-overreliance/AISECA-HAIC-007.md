---
id: AISECA-HAIC-007
title: "Delegation without accountability"
domain: "Human–AI Configuration & Overreliance"
severity: Medium
nist_ai_rmf: ["GOV-2", "MAP-4", "MAN-2"]
mitre_atlas: "No Direct Mapping"
stakeholders: ["Leadership"]
references:
  - https://www.nytimes.com/2023/05/27/nyregion/chatgpt-lawyers.html
---

# AISECA-HAIC-007 — Delegation without accountability

**Risk.** Tasks are delegated between agents without clear ownership, responsibility, or accountability for outcomes.

**Scenario.** Work is handed to AI, but no one is clearly responsible for checking it or owning the results. When mistakes happen, they slip through or no one takes responsibility.

## Tier 1 — Define & Constrain

Define ownership within formal processes that use AI, specifying who is responsible for reviewing, approving, and acting on outputs at each stage. Define where human oversight is required and how accountability is assigned across workflows.

## Tier 2 — Enforce & Monitor

Enforce accountability by embedding ownership and review requirements into workflows, ensuring AI outputs are validated by the appropriate roles before action is taken. Record decisions and actions to maintain clear traceability of responsibility.

## Tier 3 — Validate & Adapt

Continuously audit AI-assisted workflows to confirm ownership assignments are current and review checkpoints are being observed. Test accountability controls by introducing deliberate errors into AI outputs and measuring whether assigned owners catch and escalate them. Track metrics such as review completion rate and time-to-detect for AI-driven mistakes, and update ownership assignments as workflows and organizational roles evolve.

## Tooling landscape

**Categories.** NHI / Machine IAM; IGA (accountability); AI Observability

**Ownership & audit attribution**

- Keycloak (Red Hat) (OAuth 2.0 Token Exchange for on-behalf-of identity) — https://github.com/keycloak/keycloak
- SPIFFE/SPIRE (CNCF; HPE-backed) (workload identity per agent) — https://github.com/spiffe/spire
- OpenTelemetry (CNCF) (trace-context propagation) — https://opentelemetry.io
- MLflow Tracing (Databricks) (task-level audit) — https://github.com/mlflow/mlflow
