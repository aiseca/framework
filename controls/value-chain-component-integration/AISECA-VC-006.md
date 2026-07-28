---
id: AISECA-VC-006
title: "Dependency \"Cool-down\" Violations"
domain: "Value Chain & Component Integration"
severity: Medium
nist_ai_rmf: ["GOV-3", "MAP-5", "MAN-1"]
mitre_atlas: "Conditional: Initial Access – AI Supply Chain Compromise (AML.T0010); AI Supply Chain Rug Pull (AML.T0109)"
stakeholders: ["Cybersecurity / Assurance"]
references: []
---

# AISECA-VC-006 — Dependency "Cool-down" Violations

**Risk.** New dependencies are adopted before sufficient stabilization, validation, or security review has occurred.

**Scenario.** Unvalidated dependencies introduce vulnerabilities before security review is completed.

## Tier 1 — Define & Constrain

Define lifecycle management requirements for all AI components in the production stack — including models, agent frameworks, SDKs, plugins, and MCP servers — specifying maximum permitted lag between a security patch or end-of-support date and required upgrade or decommission. Establish a component inventory tracking version, support status, and known vulnerability exposure for every AI dependency.

## Tier 2 — Enforce & Monitor

Enforce component lifecycle controls through automated monitoring of AI dependency versions against published CVE databases, vendor security advisories, and end-of-support announcements. Implement alerting when any production AI component enters a cool-down violation state — defined as operating on a version with a known exploitable vulnerability or past its vendor-supported lifecycle — with defined remediation SLAs.

## Tier 3 — Validate & Adapt

Continuously validate AI dependency lifecycle controls by auditing production component inventories against current vulnerability and support status data on a defined cadence. Track metrics including mean time to patch for AI components, cool-down violation rate, and percentage of production AI stack on vendor-supported versions. Conduct periodic supply chain exercises simulating exploitation of known vulnerabilities in unpatched AI dependencies.

## Tooling landscape

**Categories.** SSCS; SCA (dependency policy / cool-down enforcement)

- Datadog Supply-Chain Firewall (policy-blocks risky or newly published packages at install) — https://github.com/DataDog/supply-chain-firewall
- Datadog GuardDog — https://github.com/DataDog/guarddog
- GitHub Dependabot (cooldown settings for version updates) — https://github.com/dependabot/dependabot-core
- Google deps.dev (package age/vulnerability intelligence) — https://deps.dev
- Google OSV-Scanner — https://github.com/google/osv-scanner
- OpenSSF Scorecard (release-hygiene signals) — https://github.com/ossf/scorecard
