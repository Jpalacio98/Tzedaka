import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from app.controllers.controllerUser import ControlUserAuth

def loginConfig(self):
    self.ui=loadUi('app/views/login2.ui',self)
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setAttribute(Qt.WA_TranslucentBackground)
    self.frame.mouseMoveEvent = self.moveWindow
    self.btn_salir.clicked.connect(self.close)
    self.btn_size.clicked.connect(lambda: change_size(self))
    self.ingresar.clicked.connect(lambda: iniciarsesion(self))
    self.btn_pass.clicked.connect(lambda:hidenpass(self) )
    obtenerFecha(self)
    timer = QTimer(self)
    timer.timeout.connect(lambda:mostrar_reloj(self))
    timer.start(1000)

   
def change_size(self):
    current_x = self.frame.x()
    if self.frame.width() == 91:
        new_x = current_x - 269
        new_width = self.frame.width() + 269
        self.btn_size.setStyleSheet("border-image: url(:/source/flechaR.png);")
    else:
        new_x = current_x + 269
        new_width = self.frame.width() - 269
        self.btn_size.setStyleSheet("border-image: url(:/source/flechaL.png);")
    self.frame.move(new_x, self.frame.y())
    self.frame.setFixedWidth(new_width)

def mostrar_reloj(self):
        current_time = QTime.currentTime()
        hour = current_time.toString("hh:mm:ss AP")
        self.hora.setText(hour)

def obtenerFecha(self):
    current_date = QDate.currentDate()
    formatted_date = current_date.toString("d 'de' MMMM 'de' yyyy")
    self.fecha.setText(formatted_date)

def hidenpass(self):
    if self.password.echoMode() == QLineEdit.Normal:
        self.password.setEchoMode(QLineEdit.Password)
        self.btn_pass.setIcon(QIcon(":/source/show.png"))
    else:
        self.password.setEchoMode(QLineEdit.Normal)
        self.btn_pass.setIcon(QIcon(":/source/hide.png"))

def iniciarsesion(self):
    print("Iniciar sesion")
    user=self.user.text
    password=self.password.text
    ControlUserAuth.ingresar_usuario(user,password)
    
