from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout
)
from PyQt5.QtCore import Qt


app = QApplication([])


#the window itself 
window = QWidget()
window.setWindowTitle("Iris Encrypt v1")
window.setFixedSize(800, 500) 
window.setStyleSheet("background-color: black;")

#all menu container 
allmenu = QStackedLayout()

'''Window 1, the encrypt and decrypt menu'''
#main page layout 
homemenu = QVBoxLayout()

#iris text label 
title = QLabel("Iris Encrypt v1")
title.setStyleSheet("color: lime; font-size: 24px; font-weight: bold;")
title.setAlignment(Qt.AlignLeft)

#description
desc = QLabel("Welcome to Iris Encrypt v1, a place to securly encrypt any file using your Iris!" "\n"
"To get started, press encrypt file if you would like to encrypt a file or decrypt file if you would like to decrypt a file ")
desc.setStyleSheet("color: white; font-size: 14px;")
desc.setAlignment(Qt.AlignLeft)

#encrypt btn 
encryptbtn = QPushButton("Encrypt")
encryptbtn.setStyleSheet("background-color: green; color: white; font-weight: bold;")
encryptbtn.setFixedHeight(40)

#decrypt btn
decryptbtn = QPushButton("Decrypt")
decryptbtn.setStyleSheet("background-color: darkred; color: white; font-weight: bold;")
decryptbtn.setFixedHeight(40)

#layout container for the btns 
btncont = QHBoxLayout()
btncont.addWidget(encryptbtn)
btncont.addWidget(decryptbtn)

#add everything to the window 
homemenu = QVBoxLayout()
homemenu.addWidget(title)
homemenu.addWidget(desc)
homemenu.addSpacing(20)
homemenu.addLayout(btncont)
homemenu.addStretch()


'''encrypt menu'''
encryptmenu = QVBoxLayout()

#encrypt title text
encrypttitle = QLabel("Encryption Panel")
encrypttitle.setStyleSheet("color: lime; font-size: 20px; font-weight: bold;")
encrypttitle.setAlignment(Qt.AlignLeft)

#description
encryptdesc = QLabel("To get started, drag and drop your desired file on the Left \n then drag and drop your image of your iris on the right ")
encryptdesc.setStyleSheet("color: white; font-size: 14px;")
encryptdesc.setAlignment(Qt.AlignLeft)

#the back button
backbtn = QPushButton("Back")
backbtn.setStyleSheet("background-color: gray; color: white; font-weight: bold;")

#add the things to the encrypt menu
encryptmenu.addWidget(encrypttitle)
encryptmenu.addWidget(encryptdesc)
encryptmenu.addStretch()
encryptmenu.addWidget(backbtn)

#first drag and drop box for the Iris 







#add the entire menu to the container 
encryptcont = QWidget()
encryptcont.setLayout(encryptmenu)







#final window settings 
homecont = QWidget()
homecont.setLayout(homemenu)
allmenu.addWidget(homecont)
allmenu.addWidget(encryptcont)

encryptbtn.clicked.connect(lambda: allmenu.setCurrentIndex(1))
backbtn.clicked.connect(lambda: allmenu.setCurrentIndex(0))

window.setLayout(allmenu)
window.show()
app.exec_()
