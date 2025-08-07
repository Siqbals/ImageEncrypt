# ImageEncrypt

**ImageEncrypt** is a fully offline, image-based file encryption and decryption system built with Python and PyQt5.  
Instead of traditional passwords, this application uses an **image file as the encryption key**, meaning only the exact same image can decrypt the file.

---

## How It Works

- Drag & Drop Interface: Use the GUI to drop your file and image key for encryption or decryption.
- Image-Derived Key: The image is preprocessed and hashed using SHA-256 to generate a secure AES key.
- AES-256 Encryption: Files are encrypted and decrypted using AES in CBC mode with PKCS7 padding.
- Fully Offline: No data is uploaded or stored anywhere—everything runs locally.

---

## Why Use an Image as a Key?

Instead of memorizing complex passwords, simply use an image.  
The system extracts pixel-level data from the image and converts it into a cryptographic key.  
Even a small change in the image (like resizing or filtering) will generate a completely different key—ensuring high security.

---

## Features

- Image-based AES-256 encryption & decryption
- Drag-and-drop PyQt5 GUI
- Real-time error and success messages
- Fully offline – zero network dependency
- Open source and customizable

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ImageEncrypt.git
cd ImageEncrypt

### 2. Install dependencies
```bash
pip install pyqt5 cryptography opencv-python numpy matplotlib

### 3. Run the App 
```bash
python display.py
