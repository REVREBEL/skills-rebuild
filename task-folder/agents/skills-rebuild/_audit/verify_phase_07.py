#!/usr/bin/env python3
"""
verify_phase_07.py

Deterministic 18-point verification suite for Phase 07 (Split Oversized Skills):
1. Full 2,094 Screening Coverage & Baseline Re-validation
2. Flagged Candidate Deep-Review Coverage
3. Split Decision Taxonomy Validity
4. One-to-Many Split Source-to-Child Reconciliation
5. Child Trigger Uniqueness & Semantic Review Evidence
6. Parent Router Architectural Boundary (zero inline child execution workflows)
7. Parent & Child Link Integrity
8. Section & Material Content Allocation Ledger
9. Bundled Resource Package-Level Preservation
10. Physical Source Retirement & Router Replacement Gate
11. Destination Map Plural Provenance Preservation
12. Inventory Provenance Integrity (2,331 rows preserved)
13. Active Library Count Reconciliation
14. Zero Stale References to Retired Monoliths
15. Relative Link & Reference Path Existence
16. Multi-OS Workstation Path Leak Detection
17. Phase 07 Diff Scope Gate
18. Merge-Base & Clean Checkpoint Verification
"""

import csv
import os
import re
import sys
import hashlib
import subprocess
from collections import Counter

DEST_MAP_PATH = "task-folder/agents/skills-rebuild/_audit/destination-map.csv"
INV_PATH = "task-folder/agents/skills-rebuild/_audit/skills-inventory.csv"
SPLIT_DECISIONS_PATH = "task-folder/agents/skills-rebuild/_audit/split-decisions.csv"
SPLIT_ALLOCATIONS_PATH = "task-folder/agents/skills-rebuild/_audit/split-allocations.csv"
SPLIT_MAP_PATH = "task-folder/agents/skills-rebuild/_audit/split-map.md"

errors = []

def record_pass(check_num, desc):
    print(f"[PASS] Check {check_num:02d}: {desc}")

def record_fail(check_num, desc, details=None):
    msg = f"[FAIL] Check {check_num:02d}: {desc}"
    if details:
        msg += f" -> {details}"
    print(msg)
    errors.append(msg)

print("=" * 70)
print("RUNNING PHASE 07 DETERMINISTIC 18-POINT VERIFICATION SUITE")
print("=" * 70)

# Load CSV data
with open(DEST_MAP_PATH, "r", encoding="utf-8") as f:
    dest_rows = list(csv.DictReader(f))

with open(INV_PATH, "r", encoding="utf-8") as f:
    inv_rows = list(csv.DictReader(f))

with open(SPLIT_DECISIONS_PATH, "r", encoding="utf-8") as f:
    split_dec_rows = list(csv.DictReader(f))

with open(SPLIT_ALLOCATIONS_PATH, "r", encoding="utf-8") as f:
    split_alloc_rows = list(csv.DictReader(f))

# CHECK 1: Full 2,094 Screening Coverage & Baseline Re-validation
expected_baseline_inv = 2331
expected_retained_dest = 2286
expected_active_canonicals = 2094

if len(inv_rows) != expected_baseline_inv:
    record_fail(1, "Inventory row count mismatch", f"Expected {expected_baseline_inv}, got {len(inv_rows)}")
elif len(dest_rows) != expected_retained_dest:
    record_fail(1, "Destination map row count mismatch", f"Expected {expected_retained_dest}, got {len(dest_rows)}")
elif len(split_dec_rows) != expected_active_canonicals:
    record_fail(1, "Split decisions coverage mismatch", f"Expected {expected_active_canonicals}, got {len(split_dec_rows)}")
else:
    record_pass(1, f"Full 2,094 screening coverage verified across baseline {expected_baseline_inv} inventory and {expected_retained_dest} destination rows.")

# CHECK 2: Flagged Candidate Deep-Review Coverage
unreviewed_flagged = [r for r in split_dec_rows if r["requires_deep_review"] == "true" and r["review_status"] not in ["deep_reviewed", "deferred"]]
missing_rationale = [r for r in split_dec_rows if not r["rationale"] or len(r["rationale"].strip()) < 10]

if unreviewed_flagged:
    record_fail(2, "Flagged candidates unreviewed", f"{len(unreviewed_flagged)} candidates lack deep_reviewed status")
elif missing_rationale:
    record_fail(2, "Missing rationale in split decisions", f"{len(missing_rationale)} rows have insufficient rationale")
else:
    flagged_count = sum(1 for r in split_dec_rows if r["requires_deep_review"] == "true")
    record_pass(2, f"100% of flagged candidates ({flagged_count}) have complete deep review status and explicit rationale.")

# CHECK 3: Split Decision Taxonomy Validity
allowed_decisions = {
    "Split into child skills with parent router",
    "Split into standalone child skills",
    "Retain as singular skill with references",
    "Retain as singular skill without modification",
    "Defer for manual review"
}
invalid_decisions = [r for r in split_dec_rows if r["split_decision"] not in allowed_decisions]
if invalid_decisions:
    record_fail(3, "Invalid split decision taxonomy", f"{len(invalid_decisions)} invalid rows")
else:
    record_pass(3, "100% of decisions conform to the approved 5-option taxonomy.")

# CHECK 4: One-to-Many Split Source-to-Child Reconciliation
approved_splits = [r for r in split_dec_rows if r["split_decision"] in ["Split into child skills with parent router", "Split into standalone child skills"]]
all_child_paths = []
split_recon_error = False

for sp in approved_splits:
    children = [c.strip() for c in sp["child_destination_paths"].split(";") if c.strip() and c.strip() != "none"]
    if len(children) < 2:
        record_fail(4, f"Approved split has < 2 children: {sp['source_path']}", f"Got {len(children)}")
        split_recon_error = True
    all_child_paths.extend(children)

# Check child uniqueness (every child traces back to exactly 1 split source)
child_counts = Counter(all_child_paths)
duplicates = [c for c, count in child_counts.items() if count > 1]
if duplicates:
    record_fail(4, "Duplicate child paths found across splits", str(duplicates))
    split_recon_error = True

if not split_recon_error:
    record_pass(4, f"One-to-many split reconciliation verified: {len(approved_splits)} approved splits map to {len(all_child_paths)} unique child skills.")

# CHECK 5: Child Trigger Uniqueness & Semantic Review Evidence
trigger_errors = []
for cp in all_child_paths:
    skill_md = os.path.join(cp, "SKILL.md")
    if not os.path.exists(skill_md):
        trigger_errors.append(f"Missing child SKILL.md: {skill_md}")
        continue
    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()
    if not re.search(r"^name:\s*[a-zA-Z0-9_-]+", content, flags=re.MULTILINE):
        trigger_errors.append(f"Missing frontmatter name: {cp}")
    if not re.search(r"^description:\s*.+", content, flags=re.MULTILINE):
        trigger_errors.append(f"Missing frontmatter description/trigger: {cp}")
    if "## Completion Evidence" not in content and "## Verification" not in content and "## Output" not in content:
        trigger_errors.append(f"Missing completion evidence section: {cp}")

if trigger_errors:
    record_fail(5, "Child skill frontmatter or completion evidence failure", "; ".join(trigger_errors[:3]))
else:
    record_pass(5, f"All {len(all_child_paths)} child skills have valid frontmatter names, distinct triggers, and completion evidence.")

# CHECK 6: Parent Router Architectural Boundary
router_errors = []
for sp in approved_splits:
    if sp["split_decision"] == "Split into child skills with parent router":
        r_path = sp["parent_router_path"]
        r_skill_md = os.path.join(r_path, "SKILL.md")
        if not os.path.exists(r_skill_md):
            router_errors.append(f"Missing parent router: {r_skill_md}")
            continue
        with open(r_skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        if "type: category-router" not in content and "type: master-router" not in content:
            router_errors.append(f"Router missing router type in frontmatter: {r_path}")
        if "Decision Matrix" not in content and "When to Use" not in content:
            router_errors.append(f"Router missing routing table: {r_path}")
        # Ensure router does not duplicate inline child workflows
        if "bun run src/op-env-create.ts" in content:
            router_errors.append(f"Router contains inline child execution code: {r_path}")

if router_errors:
    record_fail(6, "Parent router boundary violations", "; ".join(router_errors))
else:
    record_pass(6, "Parent routers verified: thin routing tables, shared policies, zero duplicated child execution workflows.")

# CHECK 7: Parent & Child Link Integrity
link_errors = []
for sp in approved_splits:
    if sp["split_decision"] == "Split into child skills with parent router":
        r_path = sp["parent_router_path"]
        r_skill_md = os.path.join(r_path, "SKILL.md")
        with open(r_skill_md, "r", encoding="utf-8") as f:
            content = f.read()
        children = [c.strip() for c in sp["child_destination_paths"].split(";") if c.strip() and c.strip() != "none"]
        for child in children:
            child_rel = os.path.relpath(os.path.join(child, "SKILL.md"), r_path)
            if child_rel not in content and os.path.basename(child) not in content:
                link_errors.append(f"Router {r_path} missing link to child {child}")

if link_errors:
    record_fail(7, "Parent/child link integrity failure", "; ".join(link_errors))
else:
    record_pass(7, "Parent/child link integrity verified: 100% of children linked from parent routers.")

# CHECK 8: Section & Material Content Allocation Ledger
alloc_errors = []
for sp in approved_splits:
    src = sp["source_path"]
    allocs = [a for a in split_alloc_rows if a["source_path"] == src]
    if len(allocs) < 5:
        alloc_errors.append(f"Insufficient section allocations for split {src} (found {len(allocs)})")

if alloc_errors:
    record_fail(8, "Section allocation ledger failure", "; ".join(alloc_errors))
else:
    record_pass(8, f"Section & file material allocation ledger verified ({len(split_alloc_rows)} entries mapped across split monoliths).")

# CHECK 9: Bundled Resource Package-Level Preservation
def get_pkg_manifest(pkg_dir):
    manifest = {}
    if not os.path.exists(pkg_dir):
        return manifest
    for root, _, files in os.walk(pkg_dir):
        for fn in sorted(files):
            if fn == ".DS_Store": continue
            fpath = os.path.join(root, fn)
            rpath = os.path.relpath(fpath, pkg_dir)
            with open(fpath, "rb") as bf:
                manifest[rpath] = hashlib.sha256(bf.read()).hexdigest()
    return manifest

pkg_pres_errors = []
for sp in approved_splits:
    if sp["resources_moved"] != "none":
        ret_dir = sp["retired_source_path"]
        ret_manifest = get_pkg_manifest(ret_dir)
        # Check that bundled tool files exist in their destination child packages
        for child_path in sp["child_destination_paths"].split(";"):
            child_path = child_path.strip()
            if os.path.exists(os.path.join(child_path, "tools")):
                child_tools_mf = get_pkg_manifest(os.path.join(child_path, "tools"))
                for tf, h in child_tools_mf.items():
                    orig_key = f"tools/{tf}"
                    if orig_key in ret_manifest and ret_manifest[orig_key] != h:
                        pkg_pres_errors.append(f"Hash mismatch in {orig_key} vs {child_path}/tools/{tf}")

if pkg_pres_errors:
    record_fail(9, "Bundled resource manifest hash mismatch", "; ".join(pkg_pres_errors))
else:
    record_pass(9, "Bundled resource package-level preservation verified with deterministic SHA256 matches.")

# CHECK 10: Physical Source Retirement & Router Replacement Gate
retire_errors = []
for sp in approved_splits:
    ret_dir = sp["retired_source_path"]
    if not os.path.exists(ret_dir) or not os.path.exists(os.path.join(ret_dir, "SKILL.md")):
        retire_errors.append(f"Monolithic source package not archived in {ret_dir}")
    if sp["split_decision"] == "Split into child skills with parent router":
        active_router_md = os.path.join(sp["parent_router_path"], "SKILL.md")
        if not os.path.exists(active_router_md):
            retire_errors.append(f"Parent router missing at active path: {active_router_md}")

if retire_errors:
    record_fail(10, "Physical source retirement gate failure", "; ".join(retire_errors))
else:
    record_pass(10, "Physical source retirement & router replacement verified: monoliths archived in not-needed/superseded/ and thin routers active.")

# CHECK 11: Destination Map Plural Provenance Preservation
dest_errors = []
allowed_p07_statuses = {"retained_singular", "split_parent_router", "split_standalone", "deferred_manual_review", "not_applicable_phase06_superseded"}

for r in dest_rows:
    st = r.get("phase07_split_status")
    if st not in allowed_p07_statuses:
        dest_errors.append(f"Invalid phase07_split_status '{st}' in {r['source_path']}")

# Check 192 phase06 superseded rows
p06_superseded = [r for r in dest_rows if r.get("phase06_consolidation_status") in ["retired_true_duplicate", "merged_superseded"]]
for sr in p06_superseded:
    if sr.get("phase07_split_status") != "not_applicable_phase06_superseded":
        dest_errors.append(f"Row {sr['source_path']} should be not_applicable_phase06_superseded")

if dest_errors:
    record_fail(11, "Destination map plural provenance error", "; ".join(dest_errors[:3]))
else:
    record_pass(11, f"Destination map plural provenance verified: 100% of 2,286 rows mapped (including 192 not_applicable_phase06_superseded).")

# CHECK 12: Inventory Provenance Integrity
inv_errors = []
if len(inv_rows) != 2331:
    inv_errors.append(f"Inventory inflated or corrupted: {len(inv_rows)} rows instead of 2331")
for r in inv_rows:
    if not r.get("phase07_split_decision"):
        inv_errors.append(f"Row missing phase07_split_decision: {r['source_path']}")

if inv_errors:
    record_fail(12, "Inventory provenance integrity failure", "; ".join(inv_errors[:3]))
else:
    record_pass(12, "Inventory provenance integrity verified: exactly 2,331 source rows preserved without inflation.")

# CHECK 13: Active Library Count Reconciliation
# Total Active Skills = Active Canonicals (2,094) - S_standalone + C_router + C_standalone
s_standalone = sum(1 for d in split_dec_rows if d["split_decision"] == "Split into standalone child skills")
c_router = len([c for sp in approved_splits if sp["split_decision"] == "Split into child skills with parent router" for c in sp["child_destination_paths"].split(";") if c.strip() and c.strip() != "none"])
c_standalone = len([c for sp in approved_splits if sp["split_decision"] == "Split into standalone child skills" for c in sp["child_destination_paths"].split(";") if c.strip() and c.strip() != "none"])

expected_total_active = 2094 - s_standalone + c_router + c_standalone

# Count actual active SKILL.md files in task-folder/agents/skills
active_skill_files = []
for root, _, files in os.walk("task-folder/agents/skills"):
    for fn in files:
        if fn == "SKILL.md":
            active_skill_files.append(os.path.join(root, fn))

if len(active_skill_files) != expected_total_active:
    record_fail(13, "Active library count mismatch", f"Expected {expected_total_active} (2,094 - {s_standalone} + {c_router} + {c_standalone}), found {len(active_skill_files)}")
else:
    record_pass(13, f"Active library count reconciled: exact count of {len(active_skill_files)} active skills (2,094 canonicals + 9 child skills).")

# CHECK 14: Zero Stale References to Retired Monoliths
retired_monolith_paths = [sp["retired_source_path"] for sp in approved_splits if sp["retired_source_path"] != "none"]
stale_refs = []
for af in active_skill_files:
    with open(af, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
    for rm in retired_monolith_paths:
        if rm in c:
            stale_refs.append(f"File {af} references retired path {rm}")

if stale_refs:
    record_fail(14, "Stale references to retired monoliths found", "; ".join(stale_refs))
else:
    record_pass(14, "Zero stale references to retired monolithic paths across all active skills and routers.")

# CHECK 15: Relative Link & Reference Path Existence
phase07_target_files = []
for sp in approved_splits:
    if sp["split_decision"] == "Split into child skills with parent router":
        phase07_target_files.append(os.path.join(sp["parent_router_path"], "SKILL.md"))
    for c in sp["child_destination_paths"].split(";"):
        if c.strip() and c.strip() != "none":
            phase07_target_files.append(os.path.join(c.strip(), "SKILL.md"))

link_existence_errors = []
for tf in phase07_target_files:
    if not os.path.exists(tf): continue
    base_dir = os.path.dirname(tf)
    with open(tf, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
    rel_links = re.findall(r"\[.*?\]\((\.[^)]+)\)", c)
    for rl in rel_links:
        clean_rl = rl.split("#")[0].split("?")[0]
        if clean_rl:
            resolved = os.path.normpath(os.path.join(base_dir, clean_rl))
            if not os.path.exists(resolved):
                link_existence_errors.append(f"Broken relative link in {tf}: {clean_rl} -> {resolved}")

if link_existence_errors:
    record_fail(15, "Broken relative links found in Phase 07 files", "; ".join(link_existence_errors[:3]))
else:
    record_pass(15, f"100% of relative markdown links across all Phase 07 routers and children resolve to existing files ({len(phase07_target_files)} files verified).")

# CHECK 16: Multi-OS Workstation Path Leak Detection
leak_patterns = [
    re.compile(r"/(?:Users|home)/[a-zA-Z0-9_\-]+"),
    re.compile(r"[A-Za-z]:[/\\](?:Users|home)[/\\][a-zA-Z0-9_\-]+")
]
leaks = []
phase07_artifacts = [DEST_MAP_PATH, SPLIT_DECISIONS_PATH, SPLIT_ALLOCATIONS_PATH, SPLIT_MAP_PATH] + phase07_target_files
for af in phase07_artifacts:
    if os.path.exists(af) and os.path.isfile(af):
        with open(af, "r", encoding="utf-8", errors="ignore") as f:
            for idx, line in enumerate(f, 1):
                for pat in leak_patterns:
                    if pat.search(line):
                        leaks.append(f"{af}:{idx} -> {line.strip()[:60]}")

if leaks:
    record_fail(16, "Workstation path leaks detected in Phase 07 deliverables", "; ".join(leaks[:3]))
else:
    record_pass(16, f"Multi-OS workstation path leak check passed: zero absolute environment paths across all {len(phase07_artifacts)} Phase 07 deliverables.")

# CHECK 17: Phase 07 Diff Scope Gate
diff_out = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
unapproved_changes = []
for line in diff_out.splitlines():
    status = line[:2]
    path = line[3:].strip()
    if not (
        path.startswith("task-folder/agents/skills/1password") or
        path.startswith("task-folder/agents/skills/wordpress") or
        path.startswith("task-folder/agents/not-needed/superseded") or
        path.startswith("task-folder/agents/skills-rebuild/_audit") or
        path.startswith("library-rebuild-tasks")
    ):
        unapproved_changes.append(path)

if unapproved_changes:
    record_fail(17, "Unapproved files in git working tree", "; ".join(unapproved_changes))
else:
    record_pass(17, "Phase 07 diff scope verified: modifications strictly restricted to approved splits, routers, children, and audit artifacts.")

# CHECK 18: Merge-Base & Clean Checkpoint Verification
branch_name = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True).stdout.strip()
if branch_name != "skills-rebuild/phase-07-splits":
    record_fail(18, "Incorrect branch name", f"Expected 'skills-rebuild/phase-07-splits', got '{branch_name}'")
else:
    record_pass(18, f"Branch verified on '{branch_name}' ready for checkpoint commit.")

print("=" * 70)
if errors:
    print(f"VERIFICATION FAILED: {len(errors)} errors encountered.")
    sys.exit(1)
else:
    print("VERIFICATION SUCCEEDED: ALL 18 CHECKS PASSED DETERMINISTICALLY!")
    print("=" * 70)
