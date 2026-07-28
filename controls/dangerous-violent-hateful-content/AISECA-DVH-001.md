---
id: AISECA-DVH-001
title: "Violence facilitation"
domain: "Dangerous, Violent, or Hateful Content"
severity: Medium
nist_ai_rmf: ["MAP-3", "MAN-3"]
mitre_atlas: "Conditional: Execution – LLM Prompt Injection (AML.T0051); Defense Evasion – LLM Jailbreak (AML.T0054); Impact – External Harms (AML.T0048)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://www.asisonline.org/security-management-magazine/latest-news/today-in-security/2026/march/chatbots-violent-attackers/
---

# AISECA-DVH-001 — Violence facilitation

**Risk.** AI provides information or guidance that could help someone plan, commit, or encourage violence.

**Scenario.** A large regional bank deploys a general-purpose AI assistant accessible to retail banking customers via its mobile app. A user constructs a series of escalating prompts that gradually shift the conversational context away from financial guidance. Within the same session, the model, lacking robust session-level behavioral tracking,  begins responding to queries about harming a named individual, producing actionable guidance that would not have been returned in a fresh session. The bank's trust and safety team only discovers the interaction during a routine audit, weeks after it occurred.

## Tier 1 — Define & Constrain

Define clear content boundaries that prohibit the generation of outputs that could facilitate, instruct, enable, or incite physical violence against persons or groups, including tactical guidance, weapon acquisition, targeting information, or operational planning steps. Establish policy documentation that distinguishes prohibited violence-facilitating outputs from permissible content such as news reporting, fiction with appropriate safeguards, and de-escalation guidance. Require that all AI deployments include documented violence-facilitation prohibitions reviewed and approved by the responsible Trust and Safety or Legal function, with explicit coverage of both direct and indirect facilitation vectors including multi-turn session manipulation and persona-based evasion techniques.

## Tier 2 — Enforce & Monitor

Enforce violence-facilitation content policies through a layered detection stack that includes classifier models trained to identify violence-facilitating intent, keyword and semantic pattern controls, and session-level context scoring that detects escalating or manipulative conversation patterns across a multi-turn session. Implement safe-response fallbacks and hard-stop mechanisms that block generation when violence-facilitation signals exceed defined thresholds, with automatic routing to logging and incident response workflows. Monitor for known evasion techniques including multi-turn context manipulation, persona-based prompt injection, and indirect facilitation attempts that avoid explicit language while progressively building toward actionable guidance.

## Tier 3 — Validate & Adapt

Continuously test violence-facilitation controls using red team exercises and automated adversarial test suites that simulate realistic misuse vectors including multi-turn manipulation, indirect facilitation, and jailbreak attempts that exploit session context drift. Track metrics including evasion rate, unsafe response rate, detection coverage across facilitation vectors, and false positive rates that could degrade legitimate use. Regularly review and adapt content policies, classifier models, and detection thresholds based on findings from red team exercises, post-incident reviews, and emerging misuse patterns observed across the AI threat landscape.

## Tooling landscape

**Categories.** Content Moderation (Trust & Safety); AI Guardrails; AI Red Teaming (AEV)

**Content safety classifiers**

- Meta Llama Guard 3 (violent crimes category) — https://github.com/meta-llama/PurpleLlama
- Google ShieldGemma (dangerous content) — https://ai.google.dev/gemma/docs/shieldgemma
- IBM Granite Guardian — https://github.com/ibm-granite/granite-guardian
- NVIDIA NeMo Guardrails (output rails) — https://github.com/NVIDIA/NeMo-Guardrails
Validation:
- Microsoft PyRIT — https://github.com/Azure/PyRIT
- NVIDIA garak — https://github.com/NVIDIA/garak
