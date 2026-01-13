# Export Conversation - Quick Reference

## Installation (One-Time)
```bash
pip install openpyxl
```

## Usage

### Invoke the Skill
```
/export-conversation
```

Or just ask: `"Export this conversation to Excel"`

### Manual Export
```bash
python scripts/export_conversation.py conversation_data.json
python scripts/export_conversation.py data.json output.xlsx
```

## Output Format

| Prompt | Summary | Output |
|--------|---------|--------|
| User's question | What was accomplished | Full response |

## File Structure

```
export-conversation/
├── SKILL.md              # Complete documentation
├── USAGE.md              # Step-by-step guide
├── EXAMPLES.md           # Sample conversations
├── README.md             # Overview
├── QUICKREF.md           # This file
├── sample_data.json      # Test data
└── scripts/
    ├── export_conversation.py  # Main script
    └── test_export.py          # Testing utility
```

## Common Commands

### Test Installation
```bash
python scripts/test_export.py
```

### Check Dependencies
```bash
python --version
python -c "import openpyxl; print(openpyxl.__version__)"
```

### Manual Data Creation
```python
import json

data = {
    "conversation": [
        {
            "prompt": "Question",
            "summary": "What happened",
            "output": "Full response"
        }
    ]
}

with open("my_data.json", "w") as f:
    json.dump(data, f, indent=2)
```

## Summary Guidelines

**Good**:
- "Created Vue component with accordion functionality"
- "Fixed JWT authentication in API middleware"
- "Explained async/await with practical examples"

**Bad**:
- "Made changes" (too vague)
- "Fixed bug" (which bug?)
- "Helped user" (not specific)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Python not found | Install from python.org |
| openpyxl missing | `pip install openpyxl` |
| Permission error | Check file/directory permissions |
| File already open | Close Excel first |
| Text truncated | Normal for >32K chars per cell |

## Output Location

Files are saved in your current working directory with format:
```
conversation-export-2026-01-12-143052.xlsx
```

## Requirements

- Python 3.6+
- openpyxl library
- Write permissions in current directory

## Alternative: CSV Export

If Excel isn't working:
```python
import csv

with open('export.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Prompt', 'Summary', 'Output'])
    for turn in data:
        writer.writerow([turn['prompt'], turn['summary'], turn['output']])
```

## Tips

1. Clear prompts make better exports
2. Edit summaries after export for clarity
3. Use timestamped filenames to avoid overwrites
4. Review exports before sharing
5. Keep exports organized by project/date

## Getting Help

- Read: [SKILL.md](SKILL.md) for full documentation
- Read: [USAGE.md](USAGE.md) for detailed workflows
- Read: [EXAMPLES.md](EXAMPLES.md) for sample outputs
- Test: Run `python scripts/test_export.py`
- Ask: Claude Code for troubleshooting help