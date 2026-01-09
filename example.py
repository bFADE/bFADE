#!/usr/bin/env python3
"""
Example usage of the QR code generator.
Run this file to see different QR code generation examples.
"""

from qr_generator import generate_rounded_qr

def main():
    """Generate example QR codes."""

    # Example 1: Website URL
    print("Generating QR for website URL...")
    generate_rounded_qr(
        qr_data="https://github.com/bFADE/bFADE",
        output_filename="example_website.png"
    )

    # Example 2: Contact card (vCard format)
    print("\nGenerating QR for contact card...")
    vcard = """BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL:+1-555-123-4567
EMAIL:john@example.com
END:VCARD"""
    generate_rounded_qr(
        qr_data=vcard,
        output_filename="example_contact.png"
    )

    # Example 3: WiFi network (auto-connect)
    print("\nGenerating QR for WiFi...")
    generate_rounded_qr(
        qr_data="WIFI:T:WPA;S:MyNetwork;P:MyPassword123;;",
        output_filename="example_wifi.png"
    )

    # Example 4: Custom colors
    print("\nGenerating QR with custom colors...")
    generate_rounded_qr(
        qr_data="Custom styled QR code",
        output_filename="example_custom.png",
        qr_color="#d32f2f",  # Red
        bg_color="#fff3e0",  # Light orange
        corner_radius=60
    )

    print("\n✓ All examples generated successfully!")
    print("Check the generated PNG files in this directory.")


if __name__ == "__main__":
    main()
