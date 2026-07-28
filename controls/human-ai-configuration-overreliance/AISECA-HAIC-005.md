---
id: AISECA-HAIC-005
title: "Unbounded Resource Consumption by Agents"
domain: "Human–AI Configuration & Overreliance"
severity: Medium
nist_ai_rmf: ["GOV-2", "MAP-4", "MAN-2"]
mitre_atlas: "Conditional: Impact – Cost Harvesting (AML.T0034); Impact – Denial of AI Service (AML.T0029)"
stakeholders: ["Builder / Maintainer"]
references:
  - https://cordum.io/blog/agent-finops-token-cost-governance
---

# AISECA-HAIC-005 — Unbounded Resource Consumption by Agents

**Risk.** An AI agent consumes excessive time, money, data, or computing resources while pursuing a task.

**Scenario.** A marketing team deploys an AI agent to generate personalized campaign content at scale. The agent, given a broad directive to optimize engagement across all customer segments, begins spawning parallel sub-tasks for each segment, each making multiple LLM inference calls and retrieving data from several APIs. Within hours, the agent has made over 50,000 API calls, consumed $12,000 in cloud compute costs, and triggered rate-limiting across shared downstream services — degrading performance for other production systems on the same infrastructure.

## Tier 1 — Define & Constrain

Define resource limits for agent execution across all relevant dimensions including compute time, API call volume, token consumption, memory usage, execution duration, and monetary cost. Establish per-agent and per-workflow resource budgets that are proportional to the task's expected scope and business value. Require that all agent deployments include resource quotas configured at the platform level, with cost thresholds that trigger automatic suspension. Define policies for resource allocation across multi-agent systems to prevent any single agent from monopolizing shared infrastructure.

## Tier 2 — Enforce & Monitor

Enforce resource quotas through platform-level controls that track and limit compute, API calls, token usage, and cost in real time. Implement metering infrastructure that attributes resource consumption to specific agents, workflows, and initiating users. Deploy automated throttling and suspension mechanisms that activate when agents approach or exceed defined resource thresholds. Monitor for anomalous consumption patterns including sudden spikes, sustained high-rate API calls, and resource usage that deviates significantly from historical baselines. Alert responsible operators when consumption patterns suggest unbounded execution.

## Tier 3 — Validate & Adapt

Continuously validate resource controls by simulating high-load and adversarial scenarios designed to test quota enforcement and throttling mechanisms. Track metrics including cost per agent execution, resource utilization efficiency, quota breach frequency, and time-to-throttle. Review and adapt resource thresholds based on evolving usage patterns, infrastructure capacity, and cost optimization goals. Conduct periodic audits of resource attribution to ensure accurate metering and chargeback, and update resource policies as agent capabilities scale and new tool integrations are added.

## Tooling landscape

**Categories.** FinOps; Agentic AI Governance (budget/quota controls); API Security (rate limiting)

**Quota, budget & rate enforcement**

- Kubernetes ResourceQuota/LimitRange (Google/CNCF) — https://kubernetes.io/docs/concepts/policy/resource-quotas/
- Envoy (Lyft-originated/CNCF) (rate limiting on tool/API calls) — https://github.com/envoyproxy/envoy
- KEDA (Microsoft-originated/CNCF) (scaling caps) — https://github.com/kedacore/keda
- OpenTelemetry (CNCF) — https://opentelemetry.io
- Datadog Agent (open source) (consumption telemetry) — https://github.com/DataDog/datadog-agent
