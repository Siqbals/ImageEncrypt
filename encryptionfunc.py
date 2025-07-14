from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sympadding
from cryptography.hazmat.backends import default_backend
from Irisencrypt import *
import os

def encrypt_file(file_path, iris_hash):
    key = bytes.fromhex(iris_hash)[:32]
    ran16 = os.urandom(16)

    # Read original file content
    with open(file_path, 'rb') as f:
        data = f.read()

    # add padding so AES works every time 
    padgen = sympadding.PKCS7(128).padder()
    repaddata = padgen.update(data) + padgen.finalize()

    # Encrypt generation
    cipher = Cipher(algorithms.AES(key), modes.CBC(ran16), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(repaddata) + encryptor.finalize()

    #apply encryption to the file
    with open(file_path, 'wb') as f:
        f.write(ran16 + ciphertext)

    print("encryption successful")

def decrypt_file(file_path, iris_hash):

    #use the same iris hash to get the stuff back
    key = bytes.fromhex(iris_hash)[:32]

    #get the ran16 and ciphertext
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    # Decrypt
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    #removing padding 
    unpadder = sympadding.PKCS7(128).unpadder()
    unpaddata = unpadder.update(padded_data) + unpadder.finalize()

    #replace file content with unecrypted versions 
    with open(file_path, 'wb') as f:
        f.write(unpaddata)

    print("decryption successful")

iris_hash = irissig("iristest.jpg")

# Encrypt in-place
decrypt_file("r.txt", iris_hash)



