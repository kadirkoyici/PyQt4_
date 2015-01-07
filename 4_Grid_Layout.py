# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
 
uygulama = QApplication([])
pencere = QWidget()
 
def kirmiziMetin():
    metin.setText('<center><font color="red" size="6">Merhaba Dunya :)</font></center>')
 
def maviMetin():
    metin.setText('<center><font color="blue" size="6">Kadir</font></center>')
 
metin = QLabel('<center><font color="green" size="6">PythonDersleri.com</font></center>')
 
butonKirmizi = QPushButton('Kirmizi')
pencere.connect(butonKirmizi, SIGNAL('pressed()'), kirmiziMetin)
 
butonMavi = QPushButton('Mavi')
pencere.connect(butonMavi, SIGNAL('pressed()'), maviMetin)
 
izgara = QGridLayout()
izgara.addWidget(metin, 0, 1, 2, 1)
izgara.addWidget(butonKirmizi, 0, 0)
izgara.addWidget(butonMavi, 1, 0)
 
pencere.setLayout(izgara)
pencere.setWindowTitle('PyQt Grid Layout')
pencere.setFixedSize(450, 150)
pencere.show()
 
uygulama.exec_()