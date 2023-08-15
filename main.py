import sys
from Resource.Images.resource import *
from datetime import datetime
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
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.frame.mouseMoveEvent = self.moveWindow
        self.btn_salir.clicked.connect(self.exit)
        self.obtenerFecha()
        timer = QTimer(self)
        timer.timeout.connect(self.mostrar_reloj)
        timer.start(1000)

    def mostrar_reloj(self):
        current_time = QTime.currentTime()
        hour = current_time.toString("hh:mm:ss AP")
        self.hora.setText(hour)

    def obtenerFecha(self):
        current_date = QDate.currentDate()
        formatted_date = current_date.toString("d 'de' MMMM 'de' yyyy")
        self.fecha.setText(formatted_date)

    def moveWindow(self, e):
        if e.buttons() == Qt.LeftButton:
            self.move(self.pos() + e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def exit(self):
        sys.exit()


def main():
    windows = QApplication(sys.argv)
    ventana= Aplicacion()
    ventana.show()

    sys.exit(windows.exec_())

if __name__ == "__main__":
    main()
