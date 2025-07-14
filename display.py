from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


app = QApplication([])

#the window itself 
window = QWidget()
window.setWindowTitle("Iris Encrypt v1")
window.setFixedSize(800, 500) 
window.setStyleSheet("background-color: black;")

#iris text label 
title = QLabel("Iris Encrypt v1")
title.setStyleSheet("color: lime; font-size: 24px; font-weight: bold;")
title.setAlignment(Qt.AlignLeft)

#description
desc = QLabel("Welcome to Iris Encrypt v1, a place to securly encrypt any file using your Iris!" "\n"
"To get started, press encrypt file if you would like to encrypt a file or decrypt file if you would like to decrypt a file ")
desc.setStyleSheet("color: white; font-size: 14px;")
desc.setAlignment(Qt.AlignLeft)

#label positioning 
layout = QVBoxLayout()
layout.addWidget(title)
layout.addWidget(desc)
layout.addStretch()  # pushes content to top

window.setLayout(layout)
window.show()
app.exec_()
