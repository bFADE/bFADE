# QR Code Generator with Rounded Corners

A Python script to generate beautifully styled QR codes with rounded corners and custom colors.

## Features

- 🎨 Custom colors (deep blue QR on soft cream background)
- ⭕ Rounded corners for a modern, polished look
- 🔧 Configurable parameters (size, border, corner radius)
- 📱 High error correction for better scanning reliability
- 💻 Simple command-line interface

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line

Generate a QR code from the command line:

```bash
# Basic usage with URL
python qr_generator.py "https://example.com"

# Custom output filename
python qr_generator.py "Hello World" my_custom_qr.png
```

### As a Python Module

```python
from qr_generator import generate_rounded_qr

# Generate QR code
generate_rounded_qr(
    qr_data="https://example.com",
    output_filename="my_qr.png"
)

# With custom settings
generate_rounded_qr(
    qr_data="Your text here",
    output_filename="custom_qr.png",
    qr_color="#162b96",
    bg_color="#f6f2ea",
    box_size=20,
    border=4,
    corner_radius=40
)
```

## Customization

- **qr_color**: Color of the QR code modules (hex format, e.g., "#162b96")
- **bg_color**: Background color (hex format, e.g., "#f6f2ea")
- **box_size**: Size of each QR box in pixels (default: 20)
- **border**: Border width in boxes (default: 4)
- **corner_radius**: Corner roundness in pixels (default: 40)

## Examples

```bash
# Generate QR for a website
python qr_generator.py "https://github.com"

# Generate QR with contact info
python qr_generator.py "mailto:hello@example.com"

# Generate QR for WiFi
python qr_generator.py "WIFI:T:WPA;S:NetworkName;P:Password;;"
```

## Output

The script generates a PNG file with:
- Transparent rounded corners (RGBA format)
- High error correction (can still scan even if 30% damaged)
- Professional appearance suitable for printing or digital use

## Requirements

- Python 3.7+
- qrcode library with PIL support
- Pillow (PIL fork)
