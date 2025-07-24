# === Imports ===
import cv2
import numpy as np
import hashlib
import matplotlib.pyplot as plt


#pre process the image itself 
def preprocess_image(image_path, to_gray=True, resize_dim=(128, 128)):
    """Load, optionally convert to grayscale, and resize the image."""
    flag = cv2.IMREAD_GRAYSCALE if to_gray else cv2.IMREAD_COLOR
    img = cv2.imread(image_path, flag)
    if img is None:
        raise ValueError(f"Image not found at path: {image_path}")
    img = cv2.resize(img, resize_dim)
    return img

#convert the entire image to a hash value 
def image_to_hash(image_path):
    try:
        img = preprocess_image(image_path)
        flattened = img.flatten()
        key_hash = hashlib.sha256(flattened.tobytes()).hexdigest()
        return key_hash
    except Exception as e:
        return f"[!] Error generating hash: {e}"

if __name__ == "__main__":
    image_path = "iristest.jpg"  # Replace with your image path
    key = image_to_hash(image_path)
    print("Generated Key (SHA-256 Hash):", key)


