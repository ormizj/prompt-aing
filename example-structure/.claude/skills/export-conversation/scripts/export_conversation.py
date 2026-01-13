#!/usr/bin/env python3
"""
Conversation to Excel Exporter
Converts conversation JSON data to a formatted Excel file with Prompt, Summary, and Output columns.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
except ImportError:
    print("ERROR: openpyxl is not installed.")
    print("Please install it with: pip install openpyxl")
    sys.exit(1)


# Excel cell character limit
EXCEL_CELL_LIMIT = 32767


def truncate_text(text: str, max_length: int = EXCEL_CELL_LIMIT) -> str:
    """Truncate text to fit within Excel cell limits."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 15] + "\n\n[...truncated]"


def create_excel_file(conversation_data: List[Dict[str, str]], output_path: str) -> None:
    """
    Create an Excel file from conversation data.

    Args:
        conversation_data: List of dicts with 'prompt', 'summary', 'output' keys
        output_path: Path where the Excel file should be saved
    """
    # Create a new workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Conversation Export"

    # Define column headers
    headers = ["Prompt", "Summary", "Output"]

    # Style for headers
    header_font = Font(name='Arial', size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # Write and style headers
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num)
        cell.value = header
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment

    # Style for data cells
    data_font = Font(name='Arial', size=10)
    data_alignment = Alignment(vertical="top", wrap_text=True)

    # Write conversation data
    for row_num, turn in enumerate(conversation_data, 2):
        # Prompt column
        prompt_cell = ws.cell(row=row_num, column=1)
        prompt_cell.value = truncate_text(turn.get('prompt', ''))
        prompt_cell.font = data_font
        prompt_cell.alignment = data_alignment

        # Summary column
        summary_cell = ws.cell(row=row_num, column=2)
        summary_cell.value = truncate_text(turn.get('summary', ''))
        summary_cell.font = data_font
        summary_cell.alignment = data_alignment

        # Output column
        output_cell = ws.cell(row=row_num, column=3)
        output_cell.value = truncate_text(turn.get('output', ''))
        output_cell.font = data_font
        output_cell.alignment = data_alignment

    # Set column widths (in character units)
    ws.column_dimensions['A'].width = 40  # Prompt
    ws.column_dimensions['B'].width = 50  # Summary
    ws.column_dimensions['C'].width = 80  # Output

    # Freeze the header row
    ws.freeze_panes = 'A2'

    # Save the workbook
    wb.save(output_path)
    print(f"Excel file created successfully: {output_path}")


def load_conversation_data(json_path: str) -> List[Dict[str, str]]:
    """
    Load conversation data from JSON file.

    Args:
        json_path: Path to JSON file containing conversation data

    Returns:
        List of conversation turns
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Support both direct list format and nested format
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'conversation' in data:
            return data['conversation']
        else:
            print(f"ERROR: Invalid JSON format. Expected list or dict with 'conversation' key.")
            sys.exit(1)
    except FileNotFoundError:
        print(f"ERROR: File not found: {json_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON format: {e}")
        sys.exit(1)


def generate_output_filename() -> str:
    """Generate a timestamped output filename."""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    return f"conversation-export-{timestamp}.xlsx"


def main():
    """Main entry point for the script."""
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python export_conversation.py <conversation_data.json> [output_file.xlsx]")
        print("\nExample:")
        print("  python export_conversation.py conversation_data.json")
        print("  python export_conversation.py conversation_data.json my_export.xlsx")
        sys.exit(1)

    # Load input data
    input_path = sys.argv[1]
    conversation_data = load_conversation_data(input_path)

    # Determine output path
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = generate_output_filename()

    # Validate data
    if not conversation_data:
        print("WARNING: No conversation data to export.")
        sys.exit(0)

    # Create Excel file
    create_excel_file(conversation_data, output_path)

    # Print summary
    print(f"\nExport Summary:")
    print(f"  - Conversation turns: {len(conversation_data)}")
    print(f"  - Output file: {Path(output_path).absolute()}")
    print(f"  - File size: {Path(output_path).stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()