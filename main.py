import sys
from app.views import configLogin2, configHome, configWork
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi


class Aplicacion(QMainWindow):

    def __init__(self):
        super().__init__()
        self.InicializarGUI()

    def InicializarGUI(self):
        #---------------------declaracion de variables-----------------------
        #configLogin2.loginConfig(self)
        configHome.homeConfig(self)
        
        
        #configWork.workConfig(self)
       


    def close(self):
        sys.exit()
    
    def minimizar(self):
        self.showMinimized()
        
    def restablecer(self):
        if self.estado:
            self.showNormal()
            self.btn_minmax.setStyleSheet("border-image: url(:/source/maximizar.png);")
            self.estado=False
        else:
            self.btn_minmax.setStyleSheet("border-image: url(:/source/restaurar.png);")
            self.estado = True
            self.showMaximized()
 
    def moveWindow(self, e):
        if e.buttons() == Qt.LeftButton:
            self.move(self.pos() + e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


def main():
    windows = QApplication(sys.argv)
    ventana= Aplicacion()
    ventana.show()

    sys.exit(windows.exec_())

if __name__ == "__main__":
    main()
