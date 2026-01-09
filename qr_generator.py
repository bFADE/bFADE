import qrcode
from PIL import Image, ImageDraw
import sys

# Colors
QR_COLOR = "#162b96"  # Deep blue
CREAM_BG = "#f6f2ea"  # Soft cream background

def generate_rounded_qr(
    qr_data: str,
    output_filename: str = "styled_qr_rounded_cream.png",
    qr_color: str = QR_COLOR,
    bg_color: str = CREAM_BG,
    box_size: int = 20,
    border: int = 4,
    corner_radius: int = 40
):
    """
    Generate a QR code with rounded corners and custom colors.

    Args:
        qr_data: The data to encode in the QR code (URL, text, etc.)
        output_filename: Name of the output PNG file
        qr_color: Color for the QR code modules (hex format)
        bg_color: Background color (hex format)
        box_size: Size of each QR code box in pixels
        border: Border size in boxes
        corner_radius: Radius for rounded corners in pixels

    Returns:
        PIL.Image: The generated QR code image
    """
    if not qr_data or qr_data.strip() == "":
        raise ValueError("QR data cannot be empty")

    # Create QR code instance
    qr = qrcode.QRCode(
        version=4,  # Controls the size (1-40, None for auto)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=box_size,
        border=border,
    )

    # Add data and generate
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create the QR image
    img = qr.make_image(
        fill_color=qr_color,
        back_color=bg_color
    ).convert("RGBA")

    # Create rounded mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        (0, 0, img.size[0], img.size[1]),
        radius=corner_radius,
        fill=255
    )

    # Apply mask for rounded corners
    img.putalpha(mask)

    # Save the image
    img.save(output_filename, "PNG")
    print(f"✓ QR code saved as: {output_filename}")
    print(f"  Size: {img.size[0]}x{img.size[1]} pixels")

    return img


def main():
    """Main function to run from command line."""
    if len(sys.argv) < 2:
        print("Usage: python qr_generator.py <data> [output_filename]")
        print("\nExample:")
        print('  python qr_generator.py "https://example.com"')
        print('  python qr_generator.py "Hello World" my_qr.png')
        sys.exit(1)

    qr_data = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else "styled_qr_rounded_cream.png"

    try:
        generate_rounded_qr(qr_data, output_filename)
    except Exception as e:
        print(f"✗ Error generating QR code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
