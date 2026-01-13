# Installation Guide

## Overview

The **export-conversation** skill allows you to export Claude Code conversations to Excel format (.xlsx) with structured columns for Prompt, Summary, and Output.

## Prerequisites

- **Python**: 3.6 or higher
- **pip**: Python package manager (usually comes with Python)
- **openpyxl**: Python library for Excel file creation

## Installation Steps

### 1. Verify Python Installation

Open your terminal and run:

```bash
python --version
```

Expected output: `Python 3.x.x` (where x is 6 or higher)

If Python is not installed:
- **Windows**: Download from [python.org](https://python.org/downloads/) and check "Add Python to PATH" during installation
- **macOS**: `brew install python3` or download from python.org
- **Linux**: `sudo apt install python3 python3-pip` (Debian/Ubuntu) or equivalent for your distribution

### 2. Install openpyxl

Once Python is installed, install the required library:

```bash
pip install openpyxl
```

On some systems, you may need to use:
```bash
pip3 install openpyxl
```

Or with administrator privileges:
```bash
sudo pip install openpyxl  # Linux/macOS
```

### 3. Verify Installation

Run the verification script:

```bash
cd .claude/skills/export-conversation
python scripts/verify_skill.py
```

You should see all checks pass:
```
======================================================================
Export Conversation Skill - Verification
======================================================================

Python Environment:
[OK] Python version: 3.x.x
[OK] openpyxl version: 3.x.x

Documentation Files:
[OK] SKILL.md (Main skill definition)
[OK] README.md (Overview)
[OK] USAGE.md (User guide)
[OK] EXAMPLES.md (Sample outputs)
[OK] QUICKREF.md (Quick reference)

Script Files:
[OK] export_conversation.py (Main script)
[OK] test_export.py (Test utility)
[OK] verify_skill.py (This script)

Sample Data:
[OK] sample_data.json (Test conversation)

SKILL.md Configuration:
[OK] YAML frontmatter found
  [OK] name
  [OK] description
  [OK] allowed-tools

======================================================================
[OK] ALL CHECKS PASSED - Skill is ready to use!
======================================================================
```

### 4. Run Test Export

Test that everything works:

```bash
python scripts/test_export.py
```

This will:
1. Create sample conversation data
2. Generate a test Excel file
3. Report success

If successful, you'll see:
```
Created test data file: /path/to/test_conversation_data.json
[OK] openpyxl is installed (version X.X.X)
Loading conversation data...
Loaded 3 conversation turns
Creating Excel file: test-export-YYYYMMDD-HHMMSS.xlsx
Excel file created successfully: test-export-YYYYMMDD-HHMMSS.xlsx

[OK] Test completed successfully!

You can now open: /full/path/to/test-export-YYYYMMDD-HHMMSS.xlsx
```

Open the generated Excel file to verify the format looks correct.

## Troubleshooting

### Python Not Found

**Error**: `python: command not found` or `'python' is not recognized`

**Solution**:
1. Install Python from [python.org](https://python.org/downloads/)
2. Make sure to check "Add Python to PATH" during Windows installation
3. On macOS/Linux, you may need to use `python3` instead of `python`
4. Restart your terminal after installation

### pip Not Found

**Error**: `pip: command not found`

**Solution**:
```bash
# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Install pip
python get-pip.py
```

Or use your system package manager:
```bash
# Debian/Ubuntu
sudo apt install python3-pip

# macOS
brew install python3  # includes pip

# Windows
# Reinstall Python and check "Install pip" during setup
```

### openpyxl Installation Fails

**Error**: `ERROR: Could not install packages due to an EnvironmentError`

**Solutions**:

1. **Try with --user flag**:
   ```bash
   pip install --user openpyxl
   ```

2. **Upgrade pip first**:
   ```bash
   python -m pip install --upgrade pip
   pip install openpyxl
   ```

3. **Use a virtual environment** (recommended):
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate it
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

   # Install openpyxl
   pip install openpyxl
   ```

4. **Check permissions**:
   ```bash
   # Linux/macOS - use sudo if needed
   sudo pip install openpyxl

   # Windows - run command prompt as Administrator
   ```

### Verification Script Shows Errors

**Error**: `[FAIL] SKILL.md (Main skill definition) MISSING`

**Solution**:
1. Ensure you're in the correct directory: `.claude/skills/export-conversation`
2. Check that all files were properly created
3. Re-download or re-create the skill files

### Test Export Fails

**Error**: Various errors when running `test_export.py`

**Solutions**:

1. **Check you're in the right directory**:
   ```bash
   cd .claude/skills/export-conversation/scripts
   python test_export.py
   ```

2. **Verify openpyxl is installed**:
   ```bash
   python -c "import openpyxl; print(openpyxl.__version__)"
   ```

3. **Check write permissions**:
   ```bash
   # Try writing a test file
   echo "test" > test.txt
   rm test.txt
   ```

## Alternative: CSV Export

If you cannot install openpyxl or prefer a simpler solution, you can use CSV format instead:

```python
import csv
import json

# Load conversation data
with open('conversation_data.json', 'r') as f:
    data = json.load(f)

# Export to CSV
with open('conversation-export.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Prompt', 'Summary', 'Output'])

    for turn in data['conversation']:
        writer.writerow([turn['prompt'], turn['summary'], turn['output']])

print("CSV file created: conversation-export.csv")
```

CSV files can be opened in Excel, Google Sheets, or any spreadsheet application, but won't have formatting (colors, column widths, etc.).

## Next Steps

Once installation is complete:

1. Read [USAGE.md](USAGE.md) for detailed usage instructions
2. Review [EXAMPLES.md](EXAMPLES.md) to see example outputs
3. Check [QUICKREF.md](QUICKREF.md) for quick command reference
4. Try exporting your first conversation with `/export-conversation`

## Getting Help

If you're still having issues:

1. Run the verification script and note which checks fail
2. Check the specific error messages
3. Search for the error message online
4. Ask Claude Code for help: "I'm having trouble installing the export-conversation skill..."

## System-Specific Notes

### Windows

- Use `python` command (not `python3`)
- Paths use backslashes: `C:\path\to\file`
- May need to run Command Prompt as Administrator for some operations

### macOS

- May need to use `python3` and `pip3` commands
- Paths use forward slashes: `/path/to/file`
- May need `sudo` for some operations

### Linux

- Usually use `python3` and `pip3` commands
- Paths use forward slashes: `/path/to/file`
- May need `sudo` for some operations
- Ensure python3-pip is installed: `sudo apt install python3-pip`

## Verification Checklist

Before considering installation complete, verify:

- [ ] Python 3.6+ is installed and accessible via `python --version`
- [ ] pip is installed and accessible via `pip --version`
- [ ] openpyxl is installed and can be imported: `python -c "import openpyxl"`
- [ ] Verification script passes all checks: `python scripts/verify_skill.py`
- [ ] Test export creates a valid Excel file: `python scripts/test_export.py`
- [ ] You can open the test Excel file and see properly formatted data

Once all items are checked, your skill is ready to use!