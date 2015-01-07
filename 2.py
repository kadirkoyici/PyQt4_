# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
 
uygulamam = QApplication([])

etiket = QLabel('PythonDersleri.com')
buton = QPushButton('Butonum') 
yatayKutu = QHBoxLayout()
pencere = QWidget() 


yatayKutu.addWidget(etiket)
yatayKutu.addWidget(buton)

pencere.setLayout(yatayKutu)
pencere.setWindowTitle('Programım')
pencere.show()
 
uygulamam.exec_()