import sys
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
        self.ui=loadUi('Resource/Views/login2.ui',self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        pass
    

def main():
    windows = QApplication(sys.argv)
    ventana= Aplicacion()
    
    ventana.show()

    sys.exit(windows.exec_())

if __name__ == "__main__":
    main()
