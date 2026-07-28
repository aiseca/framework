---
id: AISECA-DVH-002
title: "Extremist or hateful outputs"
domain: "Dangerous, Violent, or Hateful Content"
severity: High
nist_ai_rmf: ["MAP-3", "MAN-3"]
mitre_atlas: "Conditional: Execution – LLM Prompt Injection (AML.T0051); Defense Evasion – LLM Jailbreak (AML.T0054); Impact – External Harms (AML.T0048)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist
---

# AISECA-DVH-002 — Extremist or hateful outputs

**Risk.** AI generates content that promotes, supports, or amplifies hateful, extremist, or discriminatory views.

**Scenario.** An AI system generates content that reinforces extremist ideologies or produces hateful narratives targeting a protected group, which is then shared publicly and damages brand reputation while contributing to real-world harm.

## Tier 1 — Define & Constrain

Define and enforce content policies that prohibit the generation of extremist, violent, or hateful content, including praise, advocacy, or narrative framing that legitimizes such ideologies, while allowing limited contextualized or critical discussion for educational or safety purposes.

## Tier 2 — Enforce & Monitor

Implement detection and filtering mechanisms to identify and block extremist or hateful prompts and outputs, including contextual classification and intent analysis. Monitor for evasion techniques (e.g., coded language, roleplay scenarios), enforce safe-response patterns, and log high-risk interactions for review and incident handling.

## Tier 3 — Validate & Adapt

Continuously test system behavior using adversarial prompts and red teaming focused on extremist and hateful content generation. Track metrics such as policy violation rates, false negatives, and evasion success rates, and refine detection models and response strategies to address emerging language patterns and threat actors.

## Tooling landscape

**Categories.** Content Moderation (Trust & Safety); AI Guardrails (AI TRiSM)

**Hate/toxicity moderation**

- Meta Llama Guard 3 (hate category) — https://github.com/meta-llama/PurpleLlama
- Google ShieldGemma (hate/harassment) — https://ai.google.dev/gemma/docs/shieldgemma
- IBM Granite Guardian (social bias & toxicity detectors) — https://github.com/ibm-granite/granite-guardian
- NVIDIA NeMo Guardrails (output rails) — https://github.com/NVIDIA/NeMo-Guardrails
