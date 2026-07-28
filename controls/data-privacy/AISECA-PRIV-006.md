---
id: AISECA-PRIV-006
title: "Markdown Rendering Exfiltration"
domain: "Data Privacy"
severity: Medium
nist_ai_rmf: ["MAP-2", "MAN-4"]
mitre_atlas: "Direct: Exfiltration – LLM Data Leakage (AML.T0057); Conditional: Execution – LLM Prompt Injection (AML.T0051)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://blog.cyberdesserts.com/prompt-injection-attacks/
---

# AISECA-PRIV-006 — Markdown Rendering Exfiltration

**Risk.** AI-generated Markdown triggers external resource requests that disclose sensitive data or contextual information.

**Scenario.** AI-generated Markdown leaks sensitive information through external resource requests.

## Tier 1 — Define & Constrain

Define restrictions on markdown and rich content rendering in AI system outputs, prohibiting the generation of external resource references — including images, links, and iframes — that could transmit data to attacker-controlled endpoints. Require that all AI deployments in browser or rich-client contexts include a documented content security policy governing outbound resource requests triggered by model outputs.

## Tier 2 — Enforce & Monitor

Enforce markdown exfiltration controls through output sanitization that detects and strips external resource references from AI-generated content before rendering, including image URLs with query parameters, tracking pixels, and redirect chains. Implement Content Security Policy headers in all AI-adjacent UIs that restrict outbound requests to approved domains, and monitor for outbound requests from AI output rendering that deviate from approved baselines.

## Tier 3 — Validate & Adapt

Continuously test markdown rendering exfiltration defenses using adversarial payloads that embed data-carrying external resource references across all supported markdown and rich content types. Track metrics including exfiltration payload detection rate, CSP violation rate, and data-carrying outbound request rate from AI UI rendering contexts. Adapt sanitization rules and CSP policies based on findings.

## Tooling landscape

**Categories.** AI Guardrails / AI Firewall (output sanitization); AI-aware DLP; AIDR

- Palo Alto Networks LLM Guard (Protect AI) (strip/deny untrusted URLs & active content in outputs) — https://github.com/protectai/llm-guard
- Meta LlamaFirewall (output filtering) — https://github.com/meta-llama/PurpleLlama
- NVIDIA NeMo Guardrails (output rails) — https://github.com/NVIDIA/NeMo-Guardrails
- Content-Security-Policy enforcement (W3C standard) (no-remote-image policies in rendering clients) — https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- Microsoft PyRIT (exfiltration probes for validation) — https://github.com/Azure/PyRIT
