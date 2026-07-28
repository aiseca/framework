---
id: AISECA-ENV-001
title: "Excessive compute consumption"
domain: "Environmental Impacts (energy usage, carbon footprint, resource consumption)"
severity: Low
nist_ai_rmf: ["MEA-3"]
mitre_atlas: "Conditional: Impact – Cost Harvesting (AML.T0034); Impact – Denial of AI Service (AML.T0029)"
stakeholders: ["Builder / Maintainer"]
references:
  - https://www.theregister.com/security/2026/03/03/dev-stunned-by-82k-gemini-api-key-bill-after-theft/4925029
---

# AISECA-ENV-001 — Excessive compute consumption

**Risk.** AI consumes excessive computing resources, creating unnecessary cost, performance, or availability impacts.

**Scenario.** A coding assistant with access to a large enterprise codebase enters a recursive loop, spawning thousands of expensive operations as it seeks to iteratively refactor the codebase. Cloud costs spike overnight before anyone notices the runaway process.

## Tier 1 — Define & Constrain

Establish policies and configurations that bound AI resource usage. Publish an acceptable use policy defining approved agentic use cases and require budget ownership for workloads above defined thresholds. Technically, configure hard limits on token usage, tool-call depth, concurrency, and other AI metrics, enforce spend caps with budget alerts, and restrict production credentials to vetted & scoped service accounts.

## Tier 2 — Enforce & Monitor

Deploy runtime controls that terminate sessions exceeding token, cost, or other thresholds. Require human approval for long-running or high-cost agentic operations. Apply circuit breakers that detect repetitive tool calls or loops and halt execution. Stream usage telemetry into centralized observability tools with alerting. Monitor for spend spikes and other as-defined activity that trigger automated throttling or escalation.

## Tier 3 — Validate & Adapt

Test and evolve consumption controls as agents and workloads change. Conduct periodic load testing of agentic workflows, including adversarial prompts designed to induce loops and validate that circuit breakers, budget caps, and escalation mechanisms actually engage. Audit production usage to identify inefficient agents or prompts driving disproportionate spend, and feed findings into updated limits and guardrail logic. Integrate incidents into enterprise risk reporting.

## Tooling landscape

**Categories.** FinOps / Cloud Cost Management; Observability; Sustainability (GreenOps)

**Resource quotas & usage telemetry**

- Kubernetes ResourceQuota/LimitRange (Google/CNCF) — https://kubernetes.io/docs/concepts/policy/resource-quotas/
- KEDA (Microsoft-originated/CNCF) (demand-based scaling) — https://github.com/kedacore/keda
- OpenTelemetry (CNCF) — https://opentelemetry.io
- Datadog Agent (open source) (consumption metering) — https://github.com/DataDog/datadog-agent
- Cloud Carbon Footprint (Thoughtworks) — https://github.com/cloud-carbon-footprint/cloud-carbon-footprint
