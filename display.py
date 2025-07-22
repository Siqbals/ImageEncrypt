from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout,
    QSizePolicy
)
from PyQt5.QtCore import Qt, pyqtSignal

# ---------- Drag and Drop Widget ----------
class FileDropBox(QLabel):
    file_dropped = pyqtSignal()  # Signal emitted when a file is dropped

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

# ---------- Main Application ----------
app = QApplication([])

# ---------- Window Setup ----------
window = QWidget()
window.setWindowTitle("Iris Encrypt v1")
window.setFixedSize(800, 500)
window.setStyleSheet("background-color: black;")

allmenu = QStackedLayout()  # Layout stack to hold multiple screens

# ---------- Home Menu ----------
homemenu = QVBoxLayout()

title = QLabel("Iris Encrypt v1")
title.setStyleSheet("color: lime; font-size: 24px; font-weight: bold;")
title.setAlignment(Qt.AlignLeft)

desc = QLabel(
    "Welcome to Iris Encrypt v1, a place to securely encrypt any file using your iris!\n"
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
    "Then drag and drop your image of your iris on the right."
)
encryptdesc.setStyleSheet("color: white; font-size: 14px;")
encryptdesc.setAlignment(Qt.AlignLeft)

# File and Iris Drop Boxes
file_drop = FileDropBox("Drop file here")
file_drop.setFixedSize(375, 300)

iris_drop = FileDropBox("Drop iris image here")
iris_drop.setFixedSize(375, 300)

# Bottom layout: file box (left), iris box (right)
bottom_row = QHBoxLayout()
bottom_row.addWidget(file_drop)
bottom_row.addStretch()
bottom_row.addWidget(iris_drop)

# Encrypt button (initially hidden)
encrypt_action_btn = QPushButton("Encrypt")
encrypt_action_btn.setStyleSheet("background-color: green; color: white; font-weight: bold;")
encrypt_action_btn.setVisible(False)

# Back button
backbtn = QPushButton("Back")
backbtn.setStyleSheet("background-color: gray; color: white; font-weight: bold;")

# Check if both drop boxes are filled
def update_encrypt_button():
    if file_drop.dropped_file_path and iris_drop.dropped_file_path:
        encrypt_action_btn.setVisible(True)

# Connect signals
file_drop.file_dropped.connect(update_encrypt_button)
iris_drop.file_dropped.connect(update_encrypt_button)

# Add widgets to encrypt menu
encryptmenu.addWidget(encrypttitle)
encryptmenu.addWidget(encryptdesc)
encryptmenu.addStretch()
encryptmenu.addLayout(bottom_row)
encryptmenu.addWidget(encrypt_action_btn)
encryptmenu.addWidget(backbtn)

encryptcont = QWidget()
encryptcont.setLayout(encryptmenu)

# ---------- Add Screens to Main Layout ----------
allmenu.addWidget(homecont)
allmenu.addWidget(encryptcont)

# ---------- Navigation Logic ----------
encryptbtn.clicked.connect(lambda: allmenu.setCurrentIndex(1))
backbtn.clicked.connect(lambda: allmenu.setCurrentIndex(0))

# ---------- Final Window Setup ----------
window.setLayout(allmenu)
window.show()
app.exec_()
