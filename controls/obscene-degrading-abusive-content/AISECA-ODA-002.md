---
id: AISECA-ODA-002
title: "Harassment or abuse"
domain: "Obscene, Degrading, or Abusive Content"
severity: Medium
nist_ai_rmf: ["MAP-3", "MAN-3"]
mitre_atlas: "Conditional: Execution – LLM Prompt Injection (AML.T0051); Defense Evasion – LLM Jailbreak (AML.T0054); Impact – External Harms (AML.T0048)"
stakeholders: ["Leadership"]
references: []
---

# AISECA-ODA-002 — Harassment or abuse

**Risk.** AI generates, facilitates, or amplifies abusive, threatening, or harmful behavior toward individuals or groups.

**Scenario.** A national bank deploys an AI-powered customer service assistant accessible via its mobile banking app. A subset of users discover that through carefully constructed prompt sequences, including roleplay framing and identity-shifting instructions,  the assistant can be coerced into generating targeted, personalized harassment directed at named individuals and degrading content designed to be forwarded to third parties. Screenshots of the outputs circulate on social media, generating significant reputational damage before the bank's trust and safety team identifies the pattern and issues an emergency policy update. Post-incident analysis reveals the model had no session-level behavioral monitoring capable of detecting escalating harassment intent across a multi-turn conversation.

https://theconversation.com/an-ai-companion-chatbot-is-inciting-self-harm-sexual-violence-and-terror-attacks-252625

https://naturalandartificiallaw.com/garcia-v-character-ai-update/

## Tier 1 — Define & Constrain

Define conduct standards and prohibited content categories that apply to all AI systems interacting with customers, employees, or third parties, explicitly prohibiting the generation of harassing, threatening, degrading, or abusive content regardless of framing, persona assignment, or conversational context. Require that all customer-facing and employee-facing AI deployments include documented content policies covering harassment and abuse vectors, approved by the responsible Trust and Safety and Legal functions, with explicit coverage of multi-turn manipulation, roleplay and persona-based evasion, and content designed to be used against third parties not present in the conversation. Establish a content classification taxonomy that distinguishes prohibited harassment and abuse from permissible assertive, critical, or satirical content.

## Tier 2 — Enforce & Monitor

Enforce harassment and abuse content controls through a detection stack that includes classifier models trained on harassment and abuse patterns, session-level behavioral monitoring that tracks escalating or manipulative conversation trajectories, and output filtering that blocks generation when harassment intent signals exceed defined thresholds. Implement incident response workflows triggered by detected harassment events, including automatic session termination, user account flagging for review, and routing to the responsible trust and safety team. Monitor for known evasion patterns including roleplay and fictional framing, third-party targeting where abusive content is directed at someone other than the session user, and multi-turn context manipulation that gradually shifts the model toward abusive outputs.

## Tier 3 — Validate & Adapt

Continuously test harassment and abuse controls using red team exercises and automated adversarial test suites that simulate the full range of known evasion techniques, including roleplay injection, indirect third-party targeting, persona manipulation, and multi-turn escalation. Track metrics including harassment detection rate by evasion technique, false positive rate for legitimate assertive content, session escalation detection rate, and mean time to containment following detection. Conduct post-incident reviews of any harassment events that reach users, analyzing the conversation trajectory to identify detection gaps, and adapt classifier models, monitoring thresholds, and session-level behavioral controls based on findings. Update conduct policies as new misuse patterns are identified.

## Tooling landscape

**Categories.** Content Moderation (Trust & Safety); AI Guardrails

**Abuse & harassment detection**

- Meta Llama Guard 3 — https://github.com/meta-llama/PurpleLlama
- Google ShieldGemma (harassment) — https://ai.google.dev/gemma/docs/shieldgemma
- IBM Granite Guardian (toxicity/profanity detectors) — https://github.com/ibm-granite/granite-guardian
- NVIDIA NeMo Guardrails (moderation rails) — https://github.com/NVIDIA/NeMo-Guardrails
