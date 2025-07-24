from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sympadding
from cryptography.hazmat.backends import default_backend
from image_hash_keygen import image_to_hash  # <-- New file where the hash function is defined
import os

def encrypt_file(file_path, key_hash):
    """Encrypt a file using a hash-derived key and AES CBC mode."""
    key = bytes.fromhex(key_hash)[:32]  # AES-256 key (32 bytes)
    iv = os.urandom(16)  # 16-byte IV

    # Read file content
    with open(file_path, 'rb') as f:
        data = f.read()

    # Add PKCS7 padding
    padder = sympadding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Encrypt
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Save IV + ciphertext
    with open(file_path, 'wb') as f:
        f.write(iv + ciphertext)

    print("[+] Encryption successful.")


def decrypt_file(file_path, key_hash):
    """Decrypt a file using the same image-derived key and AES CBC mode."""
    key = bytes.fromhex(key_hash)[:32]

    # Read IV and ciphertext
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    # Decrypt
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = sympadding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    # Overwrite with decrypted content
    with open(file_path, 'wb') as f:
        f.write(plaintext)

    print("[+] Decryption successful.")
