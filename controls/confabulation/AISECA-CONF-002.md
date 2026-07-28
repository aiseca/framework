---
id: AISECA-CONF-002
title: "Incorrect citations or fabricated sources / information"
domain: "Confabulation (Hallucinations)"
severity: Medium
nist_ai_rmf: ["MAP-3", "MEA-1", "MAN-2"]
mitre_atlas: "Conditional: Defense Evasion – LLM Trusted Output Components Manipulation (AML.T0067)"
stakeholders: ["Builder / Maintainer"]
references:
  - https://www.nytimes.com/2023/05/27/nyregion/chatgpt-lawyers.html
---

# AISECA-CONF-002 — Incorrect citations or fabricated sources / information

**Risk.** AI invents sources, references, citations, or supporting evidence that do not actually exist.

**Scenario.** An LLM generated report includes fabricated citations that go unnoticed and inform a leadership decision, later requiring retraction.

## Tier 1 — Define & Constrain

Define and require verifiable sourcing for all citation-based outputs, restricting the model from presenting unverified or inferred sources as factual

## Tier 2 — Enforce & Monitor

Ensure data provenance by making sure every citation can be traced to a real source and clearly supports the claim; monitor outputs for missing or unsupported citations and trigger fallback or suppression when checks fail

## Tier 3 — Validate & Adapt

Continuously test citation accuracy using automated evaluations and adversarial scenarios, track false citation rates and grounding coverage, and adapt controls based on observed hallucination and failure patterns

## Tooling landscape

**Categories.** LLM Evaluation & AI Observability; AI Guardrails (grounding rails)

**Citation & source verification**

- NVIDIA NeMo Guardrails (grounding against retrieved sources) — https://github.com/NVIDIA/NeMo-Guardrails
- IBM Granite Guardian (context relevance/groundedness) — https://github.com/ibm-granite/granite-guardian
- MLflow LLM Evaluate (Databricks) (citation-accuracy test suites) — https://github.com/mlflow/mlflow
- OpenAI Evals — https://github.com/openai/evals
