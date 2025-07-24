from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout
)
from PyQt5.QtCore import Qt, pyqtSignal
import os

from image_hash_keygen import image_to_hash
from encryptionfunc import encrypt_file, decrypt_file  # Your AES file encrypt/decrypt module


class FileDropBox(QLabel):
    file_dropped = pyqtSignal()

    def __init__(self, text="Drop file here", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(
            "border: 2px dashed white; color: gray; font-size: 14px; padding: 20px;"
        )
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.dropped_file_path = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            file_url = event.mimeData().urls()[0]
            self.dropped_file_path = file_url.toLocalFile()
            self.setText(f"Selected file:\n{self.dropped_file_path}")
            self.file_dropped.emit()


app = QApplication([])

window = QWidget()
window.setWindowTitle("Image Encrypt v1")
window.setFixedSize(800, 500)
window.setStyleSheet("background-color: black;")

allmenu = QStackedLayout()

# ---------- Home Menu ----------
homemenu = QVBoxLayout()

title = QLabel("Image Encrypt v1")
title.setStyleSheet("color: lime; font-size: 24px; font-weight: bold;")
title.setAlignment(Qt.AlignLeft)

desc = QLabel(
    "Welcome to Image Encrypt v1, a place to securely encrypt any file using an image!\n"
    "To get started, press Encrypt if you'd like to encrypt a file, or Decrypt to decrypt one."
)
desc.setStyleSheet("color: white; font-size: 14px;")
desc.setAlignment(Qt.AlignLeft)

encryptbtn = QPushButton("Encrypt")
encryptbtn.setStyleSheet("background-color: green; color: white; font-weight: bold;")
encryptbtn.setFixedHeight(40)

decryptbtn = QPushButton("Decrypt")
decryptbtn.setStyleSheet("background-color: darkred; color: white; font-weight: bold;")
decryptbtn.setFixedHeight(40)

btncont = QHBoxLayout()
btncont.addWidget(encryptbtn)
btncont.addWidget(decryptbtn)

homemenu.addWidget(title)
homemenu.addWidget(desc)
homemenu.addSpacing(20)
homemenu.addLayout(btncont)
homemenu.addStretch()

homecont = QWidget()
homecont.setLayout(homemenu)

# ---------- Encrypt Menu ----------
encryptmenu = QVBoxLayout()

encrypttitle = QLabel("Encryption Panel")
encrypttitle.setStyleSheet("color: lime; font-size: 20px; font-weight: bold;")
encrypttitle.setAlignment(Qt.AlignLeft)

encryptdesc = QLabel(
    "To get started, drag and drop your desired file on the left\n"
    "Then drag and drop your image on the right."
)
encryptdesc.setStyleSheet("color: white; font-size: 14px;")
encryptdesc.setAlignment(Qt.AlignLeft)

file_drop = FileDropBox("Drop file here")
file_drop.setFixedSize(375, 300)

image_drop = FileDropBox("Drop image key here")
image_drop.setFixedSize(375, 300)

bottom_row = QHBoxLayout()
bottom_row.addWidget(file_drop)
bottom_row.addStretch()
bottom_row.addWidget(image_drop)

encrypt_action_btn = QPushButton("Encrypt")
encrypt_action_btn.setStyleSheet("background-color: green; color: white; font-weight: bold;")
encrypt_action_btn.setVisible(False)

error_label = QLabel("Error")
error_label.setStyleSheet("color: red; font-size: 14px;")
error_label.setVisible(False)

success_label = QLabel("Encryption successful!")
success_label.setStyleSheet("color: limegreen; font-size: 14px;")
success_label.setVisible(False)


backbtn = QPushButton("Back")
backbtn.setStyleSheet("background-color: gray; color: white; font-weight: bold;")


# ---------- Decrypt Menu ----------
decryptmenu = QVBoxLayout()

decrypttitle = QLabel("Decryption Panel")
decrypttitle.setStyleSheet("color: lime; font-size: 20px; font-weight: bold;")
decrypttitle.setAlignment(Qt.AlignLeft)

decryptdesc = QLabel(
    "To decrypt a file, drop the encrypted file on the left\n"
    "Then drop the original image used for encryption on the right."
)
decryptdesc.setStyleSheet("color: white; font-size: 14px;")
decryptdesc.setAlignment(Qt.AlignLeft)

decrypt_file_drop = FileDropBox("Drop encrypted file here")
decrypt_file_drop.setFixedSize(375, 300)

decrypt_image_drop = FileDropBox("Drop image key here")
decrypt_image_drop.setFixedSize(375, 300)

decrypt_bottom_row = QHBoxLayout()
decrypt_bottom_row.addWidget(decrypt_file_drop)
decrypt_bottom_row.addStretch()
decrypt_bottom_row.addWidget(decrypt_image_drop)

decrypt_action_btn = QPushButton("Decrypt")
decrypt_action_btn.setStyleSheet("background-color: darkred; color: white; font-weight: bold;")
decrypt_action_btn.setVisible(False)

decrypt_error_label = QLabel("Error")
decrypt_error_label.setStyleSheet("color: red; font-size: 14px;")
decrypt_error_label.setVisible(False)

decrypt_success_label = QLabel("decryption successful!")
decrypt_success_label.setStyleSheet("color: limegreen; font-size: 14px;")
decrypt_success_label.setVisible(False)

decrypt_backbtn = QPushButton("Back")
decrypt_backbtn.setStyleSheet("background-color: gray; color: white; font-weight: bold;")



# ---------- Button Handlers ----------
def update_encrypt_button():
    if file_drop.dropped_file_path and image_drop.dropped_file_path:
        encrypt_action_btn.setVisible(True)


def handle_encrypt():
    error_label.setVisible(False)
    file_path = file_drop.dropped_file_path
    image_path = image_drop.dropped_file_path

    if not file_path or not os.path.exists(file_path):
        error_label.setText("No file selected.")
        error_label.setVisible(True)
        return

    if not image_path or not os.path.exists(image_path):
        error_label.setText("No image key provided.")
        error_label.setVisible(True)
        return

    try:
        key_hash = image_to_hash(image_path)
        encrypt_file(file_path, key_hash)
        print("[+] Encryption complete.")
        success_label.setText("encryption successful!")
        success_label.setVisible(True)
    except Exception as e:
        error_label.setText(f"Encryption error: {e}")
        error_label.setVisible(True)


def update_decrypt_button():
    if decrypt_file_drop.dropped_file_path and decrypt_image_drop.dropped_file_path:
        decrypt_action_btn.setVisible(True)


def handle_decrypt():
    decrypt_error_label.setVisible(False)
    decrypt_success_label.setVisible(False)

    file_path = decrypt_file_drop.dropped_file_path
    image_path = decrypt_image_drop.dropped_file_path

    if not file_path or not os.path.exists(file_path):
        decrypt_error_label.setText("No file selected.")
        decrypt_error_label.setVisible(True)
        return

    if not image_path or not os.path.exists(image_path):
        decrypt_error_label.setText("No image key provided.")
        decrypt_error_label.setVisible(True)
        return

    try:
        key_hash = image_to_hash(image_path)
        decrypt_file(file_path, key_hash)
        print("[+] Decryption complete.")
        decrypt_success_label.setText("decryption successful!")
        decrypt_success_label.setVisible(True)
    except Exception as e:
        decrypt_error_label.setText(f"Decryption error: {e}")
        decrypt_error_label.setVisible(True)



# ---------- Connect Signals ----------
file_drop.file_dropped.connect(update_encrypt_button)
image_drop.file_dropped.connect(update_encrypt_button)

encryptbtn.clicked.connect(lambda: allmenu.setCurrentIndex(1))
decryptbtn.clicked.connect(lambda: allmenu.setCurrentIndex(2))
encrypt_action_btn.clicked.connect(handle_encrypt)
backbtn.clicked.connect(lambda: allmenu.setCurrentIndex(0))

decrypt_file_drop.file_dropped.connect(update_decrypt_button)
decrypt_image_drop.file_dropped.connect(update_decrypt_button)
decrypt_action_btn.clicked.connect(handle_decrypt)
decrypt_backbtn.clicked.connect(lambda: allmenu.setCurrentIndex(0))



# ---------- Assemble Encrypt Menu ----------
encryptmenu.addWidget(encrypttitle)
encryptmenu.addWidget(encryptdesc)
encryptmenu.addStretch()
encryptmenu.addLayout(bottom_row)
encryptmenu.addWidget(encrypt_action_btn)
encryptmenu.addWidget(error_label)
encryptmenu.addWidget(backbtn)
encryptmenu.addWidget(success_label)


encryptcont = QWidget()
encryptcont.setLayout(encryptmenu)

# ---------- Assemble Dencrypt Menu ----------
decryptmenu.addWidget(decrypttitle)
decryptmenu.addWidget(decryptdesc)
decryptmenu.addStretch()
decryptmenu.addLayout(decrypt_bottom_row)
decryptmenu.addWidget(decrypt_action_btn)
decryptmenu.addWidget(decrypt_error_label)
decryptmenu.addWidget(decrypt_backbtn)
decryptmenu.addWidget(decrypt_success_label)

decryptcont = QWidget()
decryptcont.setLayout(decryptmenu)

# ---------- Add Pages to Stack ----------
allmenu.addWidget(homecont)
allmenu.addWidget(encryptcont)
allmenu.addWidget(decryptcont)

window.setLayout(allmenu)
window.show()
app.exec_()
