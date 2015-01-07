# -*- coding: utf-8 -*-
from PyQt4.QtGui import *

uygulama = QApplication([])

etiket = QLabel('Merhaba PyQt')
buton = QPushButton(" Cok Tiklama")
combo = QComboBox()
etiket.show()
buton.show()
combo.show()

uygulama.exec_()

'''
bu sekilde yaparsak sonuc olarak üst üste binmiş 3 pencere görürürüz

3 Nesne Oluşturduk :
    etiket = QLabel('Merhaba PyQt')
    buton = QPushButton()
    combo = QComboBox()
show komutu hepsi için ayrı ayrı oluşturulur

bunu ortadan kaldırmak için widget görsel programlamada bir kütüphanedeki grafik bileşenlere verilen ad 
Widget kullannnnnmalıyız

'''