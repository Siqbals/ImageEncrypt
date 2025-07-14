from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout,
    QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt

#drag and drop region class 
class FileDropBox(QLabel):
    def __init__(self, text="Drop file here", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(
            "border: 2px dashed white; color: gray; font-size: 14px; padding: 20px;"
        )
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.dropped_file_path = None

    #event to accept a drop 
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    #once click released have the file url here 
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            file_url = event.mimeData().urls()[0]
            self.dropped_file_path = file_url.toLocalFile()
            self.setText(f"Selected file:\n{self.dropped_file_path}")


app = QApplication([])

#main window settings 
window = QWidget()
window.setWindowTitle("Iris Encrypt v1")
window.setFixedSize(800, 500)
window.setStyleSheet("background-color: black;")

#all 3 menu windows container 
allmenu = QStackedLayout()

#home menu
homemenu = QVBoxLayout()

#title 
title = QLabel("Iris Encrypt v1")
title.setStyleSheet("color: lime; font-size: 24px; font-weight: bold;")
title.setAlignment(Qt.AlignLeft)

#description
desc = QLabel(
    "Welcome to Iris Encrypt v1, a place to securely encrypt any file using your iris!\n"
    "To get started, press Encrypt if you'd like to encrypt a file, or Decrypt to decrypt one."
)
desc.setStyleSheet("color: white; font-size: 14px;")
desc.setAlignment(Qt.AlignLeft)

#encrypt and de crypt buttons 
encryptbtn = QPushButton("Encrypt")
encryptbtn.setStyleSheet("background-color: green; color: white; font-weight: bold;")
encryptbtn.setFixedHeight(40)

decryptbtn = QPushButton("Decrypt")
decryptbtn.setStyleSheet("background-color: darkred; color: white; font-weight: bold;")
decryptbtn.setFixedHeight(40)

#btn containers to have horizontal layout 
btncont = QHBoxLayout()
btncont.addWidget(encryptbtn)
btncont.addWidget(decryptbtn)

#add averything to the home menu layout 
homemenu.addWidget(title)
homemenu.addWidget(desc)
homemenu.addSpacing(20)
homemenu.addLayout(btncont)
homemenu.addStretch()

homecont = QWidget()
homecont.setLayout(homemenu)

#encrypt menu 
encryptmenu = QVBoxLayout()

#encrypt title 
encrypttitle = QLabel("Encryption Panel")
encrypttitle.setStyleSheet("color: lime; font-size: 20px; font-weight: bold;")
encrypttitle.setAlignment(Qt.AlignLeft)

#encrypt description
encryptdesc = QLabel(
    "To get started, drag and drop your desired file on the left\n"
    "Then drag and drop your image of your iris on the right."
)
encryptdesc.setStyleSheet("color: white; font-size: 14px;")
encryptdesc.setAlignment(Qt.AlignLeft)

#drop the file on left 
file_drop = FileDropBox("Drop file here")
file_drop.setFixedSize(375, 300)

#drop the file on right 
iris_drop = FileDropBox("Drop iris image here")
iris_drop.setFixedSize(375, 300)

#back button on bottom row 
bottom_row = QHBoxLayout()
bottom_row.addWidget(file_drop)
bottom_row.addStretch()
bottom_row.addWidget(iris_drop)
backbtn = QPushButton("Back")
backbtn.setStyleSheet("background-color: gray; color: white; font-weight: bold;")

#add aeverything to the encrypt menu layout 
encryptmenu.addWidget(encrypttitle)
encryptmenu.addWidget(encryptdesc)
encryptmenu.addStretch()
encryptmenu.addLayout(bottom_row)
encryptmenu.addWidget(backbtn)

#add everything to the encrypt layout container 
encryptcont = QWidget()
encryptcont.setLayout(encryptmenu)

#add everything to the all meny container 
allmenu.addWidget(homecont)
allmenu.addWidget(encryptcont)

#connect menu to buttons 
encryptbtn.clicked.connect(lambda: allmenu.setCurrentIndex(1))
backbtn.clicked.connect(lambda: allmenu.setCurrentIndex(0))


#create the window 
window.setLayout(allmenu)
window.show()
app.exec_()
