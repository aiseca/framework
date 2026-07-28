---
id: AISECA-HAIC-004
title: "Agent continues execution loops beyond intended bounds or stop conditions"
domain: "Human–AI Configuration & Overreliance"
severity: Medium
nist_ai_rmf: ["GOV-2", "MAP-4", "MAN-2"]
mitre_atlas: "Conditional: Impact – Cost Harvesting (AML.T0034); Impact – Denial of AI Service (AML.T0029)"
stakeholders: ["Builder / Maintainer"]
references: []
---

# AISECA-HAIC-004 — Agent continues execution loops beyond intended bounds or stop conditions

**Risk.** An AI agent continues operating after it should have stopped, creating unintended actions or consequences.

**Scenario.** A DevOps team configures an AI agent to automatically remediate failing CI/CD pipeline builds. The agent encounters a flaky integration test and enters a retry loop, repeatedly re-triggering the full build pipeline. Over six hours, the agent consumes thousands of compute hours, generates over 200 failed build artifacts, floods the team's notification channels with alerts, and blocks other teams' deployments — all while the original test failure was caused by a transient third-party API outage that resolved itself after twenty minutes.

https://dev.to/utibe_okodi_339fb47a13ef5/the-ai-agent-that-cost-47000-while-everyone-thought-it-was-working-1lg6

https://cordum.io/blog/agent-finops-token-cost-governance

## Tier 1 — Define & Constrain

Define explicit execution limits and stop conditions for all agent workflows, including maximum iteration counts, wall-clock time limits, and output volume thresholds. Require that all agent deployments include configurable circuit breakers that halt execution when predefined limits are reached. Establish policies for retry behavior including maximum retry counts, exponential backoff requirements, and conditions under which the agent must escalate to a human rather than continue retrying. Document stop conditions in the agent's deployment specification, reviewed and approved by the responsible owner.

## Tier 2 — Enforce & Monitor

Enforce runtime constraints on execution loops through platform-level controls that monitor iteration counts, elapsed time, and resource consumption in real time. Implement automated circuit breakers that suspend agent execution when any defined limit is exceeded, with alerts routed to the responsible operator. Monitor for patterns indicative of runaway execution, including rapid repeated tool calls, identical or near-identical outputs across iterations, and escalating resource consumption without progress toward the stated goal. Log all loop iterations with full context to support post-incident analysis.

## Tier 3 — Validate & Adapt

Continuously test execution limits using simulated failure scenarios and adversarial inputs designed to trigger infinite loops, retry storms, and resource exhaustion. Track metrics including loop termination rate, average iterations before halt, false-positive circuit breaker activations, and time-to-detection for runaway executions. Review and adapt execution limits based on operational data, ensuring thresholds remain appropriate as agent capabilities and workloads evolve. Conduct periodic chaos engineering exercises to validate that circuit breakers and stop conditions function correctly under realistic failure modes.

## Tooling landscape

**Categories.** Agentic AI Security / AI Agent Governance; AIDR

**Execution bounds & termination enforcement**

- Microsoft AutoGen (max-turn/termination conditions) — https://github.com/microsoft/autogen
- Kubernetes Job deadlines & liveness controls (Google/CNCF) — https://kubernetes.io/docs/concepts/workloads/controllers/job/
- Cadence (Uber-originated) (workflow timeouts/retries) — https://github.com/uber/cadence
- Falco (Sysdig/CNCF) (alerts on anomalous long-running activity) — https://github.com/falcosecurity/falco
