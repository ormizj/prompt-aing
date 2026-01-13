# Export Conversation Skill

A Claude Code skill that exports conversation history to structured Excel files.

## Overview

This skill allows you to export your Claude Code conversations to Excel format with three columns:
- **Prompt**: The user's input/question
- **Summary**: A concise summary of what was accomplished
- **Output**: The full assistant response

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install openpyxl
   ```

2. **Invoke the Skill**:
   ```
   /export-conversation
   ```
   Or simply ask: "Export this conversation to Excel"

3. **Get Your Export**:
   The skill will create a timestamped Excel file (e.g., `conversation-export-2026-01-12-143052.xlsx`) in your working directory.

## Files

- **[SKILL.md](SKILL.md)**: Complete skill documentation and workflow
- **[scripts/export_conversation.py](scripts/export_conversation.py)**: Python utility for Excel generation
- **[EXAMPLES.md](EXAMPLES.md)**: Example conversations and export formats
- **[sample_data.json](sample_data.json)**: Sample conversation data for testing

## Requirements

- Python 3.6+
- openpyxl library
- Write permissions in working directory

## Testing

Test the export script with sample data:

```bash
cd scripts
python export_conversation.py ../sample_data.json
```

This will create a test Excel file to verify the installation works correctly.

## Features

- Automatic timestamp generation
- Formatted Excel output with colors and styling
- Handles long text with automatic wrapping
- Supports Unicode and special characters
- Truncates extremely long responses to fit Excel limits
- Exports to CSV as fallback option

## Use Cases

- **Documentation**: Create records of development sessions
- **Knowledge Sharing**: Share conversations with team members
- **Archival**: Keep permanent records of AI-assisted work
- **Review**: Analyze patterns in how you use Claude Code
- **Teaching**: Create training materials from example conversations

## Example Output

The generated Excel file looks like this:

| Prompt | Summary | Output |
|--------|---------|--------|
| Create a Vue component | Created AccordionItem.vue with expand/collapse | I'll create an AccordionItem.vue component... [full response] |
| Fix the API error | Debugged JWT authentication issue | Let me check your API configuration... [full response] |

With professional formatting: blue headers, proper column widths, and text wrapping.

## Troubleshooting

See the [SKILL.md](SKILL.md) Troubleshooting section for common issues and solutions.

## License

Part of the Claude Code skills collection.