
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

def workConfig(self):
    self.ui=loadUi('Resource/Views/work.ui',self)
    self.estado = True
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.btn_cerrar.clicked.connect(self.close)
    self.btn_minmax.clicked.connect(self.restablecer)
    self.btn_minimizar.clicked.connect(self.minimizar)
    self.showMaximized()