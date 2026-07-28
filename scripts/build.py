#!/usr/bin/env python3
"""Markdown controls -> dist/framework.json + dist/framework.csv.

The Markdown files under controls/ are the source of truth. This only derives
machine-readable copies for tooling. Run `python3 scripts/build.py --check` in
CI to fail when dist/ is stale.
"""
import csv, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
FIELDS = ["id", "title", "domain", "severity", "nist_ai_rmf", "mitre_atlas",
          "stakeholders", "references", "risk", "scenario", "tier1", "tier2", "tier3", "tooling"]


def parse_frontmatter(text):
    """Minimal YAML subset: scalars, inline [..] lists, and '- item' block lists."""
    fm = {}
    key = None
    for line in text.split("\n"):
        if line.startswith("  - ") and key:
            fm.setdefault(key, []).append(line[4:].strip())
            continue
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            fm[key] = [v.strip().strip('"') for v in re.findall(r'"[^"]*"|[^,\[\]]+', val[1:-1]) if v.strip()]
        elif val:
            fm[key] = val.strip('"').replace('\\"', '"')
        else:
            fm[key] = []
    return fm


def section(body, heading):
    m = re.search(rf"^## {re.escape(heading)}.*?$\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""


def load():
    controls = []
    for path in sorted((ROOT / "controls").rglob("AISECA-*.md")):
        raw = path.read_text()
        _, fm_raw, body = raw.split("---", 2)
        fm = parse_frontmatter(fm_raw)
        risk = re.search(r"\*\*Risk\.\*\*\s*(.*?)\n", body)
        scen = re.search(r"\*\*Scenario\.\*\*\s*(.*?)\n", body)
        controls.append({
            **{k: fm.get(k, "") for k in ("id", "title", "domain", "severity", "mitre_atlas")},
            "nist_ai_rmf": fm.get("nist_ai_rmf", []),
            "stakeholders": fm.get("stakeholders", []),
            "references": fm.get("references", []),
            "risk": risk.group(1).strip() if risk else "",
            "scenario": scen.group(1).strip() if scen else "",
            "tier1": section(body, "Tier 1"),
            "tier2": section(body, "Tier 2"),
            "tier3": section(body, "Tier 3"),
            "tooling": section(body, "Tooling landscape"),
            "path": str(path.relative_to(ROOT)),
        })
    return controls


def render(controls):
    js = json.dumps(controls, indent=2, ensure_ascii=False) + "\n"
    rows = []
    for c in controls:
        rows.append({k: "; ".join(c[k]) if isinstance(c[k], list) else c[k] for k in FIELDS})
    import io
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return js, buf.getvalue()


def index_table(controls):
    """Markdown index, grouped by domain, injected into README between markers."""
    out, domain = [], None
    for c in controls:
        if c["domain"] != domain:
            domain = c["domain"]
            out += [f"\n### {domain}\n", "| ID | Risk | Severity |", "|---|---|---|"]
        out.append(f'| [{c["id"]}]({c["path"]}) | {c["title"]} | {c["severity"]} |')
    return "\n".join(out).strip()


def inject_index(controls):
    readme = ROOT / "README.md"
    text = readme.read_text()
    new, n = re.subn(r"(<!-- INDEX:START -->)(.*?)(<!-- INDEX:END -->)",
                     lambda m: f"{m.group(1)}\n{index_table(controls)}\n{m.group(3)}", text, flags=re.S)
    assert n == 1, f"README.md needs exactly one INDEX:START/INDEX:END marker pair (found {n})"
    return readme, text, new


def main():
    controls = load()
    assert controls, "no controls found under controls/"
    ids = [c["id"] for c in controls]
    dupes = {i for i in ids if ids.count(i) > 1}
    assert not dupes, f"duplicate control ids: {dupes}"
    for c in controls:
        for tier in ("tier1", "tier2", "tier3"):
            assert c[tier], f"{c['id']} is missing {tier}"

    js, csv_text = render(controls)
    readme, old_readme, new_readme = inject_index(controls)

    if "--check" in sys.argv:
        stale = [p.name for p, want in ((DIST / "framework.json", js), (DIST / "framework.csv", csv_text),
                                        (readme, new_readme)) if not p.exists() or p.read_text() != want]
        if stale:
            sys.exit(f"generated files are stale: {', '.join(stale)}. Run: python3 scripts/build.py")
        print(f"OK — {len(controls)} controls, generated files in sync")
        return

    DIST.mkdir(exist_ok=True)
    (DIST / "framework.json").write_text(js)
    (DIST / "framework.csv").write_text(csv_text)
    readme.write_text(new_readme)
    print(f"wrote dist/framework.json, dist/framework.csv, README index ({len(controls)} controls)")


if __name__ == "__main__":
    main()
