# Contributing to the AISECA Tiered Control Framework

v1.0 is released and v1.1 is in progress. Practitioner disagreement is the input we want most — it is what moves the framework between versions.

For general AISECA contribution guidance and the code of conduct, see the [org guidelines](https://github.com/aiseca/.github/blob/main/CONTRIBUTING.md).

## Where to put things

| You want to | Do this |
|---|---|
| Say a control is wrong or unworkable | [Open a challenge issue](../../issues/new?template=challenge-control.yml) |
| Add a risk we missed | [Open a proposal issue](../../issues/new?template=propose-control.yml) |
| Fix a mapping, citation, or dead link | [Open a mapping issue](../../issues/new?template=mapping-correction.yml) or send a PR |
| Rewrite control text | Send a PR |
| Argue about tiers, domains, or structure | [Org discussions](https://github.com/orgs/aiseca/discussions) |

You do not need to open an issue before sending a PR for a small fix.

## Editing controls

Each control is one Markdown file under `controls/<domain>/AISECA-<CODE>-<NNN>.md`. The YAML frontmatter holds the structured fields; the body holds the prose.

```bash
# after editing any control file
python3 scripts/build.py     # regenerates dist/ and the README index
```

Commit the regenerated files with your change. CI runs `python3 scripts/build.py --check` and fails if they are stale.

**Rules:**

- **One control per PR** where practical. Cross-cutting rewording across many files is fine as its own PR, but do not bundle it with a substantive change.
- **Control IDs are stable.** Never renumber, reuse, or reassign an ID. Withdrawn controls keep their ID and get marked withdrawn.
- **Do not edit `dist/`.** It is generated.
- **Tier discipline.** Tier 1 defines and constrains (policy, standards, boundaries). Tier 2 enforces and monitors (technical mechanism, detection, escalation). Tier 3 validates and adapts (adversarial testing, audit, feedback into the other two). If your addition to tier 1 describes a detection mechanism, it belongs in tier 2.
- **Scenarios should be real.** Prefer a documented public incident with a link. A plausible-but-invented scenario is acceptable only where no public case exists, and should read as illustrative.

## Tooling references

Every control carries two tooling lines, and they work differently:

- **Categories** names market tool categories (SCA, ASPM, AIDR, CIEM) so readers can map a control to the kind of product that addresses it. No vendors, by design.
- **Named tools are open source only.** Many are corporate-originated — Cedar, gVisor, Falco, GuardDog, Conjur — which is fine. The bar is the license, not the logo.

Keep it that way. To add a tool, it must:

- be open source, or an open standard or protocol (C2PA, A2A, CSP);
- directly implement the control at the tier it is listed under, rather than adjacently relating to it;
- be maintained, with meaningful activity in roughly the last 12 months;
- carry a link and a short parenthetical saying what it does for *this* control.

Closed-source and free-tier-gated products do not get named. Add the category instead.

**Disclose affiliation.** If you work for, are funded by, or advise a project you are adding, say so in the PR. Disclosed affiliation is fine and common. Undisclosed affiliation gets the PR closed.

Listing is descriptive, not an endorsement, and inclusion is not for sale.

## Review

Domain owners are listed in [CODEOWNERS](.github/CODEOWNERS) and are requested automatically. PRs need one approving review from a domain owner. Substantive changes — new controls, severity changes, tier reassignment — go to the AISECA board for consensus before merge, which takes longer than a wording fix.

## Licensing

Contributions are licensed under [CC BY 4.0](LICENSE), the same license as the framework. There is no CLA. By contributing you confirm you have the right to submit the work under that license, and that it is not confidential to your employer or a client.
