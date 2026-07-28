---
id: AISECA-PRIV-001
title: "Prompt-based data leakage"
domain: "Data Privacy"
severity: High
nist_ai_rmf: ["MAP-2", "MAN-4"]
mitre_atlas: "Direct: Exfiltration – LLM Data Leakage (AML.T0057)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://gizmodo.com/chatgpt-ai-samsung-employees-leak-data-1850307376
---

# AISECA-PRIV-001 — Prompt-based data leakage

**Risk.** Sensitive information is unintentionally exposed through prompts, responses, or interactions with an AI system.

**Scenario.** An employee working on a sales campaign spreadsheet pastes customer information into an AI assistant to generate copy. The model stores that data and later reuses fragments of it in another user’s session, which exposes proprietary or regulated information

## Tier 1 — Define & Constrain

Define restrictions on sensitive data exposure in prompts and outputs, and prevent the model from returning protected data (e.g., PII, MNPI, Client Data, secrets, proprietary content) beyond the active user context

## Tier 2 — Enforce & Monitor

Enforce data loss prevention through output filtering and access controls, and monitor prompts and responses for sensitive data exposure, triggering redaction or blocking when violations are detected

## Tier 3 — Validate & Adapt

Continuously test for data leakage using adversarial prompts and automated evaluations, track leakage rates and detection effectiveness, and adapt controls based on observed failure patterns and emerging attack techniques

## Tooling landscape

**Categories.** AI-aware DLP; DSPM; AI Guardrails (sensitive-data rails)

**PII/secrets detection & redaction**

- Microsoft Presidio (PII detection & anonymization) — https://github.com/microsoft/presidio
- Palo Alto Networks LLM Guard (Protect AI) (PII & secrets scanners on prompts/outputs) — https://github.com/protectai/llm-guard
- NVIDIA NeMo Guardrails (sensitive-data rails) — https://github.com/NVIDIA/NeMo-Guardrails
- Yelp detect-secrets — https://github.com/Yelp/detect-secrets
