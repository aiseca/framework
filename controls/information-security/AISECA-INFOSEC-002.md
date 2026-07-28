---
id: AISECA-INFOSEC-002
title: "Compromised AI credentials"
domain: "Information Security"
severity: High
nist_ai_rmf: ["MAP-5", "MAN-1", "MAN-3"]
mitre_atlas: "Direct: Credential Access – Unsecured Credentials (AML.T0055); Credential Access – Credentials from AI Agent Configuration (AML.T0083); Credential Access – AI Agent Tool Credential Harvesting (AML.T0098); Initial Access – Valid Accounts (AML.T0012)"
stakeholders: ["Cybersecurity / Assurance"]
references:
  - https://arxiv.org/abs/2509.10540
---

# AISECA-INFOSEC-002 — Compromised AI credentials

**Risk.** Accounts, passwords, API keys, tokens, or credentials used by AI systems are stolen, exposed, or misused.

**Scenario.** Someone steals the login or API key for an AI system and uses it to access data or run the system as if they were authorized. This can lead to data leaks, abuse, or unexpected costs.

## Tier 1 — Define & Constrain

Define how AI systems and tools are accessed securely, including clear rules for managing API keys, service accounts, and user credentials. Define who owns these credentials, who is allowed to use them, and ensure access is limited to only what is necessary (least-privilege principle).

## Tier 2 — Enforce & Monitor

Enforce secure access by protecting credentials (e.g., using a secrets manager), limiting permissions to only what is needed, and requiring authentication controls such as key rotation and, where appropriate, multi-factor authentication. Monitor and log all access and usage to detect unauthorized activity.

## Tier 3 — Validate & Adapt

Continuously adapt by monitoring for unusual usage patterns that may indicate compromised credentials, rotating and revoking credentials when risks are identified, and periodically reviewing access controls and permissions. Prevent credentials from being placed into the model's context by instead using interception for credentials when an authenticated tool or MCP is used (i.e. AWS AgentCore Gateway)

## Tooling landscape

**Categories.** PAM / Secrets Management; NHI; secret scanning (DevSecOps/AST)

**Secrets management & leak detection**

- CyberArk Conjur (open source secrets management) — https://github.com/cyberark/conjur
- SPIFFE/SPIRE (CNCF; HPE-backed) (short-lived credentials replacing static keys) — https://github.com/spiffe/spire
- AWS git-secrets (pre-commit scanning) — https://github.com/awslabs/git-secrets
- Yelp detect-secrets — https://github.com/Yelp/detect-secrets
- Palo Alto Networks LLM Guard (Protect AI) (secrets scanner on prompts/outputs) — https://github.com/protectai/llm-guard
