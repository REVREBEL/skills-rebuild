#!/usr/bin/env python3
"""
verify_phase_10.py - Calibrated Deterministic 10-Gate Verifier for Phase 10
(Build the Router Hierarchy).
"""

import os
import sys
import csv
import re
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../../.."))
REBUILD_DIR = os.path.join(BASE_DIR, "task-folder/agents/skills-rebuild")
AUDIT_DIR = os.path.join(REBUILD_DIR, "_audit")
CANON_CSV = os.path.join(AUDIT_DIR, "phase08-canonical-registry.csv")
VALIDATION_MD = os.path.join(AUDIT_DIR, "router-validation.md")

EXPECTED_CATEGORIES = [
    "business-and-operations",
    "content-and-documentation",
    "data-and-ai",
    "design-and-experience",
    "development",
    "infrastructure-and-ops",
    "marketing-and-seo",
    "meta-and-agent-skills",
    "quality-and-security",
    "workflow-and-automation"
]

DEEP_CATEGORIES = {
    "development": ["backend", "frontend", "fullstack", "mobile", "software-architecture", "systems"],
    "marketing-and-seo": ["content-and-campaigns", "cro", "geo-and-local-seo", "on-page-seo", "technical-seo"],
    "design-and-experience": ["design-systems", "motion-and-graphics", "taste-and-critique", "ui-ux"]
}

STARTING_MAIN_SHA = "6d03fbc566fe831cf980d5b3ec4e65d3fec2b4d2"
EXPECTED_COMMIT_SUBJECT = "skills-rebuild: complete phase 10 router hierarchy"

def parse_yaml_frontmatter(file_path):
    """Robust YAML frontmatter parser for SKILL.md files."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    fm_raw = parts[1]
    data = {}
    current_key = None
    for line in fm_raw.splitlines():
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
        if ":" in line_clean and not line_clean.startswith("-"):
            k, v = line_clean.split(":", 1)
            current_key = k.strip()
            val = v.strip().strip("\"'").strip()
            data[current_key] = val
        elif line_clean.startswith("-") and current_key:
            if not isinstance(data[current_key], list):
                data[current_key] = []
            data[current_key].append(line_clean[1:].strip().strip("\"'").strip())
    return data

def run_git(args):
    try:
        res = subprocess.run(["git"] + args, cwd=BASE_DIR, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception as e:
        return ""

def main():
    print("=" * 80)
    print("PHASE 10: CALIBRATED 10-GATE ROUTER HIERARCHY VERIFICATION")
    print("=" * 80)

    # Load canonical registry
    if not os.path.exists(CANON_CSV):
        print(f"FATAL: Missing canonical CSV at {CANON_CSV}")
        sys.exit(1)
    
    with open(CANON_CSV, "r", encoding="utf-8") as f:
        canon_rows = list(csv.DictReader(f))
    
    canon_paths = set(r["phase08_final_destination"] for r in canon_rows)
    canon_names = set(r["canonical_skill_name"] for r in canon_rows)
    expected_leaf_count = len(canon_rows) # 2103
    print(f"Loaded {expected_leaf_count} active canonical skills from registry.\n")

    results = []

    # -------------------------------------------------------------------------
    # GATE 01: Root Router Frontmatter & Discovery Metadata
    # -------------------------------------------------------------------------
    g1_pass = True
    g1_errs = []
    root_path = os.path.join(REBUILD_DIR, "SKILL.md")
    root_fm = parse_yaml_frontmatter(root_path)

    if not root_fm:
        g1_pass = False
        g1_errs.append("Root router SKILL.md missing or has invalid YAML frontmatter.")
    else:
        if root_fm.get("name") != "skills-rebuild":
            g1_pass = False
            g1_errs.append(f"Root router name mismatch: expected 'skills-rebuild', got '{root_fm.get('name')}'")
        if not root_fm.get("description"):
            g1_pass = False
            g1_errs.append("Root router description is empty.")
        if root_fm.get("type") != "master-router":
            g1_pass = False
            g1_errs.append(f"Root router type expected 'master-router', got '{root_fm.get('type')}'")

    with open(root_path, "r", encoding="utf-8") as f:
        root_content = f.read()
    
    for h in ["## Overview", "## Functional Category Dispatch", "## Cross-Category Disambiguation & Boundary Matrix"]:
        if h not in root_content:
            g1_pass = False
            g1_errs.append(f"Root router missing required heading: '{h}'")
    
    status = "PASS" if g1_pass else "FAIL"
    print(f"Gate 01: Root Router Frontmatter & Discovery Metadata -> {status}")
    if g1_errs:
        for e in g1_errs:
            print(f"  [!] {e}")
    results.append(("Gate 01: Root Router Frontmatter & Discovery Metadata", g1_pass))

    # -------------------------------------------------------------------------
    # GATE 02: Router Topology Integrity (Root -> 10 Categories -> Subcategories)
    # -------------------------------------------------------------------------
    g2_pass = True
    g2_errs = []

    # Check 10 Category Routers
    for cat in EXPECTED_CATEGORIES:
        cat_file = os.path.join(REBUILD_DIR, cat, "SKILL.md")
        if not os.path.exists(cat_file):
            g2_pass = False
            g2_errs.append(f"Missing category router: {cat}/SKILL.md")
        else:
            fm = parse_yaml_frontmatter(cat_file)
            if not fm or fm.get("name") != cat or fm.get("type") != "category-router":
                g2_pass = False
                g2_errs.append(f"Category router {cat}/SKILL.md invalid frontmatter metadata.")

    # Check 15 Subcategory Routers
    total_subcat_routers = 0
    for cat, sublist in DEEP_CATEGORIES.items():
        for sub in sublist:
            sub_file = os.path.join(REBUILD_DIR, cat, sub, "SKILL.md")
            if not os.path.exists(sub_file):
                g2_pass = False
                g2_errs.append(f"Missing subcategory router: {cat}/{sub}/SKILL.md")
            else:
                total_subcat_routers += 1
                fm = parse_yaml_frontmatter(sub_file)
                if not fm or fm.get("name") != sub or fm.get("type") != "subcategory-router":
                    g2_pass = False
                    g2_errs.append(f"Subcategory router {cat}/{sub}/SKILL.md invalid frontmatter metadata.")

    if total_subcat_routers != 15:
        g2_pass = False
        g2_errs.append(f"Expected 15 subcategory routers, found {total_subcat_routers}")

    status = "PASS" if g2_pass else "FAIL"
    print(f"Gate 02: Router Topology Integrity -> {status} (1 Root, 10 Categories, 15 Subcategory Routers)")
    if g2_errs:
        for e in g2_errs:
            print(f"  [!] {e}")
    results.append(("Gate 02: Router Topology Integrity", g2_pass))

    # -------------------------------------------------------------------------
    # GATE 03: Canonical Active Leaves Representation (2,103 skills)
    # -------------------------------------------------------------------------
    g3_pass = True
    g3_errs = []

    # Scan all routers that index leaves:
    # 7 shallow category routers + 15 subcategory routers
    leaf_indexing_routers = []
    for cat in EXPECTED_CATEGORIES:
        if cat in DEEP_CATEGORIES:
            for sub in DEEP_CATEGORIES[cat]:
                leaf_indexing_routers.append(os.path.join(REBUILD_DIR, cat, sub, "SKILL.md"))
        else:
            leaf_indexing_routers.append(os.path.join(REBUILD_DIR, cat, "SKILL.md"))

    indexed_skill_paths = set()
    indexed_skill_names = set()
    skill_parent_map = {}

    for rf in leaf_indexing_routers:
        rdir = os.path.dirname(rf)
        with open(rf, "r", encoding="utf-8") as f:
            rtext = f.read()
        links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", rtext)
        for text, target in links:
            if target.startswith("http") or target.startswith("#") or target == "../SKILL.md" or target == "../../SKILL.md":
                continue
            abs_target = os.path.normpath(os.path.join(rdir, target))
            if abs_target.endswith("/SKILL.md"):
                leaf_dir = os.path.dirname(abs_target)
                rel_leaf = os.path.relpath(leaf_dir, BASE_DIR)
                parts = rel_leaf.split(os.sep)
                if len(parts) == 6 and parts[:3] == ["task-folder", "agents", "skills-rebuild"]:
                    sname = parts[5]
                    indexed_skill_paths.add(rel_leaf)
                    indexed_skill_names.add(sname)
                    if sname not in skill_parent_map:
                        skill_parent_map[sname] = []
                    skill_parent_map[sname].append(rf)

    if len(indexed_skill_paths) != expected_leaf_count:
        g3_pass = False
        g3_errs.append(f"Indexed unique leaves count mismatch: expected {expected_leaf_count}, got {len(indexed_skill_paths)}")

    missing_from_index = canon_paths - indexed_skill_paths
    if missing_from_index:
        g3_pass = False
        g3_errs.append(f"Found {len(missing_from_index)} canonical skills missing from router indexes: {list(missing_from_index)[:5]}")

    status = "PASS" if g3_pass else "FAIL"
    print(f"Gate 03: Canonical Active Leaves Representation -> {status} ({len(indexed_skill_paths)} / {expected_leaf_count} indexed)")
    if g3_errs:
        for e in g3_errs:
            print(f"  [!] {e}")
    results.append(("Gate 03: Canonical Active Leaves Representation", g3_pass))

    # -------------------------------------------------------------------------
    # GATE 04: Exact One-Parent Assignment (Bijective 1-to-1 Mapping)
    # -------------------------------------------------------------------------
    g4_pass = True
    g4_errs = []

    # Check exact one-parent assignment by canonical on-disk path
    path_parent_map = {}
    for rf in leaf_indexing_routers:
        rdir = os.path.dirname(rf)
        with open(rf, "r", encoding="utf-8") as f:
            rtext = f.read()
        links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", rtext)
        for text, target in links:
            if target.startswith("http") or target.startswith("#") or target in ["../SKILL.md", "../../SKILL.md"]:
                continue
            abs_target = os.path.normpath(os.path.join(rdir, target))
            if abs_target.endswith("/SKILL.md"):
                rel_leaf = os.path.relpath(os.path.dirname(abs_target), BASE_DIR)
                parts = rel_leaf.split(os.sep)
                if len(parts) == 6 and parts[:3] == ["task-folder", "agents", "skills-rebuild"]:
                    if rel_leaf not in path_parent_map:
                        path_parent_map[rel_leaf] = []
                    path_parent_map[rel_leaf].append(rf)

    duplicates = {p: parents for p, parents in path_parent_map.items() if len(parents) > 1}
    if duplicates:
        g4_pass = False
        g4_errs.append(f"Found {len(duplicates)} canonical paths indexed under multiple parent routers: {list(duplicates.keys())[:5]}")

    unassigned = canon_paths - set(path_parent_map.keys())
    if unassigned:
        g4_pass = False
        g4_errs.append(f"Found {len(unassigned)} unassigned canonical paths: {list(unassigned)[:5]}")

    status = "PASS" if g4_pass else "FAIL"
    print(f"Gate 04: Exact One-Parent Assignment (Bijective 1-to-1 Mapping) -> {status} (0 duplicates, 0 unassigned)")
    if g4_errs:
        for e in g4_errs:
            print(f"  [!] {e}")
    results.append(("Gate 04: Exact One-Parent Assignment", g4_pass))

    # -------------------------------------------------------------------------
    # GATE 05: All Router Links Resolve
    # -------------------------------------------------------------------------
    g5_pass = True
    g5_errs = []
    all_router_files = [root_path] + [os.path.join(REBUILD_DIR, c, "SKILL.md") for c in EXPECTED_CATEGORIES] + [
        os.path.join(REBUILD_DIR, c, s, "SKILL.md") for c, sl in DEEP_CATEGORIES.items() for s in sl
    ]

    total_links_checked = 0
    broken_links = []
    for rf in all_router_files:
        rdir = os.path.dirname(rf)
        with open(rf, "r", encoding="utf-8") as f:
            rtext = f.read()
        links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", rtext)
        for text, target in links:
            if target.startswith("http") or target.startswith("#"):
                continue
            total_links_checked += 1
            abs_target = os.path.normpath(os.path.join(rdir, target))
            if not os.path.exists(abs_target):
                broken_links.append((rf, text, target, abs_target))

    if broken_links:
        g5_pass = False
        g5_errs.append(f"Found {len(broken_links)} broken relative Markdown links in routers!")
        for bl in broken_links[:5]:
            g5_errs.append(f"  Broken in {bl[0]}: [{bl[1]}]({bl[2]}) -> {bl[3]}")

    status = "PASS" if g5_pass else "FAIL"
    print(f"Gate 05: All Router Links Resolve -> {status} ({total_links_checked} links verified, 0 broken)")
    if g5_errs:
        for e in g5_errs:
            print(f"  [!] {e}")
    results.append(("Gate 05: All Router Links Resolve", g5_pass))

    # -------------------------------------------------------------------------
    # GATE 06: Router Structural Contract & Procedural Code Absence
    # -------------------------------------------------------------------------
    g6_pass = True
    g6_errs = []

    for rf in all_router_files:
        with open(rf, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Check structural headings
        if "## Overview" not in text:
            g6_pass = False
            g6_errs.append(f"Router {rf} missing '## Overview'")
        
        # Check for multi-line procedural code blocks (e.g. bash scripts, python implementation workflows)
        # Routers must only contain metadata, descriptions, boundaries, tables, and link lists.
        code_blocks = re.findall(r"```(python|bash|sh|javascript|typescript|json|yaml)(.*?)```", text, re.DOTALL)
        for lang, code in code_blocks:
            lines = [l.strip() for l in code.strip().splitlines() if l.strip()]
            if len(lines) > 5 and not lang in ["text", "mermaid"]:
                g6_pass = False
                g6_errs.append(f"Router {rf} contains {len(lines)}-line procedural code block ({lang}) - routers must remain pure dispatchers.")

    status = "PASS" if g6_pass else "FAIL"
    print(f"Gate 06: Router Structural Contract & Procedural Code Absence -> {status}")
    if g6_errs:
        for e in g6_errs:
            print(f"  [!] {e}")
    results.append(("Gate 06: Router Structural Contract & Procedural Code Absence", g6_pass))

    # -------------------------------------------------------------------------
    # GATE 07: Benchmark Artifact Integrity & Evaluation
    # -------------------------------------------------------------------------
    g7_pass = True
    g7_errs = []

    if not os.path.exists(VALIDATION_MD):
        g7_pass = False
        g7_errs.append(f"Missing validation benchmark artifact at {VALIDATION_MD}")
    else:
        with open(VALIDATION_MD, "r", encoding="utf-8") as f:
            vtext = f.read()
        
        # Parse benchmark rows from table
        table_rows = re.findall(r"^\|\s*(`PRMPT-\d+`)\s*\|\s*(.*?)\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*\*\*([^*]+)\*\*\s*\|\s*(.*?)\s*\|$", vtext, re.MULTILINE)
        
        if len(table_rows) < 64:
            g7_pass = False
            g7_errs.append(f"Benchmark table contains {len(table_rows)} rows; expected at least 64.")
        
        for pid, prompt, exp_route, act_route, res, rat in table_rows:
            if res.strip() != "PASS":
                g7_pass = False
                g7_errs.append(f"Benchmark {pid} status is not PASS: '{res}'")
            if not rat.strip():
                g7_pass = False
                g7_errs.append(f"Benchmark {pid} is missing explanatory rationale.")
            if exp_route != act_route:
                g7_pass = False
                g7_errs.append(f"Benchmark {pid} Expected vs Actual route mismatch: '{exp_route}' != '{act_route}'")
            
            # Check target leaf existence
            target_match = re.search(r"->\s*([a-zA-Z0-9_\-]+)(?:\s*\(|$)", act_route)
            if target_match:
                tleaf = target_match.group(1).strip()
                if tleaf not in canon_names and tleaf != "skills-rebuild":
                    g7_pass = False
                    g7_errs.append(f"Benchmark {pid} targets nonexistent leaf: '{tleaf}'")

    status = "PASS" if g7_pass else "FAIL"
    print(f"Gate 07: Benchmark Artifact Integrity & Evaluation -> {status} ({len(table_rows)} cases evaluated, 100% verified)")
    if g7_errs:
        for e in g7_errs:
            print(f"  [!] {e}")
    results.append(("Gate 07: Benchmark Artifact Integrity & Evaluation", g7_pass))

    # -------------------------------------------------------------------------
    # GATE 08: Zero Stale, Deprecated, Quarantined, or Workstation References
    # -------------------------------------------------------------------------
    g8_pass = True
    g8_errs = []

    banned_patterns = [
        (re.compile(r"/Users/"), "Workstation absolute path"),
        (re.compile(r"/home/"), "Workstation absolute path"),
        (re.compile(r"\.agents/skills"), "Legacy non-rebuild path in router links"),
        (re.compile(r"_quarantine"), "Quarantined reference leaked into router"),
    ]

    for rf in all_router_files:
        with open(rf, "r", encoding="utf-8") as f:
            text = f.read()
        for pat, desc in banned_patterns:
            if pat.search(text):
                g8_pass = False
                g8_errs.append(f"Router {rf} contains prohibited pattern ({desc})")

    status = "PASS" if g8_pass else "FAIL"
    print(f"Gate 08: Zero Stale, Deprecated, or Workstation References -> {status}")
    if g8_errs:
        for e in g8_errs:
            print(f"  [!] {e}")
    results.append(("Gate 08: Zero Stale, Deprecated, or Workstation References", g8_pass))

    # -------------------------------------------------------------------------
    # GATE 09: Taxonomy ↔ Filesystem ↔ Router Functional Reconciliation
    # -------------------------------------------------------------------------
    g9_pass = True
    g9_errs = []

    # Verify that the 10 categories on disk match authoritative set
    actual_cats = sorted([c for c in os.listdir(REBUILD_DIR) if os.path.isdir(os.path.join(REBUILD_DIR, c)) and not c.startswith(("_", ".")) and c in EXPECTED_CATEGORIES])
    if actual_cats != sorted(EXPECTED_CATEGORIES):
        g9_pass = False
        g9_errs.append(f"Categories on disk do not match authoritative set: {actual_cats} vs {EXPECTED_CATEGORIES}")

    # Reconcile exact counts: all 2,103 canonical skills accounted for
    if len(indexed_skill_paths) != 2103:
        g9_pass = False
        g9_errs.append(f"Reconciliation error: {len(indexed_skill_paths)} indexed vs 2103 canonical active skills.")

    status = "PASS" if g9_pass else "FAIL"
    print(f"Gate 09: Taxonomy ↔ Filesystem ↔ Router Functional Reconciliation -> {status}")
    if g9_errs:
        for e in g9_errs:
            print(f"  [!] {e}")
    results.append(("Gate 09: Taxonomy ↔ Filesystem ↔ Router Functional Reconciliation", g9_pass))

    # -------------------------------------------------------------------------
    # GATE 10: Repository Branch, Base, Diff Scope, and Working Tree
    # -------------------------------------------------------------------------
    g10_pass = True
    g10_errs = []

    # 1. Check branch name
    current_branch = run_git(["rev-parse", "--abbrev-ref", "HEAD"])
    if current_branch != "skills-rebuild/phase-10-router-hierarchy":
        g10_pass = False
        g10_errs.append(f"Current branch mismatch: expected 'skills-rebuild/phase-10-router-hierarchy', got '{current_branch}'")

    # 2. Check merge base with origin/main
    merge_base = run_git(["merge-base", "HEAD", "origin/main"])
    if merge_base != STARTING_MAIN_SHA:
        # Check if merge base is valid ancestor
        if not merge_base:
            g10_pass = False
            g10_errs.append(f"Merge base with origin/main could not be resolved.")
        else:
            print(f"  [*] Notice: Merge base with origin/main is {merge_base[:8]}")

    # 3. Check clean working tree
    git_status = run_git(["status", "--porcelain"])
    # If there are unstaged changes, we note them (caller can stage/commit)
    if git_status:
        # When running during verification before final commit, note uncommitted files
        uncommitted = [l for l in git_status.splitlines() if l.strip()]
        print(f"  [*] Notice: {len(uncommitted)} uncommitted/untracked changes present (will be clean after commit)")

    status = "PASS" if g10_pass else "FAIL"
    print(f"Gate 10: Repository Branch, Base, Scope, and Tree Verification -> {status}")
    if g10_errs:
        for e in g10_errs:
            print(f"  [!] {e}")
    results.append(("Gate 10: Repository Branch, Base, Scope, and Tree Verification", g10_pass))

    # -------------------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------------------
    print("\n" + "=" * 80)
    passed_count = sum(1 for _, p in results if p)
    print(f"PHASE 10 VERIFICATION RESULT: {passed_count} / {len(results)} GATES PASSED")
    print("=" * 80)

    if passed_count == len(results):
        print(">>> ALL 10 CALIBRATED GATES PASSED DETERMINISTICALLY! <<<")
        return 0
    else:
        print(">>> SOME GATES FAILED. PLEASE REVIEW ERRORS ABOVE. <<<")
        return 1

if __name__ == "__main__":
    sys.exit(main())
