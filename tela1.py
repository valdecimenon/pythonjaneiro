#tela1.py
#pip install pyqt5


from PyQt5.QtWidgets import *

app = QApplication([])

layout = QVBoxLayout()
layout.addWidget(QPushButton('Acima'))
layout.addWidget(QPushButton('Abaixo'))

window = QWidget()
window.setLayout(layout)
window.show()

app.exec_()

