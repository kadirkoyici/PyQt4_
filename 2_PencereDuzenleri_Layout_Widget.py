# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
 
uygulamam = QApplication([])

etiket = QLabel('PythonDersleri.com')
buton = QPushButton('Butonum') 

yatayKutu = QHBoxLayout()
yatayKutu.addWidget(etiket)
yatayKutu.addWidget(buton)

pencere = QWidget() 
pencere.setLayout(yatayKutu)
pencere.setWindowTitle('Program�m')
pencere.show()
 
uygulamam.exec_()