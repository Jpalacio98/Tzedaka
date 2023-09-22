import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi



class registrarClienteFormConfig(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = loadUi('app/views/registrarClienteForm2.ui',self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.btn_cerrar_2.clicked.connect(self.close)
        
        
        self.mouse_pressed = False
        self.old_pos = None

    def close(self):
        self.reject()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = True
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = False
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

# def registrarClienteFormConfig(self):
#     dialog = QDialog(self)
#     dialog = loadUi('Resource/Views/registrarClienteForm.ui',dialog)
#     dialog.setWindowFlag(Qt.FramelessWindowHint)
#     dialog.setAttribute(Qt.WA_TranslucentBackground)

#     dialog.exec()
    





