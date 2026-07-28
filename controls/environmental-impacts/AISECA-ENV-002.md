---
id: AISECA-ENV-002
title: "Inefficient inference or training"
domain: "Environmental Impacts (energy usage, carbon footprint, resource consumption)"
severity: Low
nist_ai_rmf: ["MEA-3"]
mitre_atlas: "No Direct Mapping"
stakeholders: ["Builder / Maintainer"]
references:
  - https://en.wikipedia.org/wiki/Artificial_intelligence_and_climate_change
---

# AISECA-ENV-002 — Inefficient inference or training

**Risk.** AI models use more processing power, time, or infrastructure than necessary to perform their intended function.

**Scenario.** AI takes longer and costs more than it should to run because it isn’t built efficiently. This leads to slow responses and unnecessarily high operating costs.

## Tier 1 — Define & Constrain

Define performance, cost, and execution constraints for all AI workloads, including target response times, cost per request, and maximum token usage. Establish model selection policies that prioritize smaller, specialized models where feasible over large general-purpose models. Define acceptable use cases for high-cost models and require justification. Establish baseline controls for efficient execution, including caching strategies, reuse of prior results, and avoidance of redundant model calls. Define maximum runtime and cost thresholds for any single request or workflow.

## Tier 2 — Enforce & Monitor

Enforce efficient and bounded execution through technical controls, including rate limiting on token usage, caps on compute consumption, and restrictions on model selection based on use case. Implement runtime and cost guardrails that automatically interrupt or terminate requests exceeding predefined thresholds. Optimize execution by minimizing redundant computation (e.g., caching, deduplication, batching) and routing workloads to appropriately sized models. Continuously monitor performance, latency, token usage, and cost against defined baselines, and generate alerts when thresholds are exceeded.

## Tier 3 — Validate & Adapt

Continuously adapt by analyzing performance and cost to identify inefficiencies and refine system efficiency over time. Update performance and cost baselines and models as usage scales to improve speed, reduce waste, and control costs.

## Tooling landscape

**Categories.** ModelOps / MLOps (inference & training optimization)

**Model & inference optimization**

- Microsoft DeepSpeed (training/inference efficiency) — https://github.com/microsoft/DeepSpeed
- NVIDIA TensorRT-LLM — https://github.com/NVIDIA/TensorRT-LLM
- NVIDIA Triton Inference Server — https://github.com/triton-inference-server/server
- Microsoft ONNX Runtime (quantization & graph optimization) — https://github.com/microsoft/onnxruntime
