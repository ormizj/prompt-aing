# Usage Guide: Export Conversation Skill

This guide walks you through using the export-conversation skill step-by-step.

## Installation

### Step 1: Install Python

Check if Python is installed:
```bash
python --version
```

If not installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python3` or download from python.org
- **Linux**: `sudo apt install python3` (Debian/Ubuntu) or `sudo yum install python3` (RHEL/CentOS)

### Step 2: Install openpyxl

```bash
pip install openpyxl
```

Verify installation:
```bash
python -c "import openpyxl; print('openpyxl version:', openpyxl.__version__)"
```

Expected output: `openpyxl version: 3.x.x`

### Step 3: Test the Installation

Run the test script:
```bash
cd .claude/skills/export-conversation/scripts
python test_export.py
```

This will:
1. Create sample conversation data
2. Generate a test Excel file
3. Verify everything works correctly

If successful, you'll see a test Excel file created that you can open.

## Using the Skill

### Method 1: Invoke via Skill Command

Simply type:
```
/export-conversation
```

Claude Code will:
1. Recognize the skill invocation
2. Analyze the current conversation
3. Extract prompts, generate summaries, and collect outputs
4. Create a JSON data file
5. Run the export script
6. Provide you with the Excel file location

### Method 2: Natural Language Request

Just ask:
```
"Can you export this conversation to Excel?"
"Save our conversation as a spreadsheet"
"I need an Excel file of our chat history"
"Export this to .xlsx format"
```

Claude will understand you want to use the export-conversation skill.

### Method 3: Manual Export (Advanced)

If you want more control, you can manually prepare the data:

1. **Create your conversation data JSON**:
```json
{
  "export_date": "2026-01-12T14:30:00",
  "conversation": [
    {
      "prompt": "User question here",
      "summary": "What was accomplished",
      "output": "Full assistant response"
    }
  ]
}
```

2. **Save it** (e.g., `my_conversation.json`)

3. **Run the export script**:
```bash
python .claude/skills/export-conversation/scripts/export_conversation.py my_conversation.json
```

4. **Optional: Specify output filename**:
```bash
python .claude/skills/export-conversation/scripts/export_conversation.py my_conversation.json my-export.xlsx
```

## Understanding the Output

### Excel File Structure

The generated Excel file has three columns:

1. **Prompt (Column A)**:
   - Width: 40 characters
   - Contains the user's complete input
   - Text is wrapped for readability

2. **Summary (Column B)**:
   - Width: 50 characters
   - Brief 1-2 sentence summary
   - Focuses on what was accomplished
   - Good for quick scanning

3. **Output (Column C)**:
   - Width: 80 characters
   - Full assistant response
   - May be truncated if extremely long (>32K chars)
   - Preserves line breaks and formatting

### Excel Formatting

- **Header Row**: Blue background (#4472C4), white bold text
- **Data Rows**: Black text on white background, top-aligned
- **Font**: Arial (10pt for data, 11pt for headers)
- **First Row Frozen**: Headers stay visible when scrolling
- **Text Wrapping**: Enabled for all cells

### File Naming

Files are automatically named with timestamps:
```
conversation-export-2026-01-12-143052.xlsx
                    YYYY-MM-DD-HHMMSS
```

This prevents overwriting previous exports.

## Common Workflows

### Workflow 1: Quick Documentation Export

**Goal**: Save today's work session for documentation

1. After completing your work with Claude Code
2. Type: `/export-conversation`
3. Wait for the Excel file to be created
4. Review the file
5. Share with your team or save to documentation folder

**Time**: ~30 seconds

### Workflow 2: Selective Export

**Goal**: Export only specific parts of a long conversation

1. Manually identify the conversation turns you want
2. Create a custom JSON with only those turns
3. Run: `python export_conversation.py my-selection.json selected-topics.xlsx`
4. Get a focused export with just the relevant content

**Time**: ~5 minutes (depends on selection size)

### Workflow 3: Regular Archival

**Goal**: Keep weekly records of all Claude Code interactions

1. At end of week, export each day's conversation
2. Name files descriptively: `2026-01-12-authentication-work.xlsx`
3. Store in organized folder structure:
   ```
   archives/
   ├── 2026-01/
   │   ├── week-1/
   │   │   ├── 2026-01-08-api-development.xlsx
   │   │   ├── 2026-01-09-frontend-components.xlsx
   │   │   └── 2026-01-10-debugging-session.xlsx
   ```

**Time**: ~2 minutes per conversation

### Workflow 4: Creating Training Materials

**Goal**: Build examples for teaching others how to use Claude Code

1. Have a exemplary conversation with Claude
2. Export to Excel
3. Use the Summary column as teaching points
4. Reference the full Output for details
5. Create presentations or guides from the structured data

**Time**: ~15 minutes (including export and review)

## Tips and Best Practices

### Writing Better Prompts for Export

When you know you'll export, write clear prompts:
- ✅ "Create an authentication API endpoint with JWT validation"
- ❌ "Do the auth thing we discussed"

Clear prompts make the export more valuable as documentation.

### Customizing Summaries

After export, you can edit the Excel file to:
- Make summaries more specific
- Add cross-references to other files
- Include links to related resources
- Add notes about outcomes or follow-ups

### Organizing Exports

Create a naming convention:
```
YYYY-MM-DD-[project]-[topic].xlsx

Examples:
2026-01-12-ecommerce-auth.xlsx
2026-01-13-ecommerce-cart-feature.xlsx
2026-01-14-ecommerce-payment-integration.xlsx
```

### Filtering and Analyzing

Once in Excel, you can:
- Filter by keyword in summaries
- Sort by prompt length
- Search across all outputs
- Create pivot tables for analysis
- Extract specific types of interactions (debugging vs. feature building)

## Advanced Usage

### Batch Exporting Multiple Conversations

Create a batch script (bash/PowerShell):

```bash
#!/bin/bash
# batch_export.sh

for json_file in conversations/*.json; do
    base_name=$(basename "$json_file" .json)
    python export_conversation.py "$json_file" "exports/${base_name}.xlsx"
done
```

### Converting to Other Formats

After generating Excel, convert to:

**PDF** (for sharing):
```python
# Requires openpyxl and reportlab
from openpyxl import load_workbook
# ... PDF generation code
```

**HTML** (for web publishing):
```python
import pandas as pd
df = pd.read_excel('export.xlsx')
df.to_html('export.html')
```

**Markdown** (for GitHub/docs):
```python
import pandas as pd
df = pd.read_excel('export.xlsx')
df.to_markdown('export.md')
```

### Programmatic Analysis

Load exports into data analysis tools:

```python
import pandas as pd

# Load multiple exports
df1 = pd.read_excel('export1.xlsx')
df2 = pd.read_excel('export2.xlsx')
combined = pd.concat([df1, df2])

# Analyze
print(f"Total conversations: {len(combined)}")
print(f"Average output length: {combined['Output'].str.len().mean()}")

# Find all debugging sessions
debugging = combined[combined['Summary'].str.contains('debug|fix|error', case=False)]
```

## Troubleshooting

### Issue: Excel file won't open

**Symptoms**: Double-clicking the file does nothing or shows an error

**Solutions**:
1. Check file isn't corrupted: `python -m openpyxl validate export.xlsx`
2. Try opening in Google Sheets or LibreOffice
3. Check file permissions: `ls -l export.xlsx`
4. Re-export with a different filename

### Issue: Some text is cut off

**Symptoms**: Long outputs are truncated

**Cause**: Excel has a 32,767 character limit per cell

**Solutions**:
1. The script automatically adds "[...truncated]" marker
2. For full content, split into multiple rows
3. Export to CSV instead (no cell limit)
4. Link to original source files

### Issue: Formatting looks wrong

**Symptoms**: Columns too narrow, text not wrapped, etc.

**Solutions**:
1. Manually adjust column widths in Excel
2. Edit the script's column width settings
3. Use Excel's "Format as Table" feature
4. Create a template with your preferred formatting

### Issue: Special characters display incorrectly

**Symptoms**: Emojis, accents, or symbols show as �

**Cause**: Encoding issues

**Solutions**:
1. Ensure script uses UTF-8 (it does by default)
2. Open in Excel with UTF-8 encoding
3. Use Google Sheets (better Unicode support)
4. Update to latest openpyxl version

## Getting Help

If you encounter issues:

1. **Check the logs**: Python will show error messages
2. **Verify installation**: Run `test_export.py`
3. **Review SKILL.md**: Full technical documentation
4. **Check EXAMPLES.md**: See working examples
5. **Ask Claude**: "I'm having trouble with the export-conversation skill..."

## Next Steps

Now that you know how to use the skill:

1. Export your first conversation
2. Review the output format
3. Customize summaries if needed
4. Set up a regular export schedule
5. Share exports with your team

Happy exporting!