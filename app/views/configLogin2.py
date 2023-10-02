import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from app.views import configHome
from data.services.serviceUser import UserService

class login(QMainWindow):
    def __init__(self, parent: QWidget | None ):
        super().__init__(parent)
        loadUi('app/views/login2.ui',parent)
        self.parent=parent
        self.userService = UserService()
        parent.setWindowFlags(Qt.FramelessWindowHint)
        parent.setAttribute(Qt.WA_TranslucentBackground)
        parent.frame.mouseMoveEvent = parent.moveWindow
        parent.btn_salir.clicked.connect(self.close)
        parent.btn_pass.clicked.connect(self.hidenpass)
        parent.ingresar.clicked.connect(self.iniciarsesion)
        self.obtenerFecha()
        timer = QTimer(parent)
        timer.timeout.connect(self.mostrar_reloj)
        timer.start(1000)
        parent.setMouseTracking(True)
        parent.enterEvent=self.enterEvent
        parent.leaveEvent=self.leaveEvent

    def close(self):
        sys.exit()
    
    def enterEvent(self, event):
        current_x = self.parent.frame.x()
        new_x = current_x - 269
        new_width = self.parent.frame.width() + 269
        self.parent.btn_size.setStyleSheet("border-image: url(:/source/flechaR.png);")
        self.parent.frame.move(new_x, self.parent.frame.y())
        self.parent.frame.setFixedWidth(new_width)

    def leaveEvent(self, event):
        current_x = self.parent.frame.x()
        new_x = current_x + 269
        new_width = self.parent.frame.width() - 269
        self.parent.btn_size.setStyleSheet("border-image: url(:/source/flechaL.png);")
        self.parent.frame.move(new_x, self.parent.frame.y())
        self.parent.frame.setFixedWidth(new_width)
    
    def mostrar_reloj(self):
        current_time = QTime.currentTime()
        hour = current_time.toString("hh:mm:ss AP")
        self.parent.hora.setText(hour)

    def obtenerFecha(self):
        current_date = QDate.currentDate()
        formatted_date = current_date.toString("d 'de' MMMM 'de' yyyy")
        self.parent.fecha.setText(formatted_date)

    def hidenpass(self):
        if self.parent.password.echoMode() == QLineEdit.Normal:
            self.parent.password.setEchoMode(QLineEdit.Password)
            self.parent.btn_pass.setIcon(QIcon(":/source/show.png"))
        else:
            self.parent.password.setEchoMode(QLineEdit.Normal)
            self.parent.btn_pass.setIcon(QIcon(":/source/hide.png"))

    def iniciarsesion(self):
        print("Iniciar sesion")
        user=self.parent.user.text()
        password=self.parent.password.text()

        res,mess,user = self.userService.authenticateUser(user,password)
        #res= self.userService.listUsers2()
        if res == True:
            for widget in self.parent.findChildren(QWidget):
                widget.deleteLater()
            self.parent.enterEvent=()
            self.parent.leaveEvent=()
            
            configHome.homeConfig(self.parent,user)
        else:
            print(mess)

# class login(QMainWindow):
#     def __init__(self, parent: QWidget | None ):
#         super().__init__(parent)
#         self.loginConfig(parent)

#     def loginConfig(self,parent):
#         self.ui=loadUi('app/views/login2.ui',parent)
#         self.userService = UserService()
#         parent.setWindowFlags(Qt.FramelessWindowHint)
#         parent.setAttribute(Qt.WA_TranslucentBackground)
#         parent.frame.mouseMoveEvent = self.moveWindow
#         self.ui.btn_salir.clicked.connect(self.close)
#         #self.btn_size.clicked.connect(lambda: change_size(self))
#         self.ui.ingresar.clicked.connect(self.iniciarsesion)
#         self.ui.btn_pass.clicked.connect(self.hidenpass)
#         self.obtenerFecha()
#         timer = QTimer(parent)
#         timer.timeout.connect(self.mostrar_reloj)
#         timer.start(1000)

#         parent.setMouseTracking(True)

#     def enterEvent(self, event):
#         current_x = self.frame.x()
#         new_x = current_x - 269
#         new_width = self.ui.frame.width() + 269
#         self.ui.btn_size.setStyleSheet("border-image: url(:/source/flechaR.png);")
#         self.ui.frame.move(new_x, self.ui.frame.y())
#         self.ui.frame.setFixedWidth(new_width)

#     def leaveEvent(self, event):
#         current_x = self.frame.x()
#         new_x = current_x + 269
#         new_width = self.ui.frame.width() - 269
#         self.ui.btn_size.setStyleSheet("border-image: url(:/source/flechaL.png);")
#         self.ui.frame.move(new_x, self.ui.frame.y())
#         self.ui.frame.setFixedWidth(new_width)

#     def moveWindow(self, e):
#         if e.buttons() == Qt.LeftButton:
#             self.move(self.pos() + e.globalPos() - self.clickPosition)
#             self.clickPosition = e.globalPos()
#             e.accept()

#     def mousePressEvent(self, event):
#         self.clickPosition = event.globalPos()

#     def close(self):
#         sys.exit()
    
#     def change_size(self):
#         current_x = self.frame.x()
#         if self.frame.width() == 91:
#             new_x = current_x - 269
#             new_width = self.frame.width() + 269
#             self.btn_size.setStyleSheet("border-image: url(:/source/flechaR.png);")
#         else:
#             new_x = current_x + 269
#             new_width = self.frame.width() - 269
#             self.btn_size.setStyleSheet("border-image: url(:/source/flechaL.png);")
#         self.frame.move(new_x, self.frame.y())
#         self.frame.setFixedWidth(new_width)

#     def mostrar_reloj(self):
#             current_time = QTime.currentTime()
#             hour = current_time.toString("hh:mm:ss AP")
#             self.ui.hora.setText(hour)

#     def obtenerFecha(self):
#         current_date = QDate.currentDate()
#         formatted_date = current_date.toString("d 'de' MMMM 'de' yyyy")
#         self.ui.fecha.setText(formatted_date)

#     def hidenpass(self):
#         if self.ui.password.echoMode() == QLineEdit.Normal:
#             self.ui.password.setEchoMode(QLineEdit.Password)
#             self.ui.btn_pass.setIcon(QIcon(":/source/show.png"))
#         else:
#             self.ui.password.setEchoMode(QLineEdit.Normal)
#             self.ui.btn_pass.setIcon(QIcon(":/source/hide.png"))

#     def iniciarsesion(self):
#         print("Iniciar sesion")
#         user=self.ui.user.text()
#         password=self.ui.password.text()

#         res,mess,user = self.userService.authenticateUser(user,password)
#         #res= self.userService.listUsers2()
#         if res == True:
#             for widget in self.findChildren(QWidget):
#                 widget.deleteLater()
#             configHome.homeConfig(self,user)
#         else:
#             print(mess)
