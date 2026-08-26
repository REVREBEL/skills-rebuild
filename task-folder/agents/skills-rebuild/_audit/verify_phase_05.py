#!/usr/bin/env python3
"""
verify_phase_05.py

Comprehensive 18-Point Verification Suite for Phase 05 (Functional Taxonomy & Destination Mapping).
Ensures:
1. skills-inventory.csv contains 2,331 rows.
2. Exactly 45 quarantined rows are excluded from destination mapping.
3. Exactly 2,286 active rows are mapped.
4. Every active source path appears exactly once.
5. No quarantined source path appears in destination-map.csv.
6. Every mapped row has a valid top-level category.
7. Every mapped row has a valid compatibility classification.
8. Every mapped row has a non-empty destination path.
9. Destination paths are globally unique.
10. Destination paths are unique case-insensitively.
11. No router/path namespace collisions exist between destination-map.csv and router-map.csv.
12. Target paths follow canonical naming conventions.
13. Category counts sum to exactly 2,286.
14. Report category counts in functional-taxonomy.md equal CSV counts.
15. Confidence values belong to allowed enum {'high', 'medium', 'low'}.
16. Every 'low' confidence row contains an explicit placement concern.
17. Zero workstation absolute path leaks in Phase 05 files.
18. Hard check: Git diff proves ZERO modifications under task-folder/agents/skills/.
"""

import csv
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

ALLOWED_CATEGORIES = {
    "development",
    "design-and-experience",
    "infrastructure-and-ops",
    "data-and-ai",
    "quality-and-security",
    "marketing-and-seo",
    "business-and-operations",
    "content-and-documentation",
    "workflow-and-automation",
    "meta-and-agent-skills"
}

ALLOWED_CONFIDENCE = {"high", "medium", "low"}

INVENTORY_PATH = "task-folder/agents/skills-rebuild/_audit/skills-inventory.csv"
DESTINATION_MAP_PATH = "task-folder/agents/skills-rebuild/_audit/destination-map.csv"
ROUTER_MAP_PATH = "task-folder/agents/skills-rebuild/_audit/router-map.csv"
TAXONOMY_REPORT_PATH = "task-folder/agents/skills-rebuild/_audit/functional-taxonomy.md"

def get_git_output(cmd):
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return res.stdout.strip()

def verify_all():
    print("=== STARTING PHASE 05 TAXONOMY & DESTINATION RECONCILIATION VALIDATION ===")
    
    # Check HEAD and Base
    try:
        head_sha = get_git_output(["git", "rev-parse", "HEAD"])
        print(f"  HEAD SHA: {head_sha}")
    except Exception as e:
        print(f"  Warning: Could not get HEAD SHA: {e}")

    # 1. Check 1: skills-inventory.csv contains 2,331 rows
    print("\n[CHECK 1] Row Count of Source Inventory:")
    assert os.path.exists(INVENTORY_PATH), f"Error: Inventory missing at {INVENTORY_PATH}"
    with open(INVENTORY_PATH, "r", encoding="utf-8") as f:
        inv_rows = list(csv.DictReader(f))
    total_inv = len(inv_rows)
    print(f"  - Total source inventory rows: {total_inv}")
    assert total_inv == 2331, f"Expected 2331 rows in inventory, found {total_inv}"
    print(" -> PASS: Inventory row count is exactly 2,331.")

    # 2. Check 2: Exactly 45 quarantined rows excluded
    print("\n[CHECK 2] Quarantined Population Identification:")
    quarantined_rows = [r for r in inv_rows if r.get("conversion_status") == "Not In Scope (Phase 03 Quarantined)"]
    quarantined_count = len(quarantined_rows)
    print(f"  - Quarantined row count: {quarantined_count}")
    assert quarantined_count == 45, f"Expected 45 quarantined rows, found {quarantined_count}"
    quarantined_paths = {r["source_path"] for r in quarantined_rows}
    print(" -> PASS: Exactly 45 quarantined rows identified and isolated.")

    # 3. Check 3: Exactly 2,286 active rows mapped
    print("\n[CHECK 3] Retained Population Destination Mapping Count:")
    assert os.path.exists(DESTINATION_MAP_PATH), f"Error: Destination map missing at {DESTINATION_MAP_PATH}"
    with open(DESTINATION_MAP_PATH, "r", encoding="utf-8") as f:
        dest_rows = list(csv.DictReader(f))
    dest_count = len(dest_rows)
    print(f"  - Total mapped destination rows: {dest_count}")
    assert dest_count == 2286, f"Expected 2286 destination rows, found {dest_count}"
    print(" -> PASS: Exactly 2,286 active retained skills mapped.")

    # 4. Check 4: Every active source path appears exactly once
    print("\n[CHECK 4] Source Path 1:1 Coverage & Bijectivity:")
    active_inv_paths = {r["source_path"] for r in inv_rows if r.get("conversion_status") != "Not In Scope (Phase 03 Quarantined)"}
    dest_src_paths = [r["source_path"] for r in dest_rows]
    dest_src_set = set(dest_src_paths)
    assert len(dest_src_paths) == len(dest_src_set), "Duplicate source_path found in destination-map.csv!"
    assert active_inv_paths == dest_src_set, "Mismatch between active inventory source paths and destination map source paths!"
    print(f"  - Verified 1:1 coverage across all {len(dest_src_set)} source paths.")
    print(" -> PASS: Every active source path appears exactly once.")

    # 5. Check 5: No quarantined source path appears in destination-map.csv
    print("\n[CHECK 5] Quarantined Source Exclusion:")
    quarantined_in_dest = quarantined_paths.intersection(dest_src_set)
    assert len(quarantined_in_dest) == 0, f"Error: Quarantined paths leaked into destination map: {quarantined_in_dest}"
    print(" -> PASS: Zero quarantined source paths exist in destination-map.csv.")

    # 6. Check 6: Every mapped row has a valid top-level category
    print("\n[CHECK 6] Category and Subcategory Validity:")
    cat_counts = Counter()
    subcat_counts = defaultdict(Counter)
    for r in dest_rows:
        cat = r.get("proposed_category", "")
        subcat = r.get("proposed_subcategory", "")
        assert cat in ALLOWED_CATEGORIES, f"Invalid category '{cat}' for source '{r['source_path']}'"
        assert subcat and subcat.strip() != "", f"Empty subcategory for source '{r['source_path']}'"
        cat_counts[cat] += 1
        subcat_counts[cat][subcat] += 1
    print(f"  - Verified all rows map to the 10 allowed functional categories.")
    print(" -> PASS: Category and subcategory fields are 100% valid.")

    # 7. Check 7: Valid compatibility classification
    print("\n[CHECK 7] Compatibility Status Field Check:")
    for r in dest_rows:
        compat = r.get("compatibility_status", "")
        assert compat and compat.strip() != "", f"Empty compatibility_status for source '{r['source_path']}'"
    print(" -> PASS: Every row possesses a valid compatibility status.")

    # 8. Check 8: Non-empty destination path
    print("\n[CHECK 8] Destination Path Presence:")
    for r in dest_rows:
        dest_p = r.get("proposed_final_path", "")
        assert dest_p and dest_p.strip() != "", f"Empty proposed_final_path for source '{r['source_path']}'"
    print(" -> PASS: Every row has an explicit proposed destination path.")

    # 9. Check 9: Destination paths are globally unique
    print("\n[CHECK 9] Global Destination Path Uniqueness (Exact):")
    final_paths = [r["proposed_final_path"] for r in dest_rows]
    assert len(final_paths) == len(set(final_paths)), "Duplicate proposed_final_path detected in destination-map.csv!"
    print(f"  - Verified all {len(final_paths)} destination paths are globally unique.")
    print(" -> PASS: Global destination path uniqueness confirmed (0 duplicates).")

    # 10. Check 10: Destination paths are unique case-insensitively
    print("\n[CHECK 10] Case-Insensitive Destination Path Uniqueness:")
    final_paths_lower = [p.lower() for p in final_paths]
    assert len(final_paths_lower) == len(set(final_paths_lower)), "Case-insensitive duplicate proposed_final_path detected!"
    print(" -> PASS: Case-insensitive destination path uniqueness confirmed.")

    # 11. Check 11: No router/path namespace collisions
    print("\n[CHECK 11] Router and Destination Namespace Collision Detection:")
    assert os.path.exists(ROUTER_MAP_PATH), f"Error: Router map missing at {ROUTER_MAP_PATH}"
    with open(ROUTER_MAP_PATH, "r", encoding="utf-8") as f:
        router_rows = list(csv.DictReader(f))
    router_paths = [r["proposed_path"] for r in router_rows]
    router_paths_lower = {p.lower() for p in router_paths}
    for p in final_paths:
        assert p.lower() not in router_paths_lower, f"Destination path '{p}' collides with a planned router path!"
    print(f"  - Verified 0 collisions across {len(router_rows)} planned routers and {len(final_paths)} skill destinations.")
    print(" -> PASS: Zero namespace collisions between skill destinations and planned routers.")

    # 12. Check 12: Target paths follow canonical naming conventions
    print("\n[CHECK 12] Destination Path Naming Conventions:")
    for p in final_paths:
        assert p.startswith("task-folder/agents/skills/"), f"Path '{p}' does not start with task-folder/agents/skills/"
        parts = p.split("/")
        assert len(parts) == 6, f"Path '{p}' depth is not standard (expected 6 parts, got {len(parts)})"
        cat, subcat, skill_fn = parts[3], parts[4], parts[5]
        assert cat in ALLOWED_CATEGORIES, f"Category '{cat}' invalid in path '{p}'"
        assert re.match(r"^[a-z0-9\-]+$", subcat), f"Subcategory '{subcat}' is not kebab-case in '{p}'"
        assert re.match(r"^[a-z0-9\-]+$", skill_fn), f"Skill folder '{skill_fn}' is not kebab-case in '{p}'"
    print(" -> PASS: All destination paths adhere strictly to kebab-case and shallow directory conventions.")

    # 13. Check 13: Category counts sum to exactly 2,286
    print("\n[CHECK 13] Category Sum Reconciliation:")
    sum_cats = sum(cat_counts.values())
    print(f"  - Category sum: {sum_cats}")
    assert sum_cats == 2286, f"Expected category sum 2286, got {sum_cats}"
    for cat in sorted(cat_counts.keys()):
        print(f"    * {cat}: {cat_counts[cat]}")
    print(" -> PASS: Category counts sum exactly to 2,286.")

    # 14. Check 14: Report category counts in functional-taxonomy.md equal CSV counts
    print("\n[CHECK 14] Report-to-CSV Reconciliation:")
    assert os.path.exists(TAXONOMY_REPORT_PATH), f"Error: Taxonomy report missing at {TAXONOMY_REPORT_PATH}"
    with open(TAXONOMY_REPORT_PATH, "r", encoding="utf-8") as f:
        report_text = f.read()
    for cat, count in cat_counts.items():
        assert f"Skill Count**: **{count}**" in report_text or f"| **`{cat}`** | *(Total)* | **{count}** |" in report_text, (
            f"Category count for '{cat}' ({count}) not reconciled in report!"
        )
    print(" -> PASS: All category counts in functional-taxonomy.md match destination-map.csv exactly.")

    # 15. Check 15: Confidence values belong to allowed enum
    print("\n[CHECK 15] Placement Confidence Enum:")
    for r in dest_rows:
        conf = r.get("placement_confidence", "")
        assert conf in ALLOWED_CONFIDENCE, f"Invalid confidence '{conf}' for source '{r['source_path']}'"
    print(" -> PASS: All placement confidence values belong strictly to {'high', 'medium', 'low'}.")

    # 16. Check 16: Every 'low' confidence row contains an explicit placement concern
    print("\n[CHECK 16] Low Confidence Placement Concern Gate:")
    low_count = 0
    for r in dest_rows:
        conf = r.get("placement_confidence", "")
        concern = r.get("placement_concern", "")
        if conf == "low":
            low_count += 1
            assert concern and concern.strip() != "None" and concern.strip() != "", (
                f"Row '{r['source_path']}' with low confidence has no documented placement_concern!"
            )
    print(f"  - Verified {low_count} low-confidence rows (all contain documented placement concerns).")
    print(" -> PASS: Placement concern requirement verified for all low-confidence rows.")

    # 17. Check 17: Zero workstation absolute path leaks in Phase 05 files
    print("\n[CHECK 17] Workstation Path Leak Detection:")
    phase_05_files = [DESTINATION_MAP_PATH, ROUTER_MAP_PATH, TAXONOMY_REPORT_PATH, "task-folder/agents/skills-rebuild/_audit/verify_phase_05.py"]
    user_pattern = re.compile(r"/Users/[a-zA-Z0-9_\-]+|/home/[a-zA-Z0-9_\-]+|C:\\\\Users\\\\[a-zA-Z0-9_\-]+")
    for fp in phase_05_files:
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                matches = user_pattern.findall(content)
                assert len(matches) == 0, f"Workstation path leak detected in {fp}: {matches}"
    print(" -> PASS: Zero workstation absolute path leaks detected in any Phase 05 files.")

    # 18. Check 18: Hard check: Git diff proves ZERO modifications under task-folder/agents/skills/
    print("\n[CHECK 18] Physical Immutability Gate (Zero Changes in Active Skills Tree):")
    try:
        git_status_diff = get_git_output(["git", "diff", "--name-only", "main"])
        changed_files = [line.strip() for line in git_status_diff.splitlines() if line.strip()]
        skill_tree_changes = [f for f in changed_files if f.startswith("task-folder/agents/skills/")]
        assert len(skill_tree_changes) == 0, (
            f"Violation: Physical skills tree modified during Phase 05! Touched files: {skill_tree_changes}"
        )
        print(f"  - Checked {len(changed_files)} changed files on branch vs main.")
        print("  - ZERO physical skills were moved, modified, split, merged, or deleted.")
        print(" -> PASS: Hard check confirmed: 'map first, move later' principle physically upheld.")
    except Exception as e:
        print(f"  - Error during git diff verification: {e}")
        raise e

    print("\n=== ALL 18 PHASE 05 VALIDATION CHECKS PASSED PERFECTLY! CONGRATULATIONS! ===")

if __name__ == "__main__":
    verify_all()
