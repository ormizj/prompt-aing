#!/usr/bin/env python3
"""
Skill Verification Script
Checks that all components of the export-conversation skill are properly installed.
"""

import sys
from pathlib import Path

def check_file(path, description):
    """Check if a file exists."""
    if path.exists():
        size = path.stat().st_size
        print(f"[OK] {description:40} ({size:,} bytes)")
        return True
    else:
        print(f"[FAIL] {description:40} MISSING")
        return False

def check_python():
    """Check Python version."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"[OK] Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"[FAIL] Python version: {version.major}.{version.minor}.{version.micro} (3.6+ required)")
        return False

def check_openpyxl():
    """Check if openpyxl is installed."""
    try:
        import openpyxl
        print(f"[OK] openpyxl version: {openpyxl.__version__}")
        return True
    except ImportError:
        print(f"[FAIL] openpyxl not installed (run: pip install openpyxl)")
        return False

def main():
    """Main verification function."""
    print("=" * 70)
    print("Export Conversation Skill - Verification")
    print("=" * 70)
    print()

    skill_dir = Path(__file__).parent.parent
    all_good = True

    # Check Python
    print("Python Environment:")
    all_good &= check_python()
    all_good &= check_openpyxl()
    print()

    # Check documentation files
    print("Documentation Files:")
    all_good &= check_file(skill_dir / "SKILL.md", "SKILL.md (Main skill definition)")
    all_good &= check_file(skill_dir / "README.md", "README.md (Overview)")
    all_good &= check_file(skill_dir / "USAGE.md", "USAGE.md (User guide)")
    all_good &= check_file(skill_dir / "EXAMPLES.md", "EXAMPLES.md (Sample outputs)")
    all_good &= check_file(skill_dir / "QUICKREF.md", "QUICKREF.md (Quick reference)")
    print()

    # Check script files
    print("Script Files:")
    all_good &= check_file(skill_dir / "scripts" / "export_conversation.py", "export_conversation.py (Main script)")
    all_good &= check_file(skill_dir / "scripts" / "test_export.py", "test_export.py (Test utility)")
    all_good &= check_file(skill_dir / "scripts" / "verify_skill.py", "verify_skill.py (This script)")
    print()

    # Check sample data
    print("Sample Data:")
    all_good &= check_file(skill_dir / "sample_data.json", "sample_data.json (Test conversation)")
    print()

    # Check YAML frontmatter
    print("SKILL.md Configuration:")
    try:
        with open(skill_dir / "SKILL.md", 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                # Extract frontmatter
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1].strip()
                    print("[OK] YAML frontmatter found")

                    # Check for required fields
                    required = ['name:', 'description:', 'allowed-tools:']
                    for field in required:
                        if field in frontmatter:
                            print(f"  [OK] {field.strip(':')}")
                        else:
                            print(f"  [FAIL] {field.strip(':')} MISSING")
                            all_good = False
                else:
                    print("[FAIL] YAML frontmatter malformed")
                    all_good = False
            else:
                print("[FAIL] YAML frontmatter missing")
                all_good = False
    except Exception as e:
        print(f"[FAIL] Error checking SKILL.md: {e}")
        all_good = False
    print()

    # Final summary
    print("=" * 70)
    if all_good:
        print("[OK] ALL CHECKS PASSED - Skill is ready to use!")
        print()
        print("Next steps:")
        print("  1. If openpyxl is installed, run: python scripts/test_export.py")
        print("  2. Try the skill: /export-conversation")
        print("  3. Read USAGE.md for detailed instructions")
    else:
        print("[FAIL] SOME CHECKS FAILED - Please review the errors above")
        print()
        print("Common fixes:")
        print("  - Install Python 3.6+: https://python.org")
        print("  - Install openpyxl: pip install openpyxl")
        print("  - Check file permissions")
    print("=" * 70)

    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())