---
id: AISECA-INFOSEC-019
title: "Public Discovery of Internal AI Middleware"
domain: "Information Security"
severity: Medium
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Reconnaissance – Active Scanning (AML.T0006); Search Victim-Owned Websites (AML.T0003)"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-INFOSEC-019 — Public Discovery of Internal AI Middleware

**Risk.** Internal AI middleware, orchestration services, or endpoints become publicly discoverable and expose information useful to attackers.

**Scenario.** Exposed AI infrastructure enables reconnaissance and targeted attacks against AI services.

## Tier 1 — Define & Constrain

Define disclosure restrictions for AI system architecture, prohibiting AI systems from revealing system prompt contents, internal tool names, middleware component identities, integration endpoints, or deployment architecture details in user-facing responses. Require that all AI deployments include output filters detecting and suppressing architectural disclosure, and establish approved deflection templates for architecture probing queries.

## Tier 2 — Enforce & Monitor

Enforce architectural confidentiality through output monitoring that detects responses containing system prompt fragments, internal tool or service names, infrastructure references, or other architectural identifiers. Implement output filtering that redacts detected architectural disclosures before responses are returned, and log probing attempts for threat intelligence purposes.

## Tier 3 — Validate & Adapt

Continuously test architectural disclosure controls using adversarial probing queries designed to extract system prompt content, tool names, and middleware architecture through direct and indirect elicitation. Track metrics including architecture disclosure rate by probing technique, suppression effectiveness, and probing attempt volume as a leading indicator of targeted exploitation. Adapt filters based on findings.

## Tooling landscape

**Categories.** EASM; Vulnerability Assessment; API Security

- Google Tsunami (network/exposure scanning) — https://github.com/google/tsunami-security-scanner
- OWASP Amass (attack-surface enumeration) — https://github.com/owasp-amass/amass
- Rapid7 Metasploit (exposure validation) — https://github.com/rapid7/metasploit-framework
- Envoy (Lyft-originated/CNCF) (authentication proxy in front of internal AI middleware) — https://github.com/envoyproxy/envoy
