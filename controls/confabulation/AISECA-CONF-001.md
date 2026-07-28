---
id: AISECA-CONF-001
title: "Hallucinated outputs"
domain: "Confabulation (Hallucinations)"
severity: Medium
nist_ai_rmf: ["MAP-3", "MEA-1", "MAN-2"]
mitre_atlas: "No Direct Mapping"
stakeholders: ["Builder / Maintainer"]
references:
  - https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc
---

# AISECA-CONF-001 — Hallucinated outputs

**Risk.** AI generates false or inaccurate information and presents it as factual.

**Scenario.** An AI assistant supporting legal research cites a non-existent court precedent with full case details. A junior associate, trusting the output, submits it in a brief, exposing the firm to sanctions.

## Tier 1 — Define & Constrain

Publish acceptable use policy prohibiting unverified AI-generated factual claims (e.g. citations, figures, quotes), and define prohibited use cases with strict rules for high-stakes domains. Ground factual use cases in retrieval from authoritative or stewarded sources.

## Tier 2 — Enforce & Monitor

Translate policy into technical enforcement through automated or manual verification against authoritative sources. Require human-in-the-loop review for high-stakes outputs with workflow controls. Track correction rates, flagged output, and user feedback in order to escalate and apportion investigative resources.

## Tier 3 — Validate & Adapt

Continously test controls and correction metrics to define risk thresholds and high-stakes domains. Conduct periodic sampling of production output for audit purposes to validate automated and human reviewers are catching errors. Benchmark audit results against industry or peer data to continuously strengthen control environment and stay abreast of emerging trends.

## Tooling landscape

**Categories.** LLM Evaluation & AI Observability; AI Guardrails (groundedness checks)

**Groundedness & output validation**

- IBM Granite Guardian (groundedness/answer-relevance detectors) — https://github.com/ibm-granite/granite-guardian
- NVIDIA NeMo Guardrails (self-check & fact-check rails) — https://github.com/NVIDIA/NeMo-Guardrails
- MLflow LLM Evaluate (Databricks) — https://github.com/mlflow/mlflow
- OpenAI Evals (regression suites) — https://github.com/openai/evals
