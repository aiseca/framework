# AISECA AI Security Maturity Framework

A three-tier model mapping practical security controls to NIST GenAI Risk Domains -- from foundational governance to adaptive, threat-aware defence.

**Status:** Draft 1 (In Progress) | **Target Release:** June 2026

---

## Overview

The AISECA AI Security Maturity Framework provides organisations with a structured approach to securing enterprise AI tooling. It is:

- **Practitioner-led** -- built by people who implement AI security, not just advise on it
- **Vendor-agnostic** -- no product dependencies, works with any stack
- **Mapped to NIST** -- aligned with NIST GenAI Risk Domains for regulatory compatibility
- **Tiered** -- progressive maturity levels so organisations can start where they are

## Framework Tiers

### Tier 01: Define & Constrain (Foundational Controls)

Foundational controls to get AI governance started.

| Control | Description |
|---------|-------------|
| AI Asset Inventory | Catalogue all AI tools, models, and integrations across the org |
| Acceptable Use Policy | Establish clear guidelines for how AI tools may be used |
| Access Control Baseline | Role-based access to AI systems and their training data |
| Initial Risk Assessment | Map AI deployments to NIST GenAI Risk Domains |
| Data Classification | Classify data flowing into and out of AI systems |
| Vendor Evaluation Criteria | Security evaluation standards for AI vendor selection |

### Tier 02: Enforce & Monitor (Operational Controls)

Operational controls with active enforcement.

| Control | Description |
|---------|-------------|
| Prompt Injection Defence | Input validation and sanitisation for all AI-facing interfaces |
| Data Leakage Prevention | Monitor and prevent sensitive data exfiltration through AI |
| Output Monitoring | Real-time scanning of AI outputs for policy violations |
| Automated Compliance Checks | Continuous verification of AI systems against defined policies |
| Incident Response Playbooks | AI-specific incident response procedures and escalation |
| Audit Logging | Comprehensive logging of all AI interactions for forensics |

### Tier 03: Validate & Adapt (Continuous Validation)

Continuous validation that evolves with the threat landscape.

| Control | Description |
|---------|-------------|
| Red Team Exercises | Adversarial testing of AI systems by internal or external teams |
| Model Behaviour Monitoring | Drift detection and behavioural anomaly identification |
| Threat Intelligence Integration | Feed AI-specific threat intel into defence posture |
| Feedback Loops | Continuous improvement cycles from security events and testing |
| Adaptive Control Refinement | Evolve controls based on new attack vectors and research |
| Cross-Org Benchmarking | Compare maturity and controls against peer organisations |

## Roadmap

| Period | Milestone | Deliverable | Status |
|--------|-----------|-------------|--------|
| Jan -- Feb 2026 | Board Charter & Scope | Charter + Scope | Complete |
| Feb -- Mar 2026 | Framework Design | Framework Draft 1 | In Progress |
| Apr -- May 2026 | Validation & Refinement | Framework Draft 2 | Upcoming |
| May -- Jun 2026 | Sign Off & Release | MVP 1.0 | Upcoming |

## How to Contribute

We are developing this framework in the open. Feedback from practitioners is essential.

- **Open an issue** with the `feedback` label to suggest changes
- **Submit a PR** for specific control refinements
- **Join the discussion** in [GitHub Discussions](https://github.com/orgs/aiseca/discussions)

See [CONTRIBUTING.md](https://github.com/aiseca/.github/blob/main/CONTRIBUTING.md) for guidelines.

## License

This framework is released under [CC BY 4.0](LICENSE). You are free to share and adapt it with attribution.

---

**AISECA** -- AI Security Alliance | [aiseca.org](https://aiseca.org) | [GitHub](https://github.com/aiseca)
