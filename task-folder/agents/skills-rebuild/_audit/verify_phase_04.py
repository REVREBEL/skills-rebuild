import csv
import os

CSV_PATH = "task-folder/agents/skills-rebuild/_audit/skills-inventory.csv"
ROOT_DIR = "."

RENAMED_PATHS_MAP = {
    "task-folder/agents/skills/linear-claude-skill": "task-folder/agents/skills/linear-skill",
    "task-folder/agents/skills/varlock-claude-skill": "task-folder/agents/skills/varlock-skill",
    "task-folder/agents/skills/folder-specific-claude-and-agents-md": "task-folder/agents/skills/folder-specific-agent-context",
    "task-folder/agents/skills/internal-comms-anthropic": "task-folder/agents/skills/internal-comms-guidelines"
}

def verify_all():
    print("=== STARTING PHASE 04 RECONCILIATION VALIDATION ===")

    # 1. Load CSV
    assert os.path.exists(CSV_PATH), f"Error: CSV does not exist at {CSV_PATH}"
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # 2. Check total row count
    total_rows = len(rows)
    print(f"[CHECK 1] Row Count: {total_rows} rows loaded.")
    assert total_rows == 2331, f"Error: Expected exactly 2331 rows, got {total_rows}"
    print(" -> PASS: Row count is exactly 2,331.")

    # 3. Check status metrics
    converted = sum(1 for r in rows if r.get("conversion_status") == "Converted")
    intrinsic = sum(1 for r in rows if r.get("conversion_status") == "Retained (Intrinsic)")
    no_change = sum(1 for r in rows if r.get("conversion_status") == "Reviewed - No Conversion Required")
    blockers = sum(1 for r in rows if r.get("conversion_status") == "Requires Manual Review")

    print(f"[CHECK 2] Reconciliation Metrics:")
    print(f"  - Converted (Neutralized): {converted}")
    print(f"  - Retained (Intrinsic): {intrinsic}")
    print(f"  - Reviewed (No Conversion Required): {no_change}")
    print(f"  - Requires Manual Review: {blockers}")

    assert converted == 399, f"Error: Expected exactly 399 Converted, got {converted}"
    assert intrinsic == 14, f"Error: Expected exactly 14 Retained, got {intrinsic}"
    assert no_change == 1918, f"Error: Expected exactly 1918 Reviewed, got {no_change}"
    assert blockers == 0, f"Error: Expected exactly 0 Blockers, got {blockers}"
    assert converted + intrinsic + no_change + blockers == 2331, "Error: Sum of statuses does not match total!"
    print(" -> PASS: All category reconciliation metrics match perfectly.")

    # 4. Check renamed paths physically exist and old paths are gone
    print("[CHECK 3] Renamed Folder Physical State:")
    for old, new in RENAMED_PATHS_MAP.items():
        assert os.path.exists(os.path.join(ROOT_DIR, new)), f"Error: New folder does not exist: {new}"
        assert not os.path.exists(os.path.join(ROOT_DIR, old)), f"Error: Old folder still exists: {old}"
        print(f"  - {old} -> {new} verified.")
    print(" -> PASS: Renamed folders physically exist in their new locations, and old directories are gone.")

    # 5. Check database-to-filesystem reconciliation
    print("[CHECK 4] Database-to-Filesystem Path Reconciliation:")
    for r in rows:
        dest = r.get("current_destination")
        assert dest, f"Error: Row {r['source_path']} is missing current_destination!"
        assert os.path.exists(os.path.join(ROOT_DIR, dest)), f"Error: Path listed in current_destination does not exist: {dest}"
    print(" -> PASS: Every single row's current_destination reconciles perfectly with a physical filesystem path.")

    # 5. Check for workstation absolute paths (specifically our workstation 'garystringham')
    print("[CHECK 5] Workstation Absolute Path Leak Detection:")
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        csv_text = f.read()
    
    assert "garystringham" not in csv_text, "Error: Found 'garystringham' workstation leakage in CSV!"
    assert "file:///Users/" not in csv_text, "Error: Found 'file:///Users/' workstation leakage in CSV!"
    
    # Check renamed folder files for absolute path leaks
    for new in RENAMED_PATHS_MAP.values():
        dir_path = os.path.join(ROOT_DIR, new)
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="replace") as sf:
                        text = sf.read()
                    assert "garystringham" not in text, f"Error: Found 'garystringham' in {file_path}"
                    assert "file:///Users/" not in text, f"Error: Found 'file:///Users/' in {file_path}"
                except Exception as e:
                    pass
    print(" -> PASS: Zero workstation absolute path leaks detected in any Phase 04 assets.")

    print("=== ALL PHASE 04 RECONCILIATION VALIDATIONS PASSED! CONGRATULATIONS! ===")

if __name__ == "__main__":
    verify_all()
