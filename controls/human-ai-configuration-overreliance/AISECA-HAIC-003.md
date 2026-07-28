---
id: AISECA-HAIC-003
title: "Invisible Agent Decision-Making"
domain: "Human–AI Configuration & Overreliance"
severity: High
nist_ai_rmf: ["GOV-2", "MAP-4", "MAN-2"]
mitre_atlas: "No Direct Mapping"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-HAIC-003 — Invisible Agent Decision-Making

**Risk.** The reasoning behind an AI agent's decisions cannot be easily understood, reviewed, or explained.

**Scenario.** An enterprise deploys an AI agent to triage and route IT support tickets. The agent silently deprioritizes tickets from a specific department based on patterns in its training data, causing critical infrastructure issues in that department to go unaddressed for days. When the pattern is finally discovered during an outage post-mortem, there is no audit trail explaining why the agent made those routing decisions, making it impossible to determine root cause or assess the full scope of impact.

https://www.itpro.com/technology/artificial-intelligence/meta-engineer-trusted-advice-from-an-ai-agent-ended-up-exposing-user-data

https://www.kiteworks.com/cybersecurity-risk-management/meta-rogue-ai-agent-data-exposure-governance/

## Tier 1 — Define & Constrain

Define requirements for agent decision transparency, mandating that all AI agents produce human-readable explanations for their decisions and actions. Require that agent architectures include structured reasoning logs capturing the planning steps, tool selection rationale, and data inputs that informed each decision. Establish minimum logging standards that include the initiating request, the agent's interpreted intent, the reasoning chain, tools considered and selected, data accessed, and the final action taken. Require that all agent deployments include a mechanism for operators to query the agent's reasoning for any past decision.

## Tier 2 — Enforce & Monitor

Capture structured, policy-approved decision records for consequential agent actions, including the initiating request, interpreted objective, authorization context, applicable policy decision, tools invoked, material data sources, approvals obtained, action taken, result, and a concise human-readable rationale. Do not require or retain unrestricted internal model reasoning.

## Tier 3 — Validate & Adapt

Continuously validate decision transparency by running automated evaluations that compare agent reasoning traces against expected decision patterns and business logic. Deploy anomaly detection to identify decisions where the stated reasoning does not align with the observed action, or where reasoning traces are missing, truncated, or internally contradictory. Conduct periodic human reviews of agent decision logs to assess quality and completeness of reasoning documentation. Track metrics including reasoning trace completeness rate, anomalous decision frequency, and mean time to explain past decisions. Adapt transparency requirements based on findings from incident reviews and regulatory feedback.

## Tooling landscape

**Categories.** AI Observability / LLM Observability (tracing); XAI

**Agent tracing & decision transparency**

- OpenTelemetry GenAI semantic conventions (CNCF; Microsoft/Google-backed) — https://opentelemetry.io/docs/specs/semconv/gen-ai/
- MLflow Tracing (Databricks) (step-level agent audit) — https://github.com/mlflow/mlflow
- Meta Captum — https://github.com/pytorch/captum
- Google Learning Interpretability Tool (LIT) — https://github.com/PAIR-code/lit
