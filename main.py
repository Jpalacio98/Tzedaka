import sys
from app.views import configLogin2, configHome, configWork
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import pyrebase


class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InicializarGUI()

    def InicializarGUI(self):
        # ---------------------declaracion de variables-----------------------
        configLogin2.loginConfig(self)
        # configHome.homeConfig(self)
        # configWork.workConfig(self)

    def close(self):
        sys.exit()

    def minimizar(self):
        self.showMinimized()

    def restablecer(self):
        if self.estado:
            self.showNormal()
            self.btn_minmax.setStyleSheet("border-image: url(:/source/maximizar.png);")
            self.estado = False
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


def initialize_firebase():
    # Ruta al archivo de credenciales descargado
    cred = {
        "apiKey": "AIzaSyAnE6WxkeYDZ9Oro8moJUbTDWwML2VtdyY",
        "authDomain": "tzedaka-db.firebaseapp.com",
        "databaseURL": "https://tzedaka-db-default-rtdb.firebaseio.com",
        "projectId": "tzedaka-db",
        "storageBucket": "tzedaka-db.appspot.com",
        "messagingSenderId": "818074652781",
        "appId": "1:818074652781:web:d4f7c6b994745a5a59af64",
        "measurementId": "G-0Y4L73XMB7",
    }

    firebase=pyrebase.initialize_app(cred)

def main():
    initialize_firebase()
    windows = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()

    sys.exit(windows.exec_())


if __name__ == "__main__":
    main()
