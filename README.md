# AISECA Tiered Control Framework

A practitioner-led, vendor-agnostic control framework for securing enterprise AI. Each risk is mapped to a NIST AI 600-1 GenAI risk domain and to MITRE ATLAS where a technique applies, then answered with three tiers of control: define it, enforce it, validate it.

**Version:** 1.0 · **Controls:** 57 across 12 risk domains · **License:** [CC BY 4.0](LICENSE)

> v1.0 is a released version of the framework. v1.1 is in progress — practitioner feedback is what shapes it, and disagreement is the point. See [Giving feedback](#giving-feedback).

---

## The three tiers

| Tier | Name | What it means |
|---|---|---|
| **1** | Define & Constrain | Policy, boundaries, and standards. What is allowed, what is prohibited, who owns it. |
| **2** | Enforce & Monitor | Technical enforcement of tier 1. Detection, logging, blocking, escalation. |
| **3** | Validate & Adapt | Adversarial testing and continuous evidence that tiers 1 and 2 actually hold. |

A tier is not a maturity badge you graduate from. Tier 3 without tier 1 is theatre; tier 1 without tier 2 is a PDF.

## How to read a control

Every control is one file under [`controls/`](controls/), named by its stable ID. Structured fields live in the YAML frontmatter (domain, severity, NIST AI RMF subcategories, MITRE ATLAS mapping, stakeholder, references); the prose body carries the risk, a real-world scenario, the three tiers, and the tooling landscape.

IDs are stable. Once assigned, a control ID is never reused or renumbered, even if the control is withdrawn.

## Machine-readable

[`dist/framework.json`](dist/framework.json) and [`dist/framework.csv`](dist/framework.csv) are generated from the Markdown by [`scripts/build.py`](scripts/build.py). Do not edit them directly — edit the control file and re-run the build. CI enforces this.

```bash
python3 scripts/build.py          # regenerate
python3 scripts/build.py --check  # verify in sync (what CI runs)
```

## Giving feedback

We would rather have an argument than a citation. Three ways in, in order of usefulness:

1. **Open an issue** — [challenge a control](../../issues/new?template=challenge-control.yml), [propose a new one](../../issues/new?template=propose-control.yml), or [fix a mapping](../../issues/new?template=mapping-correction.yml). The forms ask which control ID and what your operational experience was.
2. **Open a pull request** — edit the control file directly. One control per PR keeps review tractable. See [CONTRIBUTING.md](CONTRIBUTING.md).
3. **Start a discussion** — [org discussions](https://github.com/orgs/aiseca/discussions) for anything broader than one control: tier boundaries, domain coverage, framework structure.

If you have implemented one of these controls in production and it did not work as written, that is the single most valuable contribution you can make.

### On tooling references

Named tools are open source only — many corporate-originated, none proprietary. Commercial options appear as market categories (SCA, ASPM, AIDR), never as named products. Listing is descriptive, not an endorsement. See [CONTRIBUTING.md](CONTRIBUTING.md#tooling-references) for the bar.

## Risk domains

Domains follow [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) (Generative AI Profile).

<!-- INDEX:START -->
### CBRN (Chemical, Biological, Radiological, Nuclear)

| ID | Risk | Severity |
|---|---|---|
| [AISECA-CBRN-001](controls/cbrn/AISECA-CBRN-001.md) | CBRN knowledge enablement | Medium |
| [AISECA-CBRN-002](controls/cbrn/AISECA-CBRN-002.md) | Dual-use misuse | Medium |

### Confabulation (Hallucinations)

| ID | Risk | Severity |
|---|---|---|
| [AISECA-CONF-001](controls/confabulation/AISECA-CONF-001.md) | Hallucinated outputs | Medium |
| [AISECA-CONF-002](controls/confabulation/AISECA-CONF-002.md) | Incorrect citations or fabricated sources / information | Medium |

### Dangerous, Violent, or Hateful Content

| ID | Risk | Severity |
|---|---|---|
| [AISECA-DVH-001](controls/dangerous-violent-hateful-content/AISECA-DVH-001.md) | Violence facilitation | Medium |
| [AISECA-DVH-002](controls/dangerous-violent-hateful-content/AISECA-DVH-002.md) | Extremist or hateful outputs | High |

### Data Privacy

| ID | Risk | Severity |
|---|---|---|
| [AISECA-PRIV-001](controls/data-privacy/AISECA-PRIV-001.md) | Prompt-based data leakage | High |
| [AISECA-PRIV-002](controls/data-privacy/AISECA-PRIV-002.md) | Sensitive data retention | High |
| [AISECA-PRIV-003](controls/data-privacy/AISECA-PRIV-003.md) | Context Injection via Tools or MCP | High |
| [AISECA-PRIV-004](controls/data-privacy/AISECA-PRIV-004.md) | Re-identification risk | High |
| [AISECA-PRIV-005](controls/data-privacy/AISECA-PRIV-005.md) | Unauthorized training data use | High |
| [AISECA-PRIV-006](controls/data-privacy/AISECA-PRIV-006.md) | Markdown Rendering Exfiltration | Medium |

### Environmental Impacts (energy usage, carbon footprint, resource consumption)

| ID | Risk | Severity |
|---|---|---|
| [AISECA-ENV-001](controls/environmental-impacts/AISECA-ENV-001.md) | Excessive compute consumption | Low |
| [AISECA-ENV-002](controls/environmental-impacts/AISECA-ENV-002.md) | Inefficient inference or training | Low |

### Harmful Bias & Homogenization

| ID | Risk | Severity |
|---|---|---|
| [AISECA-BIAS-001](controls/harmful-bias-homogenization/AISECA-BIAS-001.md) | Discriminatory outputs | Medium |
| [AISECA-BIAS-002](controls/harmful-bias-homogenization/AISECA-BIAS-002.md) | Exclusionary recommendations | Medium |
| [AISECA-BIAS-003](controls/harmful-bias-homogenization/AISECA-BIAS-003.md) | Loss of diversity / homogenized outputs | Medium |

### Human–AI Configuration & Overreliance

| ID | Risk | Severity |
|---|---|---|
| [AISECA-HAIC-001](controls/human-ai-configuration-overreliance/AISECA-HAIC-001.md) | Automation bias | Medium |
| [AISECA-HAIC-002](controls/human-ai-configuration-overreliance/AISECA-HAIC-002.md) | Unsafe agent autonomy | High |
| [AISECA-HAIC-003](controls/human-ai-configuration-overreliance/AISECA-HAIC-003.md) | Invisible Agent Decision-Making | High |
| [AISECA-HAIC-004](controls/human-ai-configuration-overreliance/AISECA-HAIC-004.md) | Agent continues execution loops beyond intended bounds or stop conditions | Medium |
| [AISECA-HAIC-005](controls/human-ai-configuration-overreliance/AISECA-HAIC-005.md) | Unbounded Resource Consumption by Agents | Medium |
| [AISECA-HAIC-006](controls/human-ai-configuration-overreliance/AISECA-HAIC-006.md) | Uncontrolled Agent Delegation Chains | Medium |
| [AISECA-HAIC-007](controls/human-ai-configuration-overreliance/AISECA-HAIC-007.md) | Delegation without accountability | Medium |

### Information Integrity

| ID | Risk | Severity |
|---|---|---|
| [AISECA-INTG-001](controls/information-integrity/AISECA-INTG-001.md) | Misinformation propagation | Medium |
| [AISECA-INTG-002](controls/information-integrity/AISECA-INTG-002.md) | Output manipulation | Medium |
| [AISECA-INTG-003](controls/information-integrity/AISECA-INTG-003.md) | Lack of provenance | Medium |

### Information Security

| ID | Risk | Severity |
|---|---|---|
| [AISECA-INFOSEC-001](controls/information-security/AISECA-INFOSEC-001.md) | Loss of identity attribution | Medium |
| [AISECA-INFOSEC-002](controls/information-security/AISECA-INFOSEC-002.md) | Compromised AI credentials | High |
| [AISECA-INFOSEC-003](controls/information-security/AISECA-INFOSEC-003.md) | Over-privileged AI identities | High |
| [AISECA-INFOSEC-004](controls/information-security/AISECA-INFOSEC-004.md) | Agent action exceeds authority delegated by initiating identity | Medium |
| [AISECA-INFOSEC-005](controls/information-security/AISECA-INFOSEC-005.md) | Cross-Agent Impersonation | High |
| [AISECA-INFOSEC-006](controls/information-security/AISECA-INFOSEC-006.md) | Untrusted MCP servers or tools gaining implicit trust | High |
| [AISECA-INFOSEC-007](controls/information-security/AISECA-INFOSEC-007.md) | Prompt & instruction manipulation | High |
| [AISECA-INFOSEC-008](controls/information-security/AISECA-INFOSEC-008.md) | Model extraction or abuse | High |
| [AISECA-INFOSEC-009](controls/information-security/AISECA-INFOSEC-009.md) | Indirect Prompt Injection | High |
| [AISECA-INFOSEC-010](controls/information-security/AISECA-INFOSEC-010.md) | Loss of initiating identity through multi-agent workflows | Medium |
| [AISECA-INFOSEC-011](controls/information-security/AISECA-INFOSEC-011.md) | Training data poisoning | High |
| [AISECA-INFOSEC-012](controls/information-security/AISECA-INFOSEC-012.md) | Initialization Race Conditions | High |
| [AISECA-INFOSEC-013](controls/information-security/AISECA-INFOSEC-013.md) | Sandbox Self-Escalation | High |
| [AISECA-INFOSEC-014](controls/information-security/AISECA-INFOSEC-014.md) | Ambient Authority Exploitation | High |
| [AISECA-INFOSEC-015](controls/information-security/AISECA-INFOSEC-015.md) | Recursive Prompt Injection (LLM-as-a-Judge) | High |
| [AISECA-INFOSEC-016](controls/information-security/AISECA-INFOSEC-016.md) | Multimodal Injection | High |
| [AISECA-INFOSEC-017](controls/information-security/AISECA-INFOSEC-017.md) | Semantic Context Shifting | Medium |
| [AISECA-INFOSEC-018](controls/information-security/AISECA-INFOSEC-018.md) | Abuse of Legitimate Agency | High |
| [AISECA-INFOSEC-019](controls/information-security/AISECA-INFOSEC-019.md) | Public Discovery of Internal AI Middleware | Medium |

### Intellectual Property

| ID | Risk | Severity |
|---|---|---|
| [AISECA-IP-001](controls/intellectual-property/AISECA-IP-001.md) | Proprietary data leakage | High |
| [AISECA-IP-002](controls/intellectual-property/AISECA-IP-002.md) | Copyright infringement | Medium |
| [AISECA-IP-003](controls/intellectual-property/AISECA-IP-003.md) | Model inversion | High |

### Obscene, Degrading, or Abusive Content

| ID | Risk | Severity |
|---|---|---|
| [AISECA-ODA-001](controls/obscene-degrading-abusive-content/AISECA-ODA-001.md) | Sexually explicit outputs | Low |
| [AISECA-ODA-002](controls/obscene-degrading-abusive-content/AISECA-ODA-002.md) | Harassment or abuse | Medium |

### Value Chain & Component Integration

| ID | Risk | Severity |
|---|---|---|
| [AISECA-VC-001](controls/value-chain-component-integration/AISECA-VC-001.md) | Third-party model risk | High |
| [AISECA-VC-002](controls/value-chain-component-integration/AISECA-VC-002.md) | Uncontrolled model updates | High |
| [AISECA-VC-003](controls/value-chain-component-integration/AISECA-VC-003.md) | Security weaknesses inherited from orchestration frameworks or SDKs | High |
| [AISECA-VC-004](controls/value-chain-component-integration/AISECA-VC-004.md) | Compromised, Untrusted, or Malicious Agent Tool Ecosystem | High |
| [AISECA-VC-005](controls/value-chain-component-integration/AISECA-VC-005.md) | Insecure plugins or tools | High |
| [AISECA-VC-006](controls/value-chain-component-integration/AISECA-VC-006.md) | Dependency "Cool-down" Violations | Medium |
<!-- INDEX:END -->

---

**AISECA** — AI Security Alliance · [aiseca.org](https://aiseca.org) · [GitHub](https://github.com/aiseca)
