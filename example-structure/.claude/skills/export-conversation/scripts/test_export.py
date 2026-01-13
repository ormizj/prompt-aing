#!/usr/bin/env python3
"""
Test script for conversation export functionality.
This script demonstrates how to use the export_conversation module.
"""

import json
from datetime import datetime
from pathlib import Path

# Sample conversation data for testing
test_conversation = [
    {
        "prompt": "Hello, can you help me with my Nuxt project?",
        "summary": "Initial greeting and project setup discussion",
        "output": "Of course! I'd be happy to help with your Nuxt project. What specifically would you like assistance with?"
    },
    {
        "prompt": "I need to create a user authentication system",
        "summary": "Planned authentication implementation with JWT and Pinia store",
        "output": "I'll help you implement a comprehensive authentication system. Here's what we'll create:\n\n1. API endpoints for login/register/logout\n2. Pinia store for auth state management\n3. Auth middleware for protected routes\n4. Login and registration forms\n\nLet's start with the API endpoints..."
    },
    {
        "prompt": "Can you also add password reset functionality?",
        "summary": "Added password reset flow with email verification and token validation",
        "output": "I'll add a complete password reset flow:\n\n1. Request reset endpoint (sends email)\n2. Verify token endpoint\n3. Update password endpoint\n4. Reset password form component\n\n[Implementation details follow...]"
    }
]

def create_test_data():
    """Create a test JSON file with conversation data."""
    data = {
        "export_date": datetime.now().isoformat(),
        "conversation": test_conversation
    }

    output_path = Path("test_conversation_data.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Created test data file: {output_path.absolute()}")
    return str(output_path)

def main():
    """Main test function."""
    print("=" * 60)
    print("Conversation Export Test Script")
    print("=" * 60)
    print()

    # Create test data
    test_file = create_test_data()
    print()

    # Try to import openpyxl
    try:
        import openpyxl
        print(f"✓ openpyxl is installed (version {openpyxl.__version__})")
        print()

        # Import the export module
        from export_conversation import create_excel_file, load_conversation_data

        # Load and export
        print("Loading conversation data...")
        conversation_data = load_conversation_data(test_file)
        print(f"Loaded {len(conversation_data)} conversation turns")
        print()

        output_file = f"test-export-{datetime.now().strftime('%Y%m%d-%H%M%S')}.xlsx"
        print(f"Creating Excel file: {output_file}")
        create_excel_file(conversation_data, output_file)
        print()

        print("=" * 60)
        print("✓ Test completed successfully!")
        print("=" * 60)
        print(f"\nYou can now open: {Path(output_file).absolute()}")

    except ImportError:
        print("✗ openpyxl is not installed")
        print()
        print("To install openpyxl, run:")
        print("  pip install openpyxl")
        print()
        print("After installation, run this test again to verify the export works.")

if __name__ == "__main__":
    main()