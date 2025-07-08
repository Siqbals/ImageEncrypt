from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sympadding
from cryptography.hazmat.backends import default_backend
from Irisencrypt import *
import hashlib, os

def derive_key_from_iris_signature(iris_hash: str) -> bytes:
    return bytes.fromhex(iris_hash)[:32]  # 32-byte AES key

def encrypt_file_in_place(file_path, iris_hash):
    key = derive_key_from_iris_signature(iris_hash)
    iv = os.urandom(16)

    # Read original file content
    with open(file_path, 'rb') as f:
        data = f.read()

    # Pad content
    padder = sympadding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Encrypt
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Overwrite file: store IV + ciphertext
    with open(file_path, 'wb') as f:
        f.write(iv + ciphertext)

    print(f"[+] File encrypted in-place: {file_path}")

def decrypt_file_in_place(file_path, iris_hash):
    key = derive_key_from_iris_signature(iris_hash)

    # Read IV + encrypted content
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    # Decrypt
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = sympadding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    # Overwrite file with plaintext
    with open(file_path, 'wb') as f:
        f.write(data)

    print(f"[+] File decrypted in-place: {file_path}")

    iris_hash = iris_signature_from_image("iristest.jpg")

iris_hash = iris_signature_from_image("iristest.jpg")

# Encrypt in-place
decrypt_file_in_place("r.txt", iris_hash)



