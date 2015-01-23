# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class yavru(QDialog):
    def __init__(self,parent=None):
        super(yavru,self).__init__(parent)
        
        self.parent=parent
        #QDialog nesnesinin alttaki ana sınıftaki elemanlarına ulaşmak için
        self.setAttribute(Qt.WA_DeleteOnClose)
        
        self.liste=["Blue","Greem","Red","Yellow"]
        
        self.combom=QComboBox()
        self.combom.addItems(self.liste)
        self.butonum=QPushButton(u"Renk Değiştir")
        self.connect(self.butonum, SIGNAL("pressed()"),self.renkDegistir)
        
        
        pencerem=QGridLayout()
        pencerem.addWidget(self.combom,0,0)
        pencerem.addWidget(self.butonum,1,0)
        self.setLayout(pencerem)
        
    def renkDegistir(self):
        self.parent.renk=self.combom.currentText()
        self.parent.etiket.setText(self.parent.metin%self.parent.renk)

class ana(QDialog):
    def __init__(self,parent=None):
        super(ana,self).__init__(parent)
        
        self.renk="Green"
        self.metin='<center><font size="+6" color=%s>Deneme</font></center>'
        self.etiket=QLabel(self.metin%self.renk)
        self.butonum=QPushButton("Renk Degistir")
        self.connect(self.butonum, SIGNAL("pressed()"),self.yavru_cagir)
        izgara=QGridLayout()
        izgara.addWidget(self.etiket)
        izgara.addWidget(self.butonum)
        
        self.setLayout(izgara)
    def yavru_cagir(self):
        diyalog=yavru(self)
        #yavru(self)    self e çok dikkat
        diyalog.show()
        
uygulama=QApplication([])
pencere=ana()
pencere.show()
uygulama.exec_()
        
        
        
        
        
        
        