# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
  
app = QApplication([])
  
window = QWidget()
window.setWindowTitle('PythonDersleri.com')
txtLabel = QLabel('Python Dersleri')
btnButton = QPushButton('De�i�tir')
  
def changeTxtLabel():
    txtLabel.setText('Python ��reniyorum')
  
  
dizayn = QHBoxLayout()
dizayn.addWidget(txtLabel)
dizayn.addWidget(btnButton)

window.connect(btnButton, SIGNAL('pressed()'), changeTxtLabel)

window.setLayout(dizayn)
window.show()

app.exec_()