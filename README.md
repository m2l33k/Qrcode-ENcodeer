# QR code encoder/coder
# QR Code Encoder

A simple QR Code Encoder application built using Python. This app allows users to generate QR codes from text input. It uses the `qrcode` library for QR code generation and the `PIL` library for image handling.

## Features

- Encode text into QR codes.
- Save generated QR codes as image files.
- Easy-to-use graphical user interface (GUI) built with Tkinter.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/m2l33k/QR-Code-Encoder.git
    cd QR-Code-Encoder
    ```

2. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

3. **Install Dependencies**: Install the required Python libraries:

    ```bash
    pip install qrcode[pil] pillow
    ```

4. **Run the Application**: Execute the Python script to start the QR Code Encoder:

    ```bash
    python qr_code_encoder.py
    ```

## Code Overview

The `qr_code_encoder.py` script includes the following key components:

- **Tkinter GUI**: Provides an interface for inputting text and generating QR codes.
- **QR Code Generation**: Uses the `qrcode` library to create QR codes from the provided text.
- **Image Handling**: Utilizes the `Pillow` library for image handling and saving.
