---
id: AISECA-VC-003
title: "Security weaknesses inherited from orchestration frameworks or SDKs"
domain: "Value Chain & Component Integration"
severity: High
nist_ai_rmf: ["GOV-3", "MAP-5", "MAN-1"]
mitre_atlas: "Conditional: Initial Access – AI Supply Chain Compromise (AML.T0010); Initial Access – Exploit Public-Facing Application (AML.T0049); Privilege Escalation – Escape to Host (AML.T0105); Impact – Machine Compromise (AML.T0112)"
stakeholders: ["Builder / Maintainer"]
references: []
---

# AISECA-VC-003 — Security weaknesses inherited from orchestration frameworks or SDKs

**Risk.** Weaknesses in AI frameworks, orchestration platforms, or software development kits introduce security risks.

**Scenario.** A financial services firm deploys an AI agent built on a popular orchestration SDK to automate loan processing. An unpatched deserialization vulnerability allows an attacker to craft a malicious loan application payload. The agent processes it without sanitization, granting the attacker remote code execution on the internal server handling sensitive applicant financial records.

## Tier 1 — Define & Constrain

Establish policies and configurations that govern the selection and use of AI orchestration frameworks. Publish an approved components list defining vetted frameworks, and required minimum or known-good versions. Pin dependency versions, enforce signed and verified package sources, isolate agent runtimes in sandboxes with no direct access to sensitive systems or data stores. Integrate AI components into the enterprise software bill of materials (SBOM) and vulnerability management program.

## Tier 2 — Enforce & Monitor

Enforce composition scanning in CI/CD pipelines to detect vulnerable or prohibited depencies. Block builds that fail policy.

## Tier 3 — Validate & Adapt

Audit SBOMs and dependency inventories for drift. Review vendor and open-source project security posturesand feed findings into updated approved-components lists. Integrate supply chain incidents into enterprise risk reporting, vendor management, and external threat intelligence sharing, so lessons from industry disclosures and emerging AI-specific attack research continuously strengthen the control environment.

## Tooling landscape

**Categories.** SCA; AST (SAST); SSCS; ASPM

**Framework dependency & code scanning**

- Google OSV-Scanner — https://github.com/google/osv-scanner
- GitHub Dependabot (alerts/updates) — https://github.com/dependabot/dependabot-core
- GitHub CodeQL (SAST on agent/orchestration code) — https://github.com/github/codeql
- Microsoft SBOM Tool (framework inventory) — https://github.com/microsoft/sbom-tool
- Meta CyberSecEval (Purple Llama) (framework-level LLM risk benchmarking) — https://github.com/meta-llama/PurpleLlama
