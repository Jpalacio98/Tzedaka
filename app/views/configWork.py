
import sys

from app.components.listItem import Ui_Frame
from app.views import configRegistraClienteForm
from app.components.CustomButton2 import CustomButton as Cbutton1
from app.components.SideBar import Sidebar
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

def workConfig(self):
    self.ui=loadUi("app/views/work.ui",self)
    datos=[
            ("Clientes", ":source/cliente.png",lambda:FuncionMenuBtn(self)),
            ("Procesos", ":source/proceso.png",lambda:FuncionMenuBtn(self)),
            ("Calculos", ":source/widget.png",lambda:FuncionMenuBtn(self)),
            ("Finanzas",":source/finanzas.png",lambda:FuncionMenuBtn(self)),
            ("Ajustes", ":source/ajustamiento.png",lambda:FuncionMenuBtn(self))
        ]
    self.frameSidebar = Sidebar(datos)
    self.horizontalLayout.replaceWidget(self.sidebar,self.frameSidebar)
    self.sidebar.close()
    #self.sidebar= 
    self.estado = False
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.btn_cerrar.clicked.connect(self.close)
    self.btn_minmax.clicked.connect(self.restablecer)
    self.btn_minimizar.clicked.connect(self.minimizar)
    #-----boton 1---------
    self.spacer = self.verticalLayout_4.itemAt(3)
    self.verticalLayout_4.addItem(self.spacer)
    self.btn_Registar= Cbutton1("Registrar","anadir_cliente.png")
    self.verticalLayout_4.removeWidget(self.pushButton)
    self.pushButton.deleteLater()
    self.verticalLayout_4.addWidget(self.btn_Registar,0, Qt.AlignHCenter|Qt.AlignVCenter)
    
    #-----boton 2---------
    self.btn_Actualizar= Cbutton1("Actualizar","editar_cliente.png")
    self.verticalLayout_4.removeWidget(self.pushButton_2)
    self.pushButton_2.deleteLater()
    self.verticalLayout_4.addWidget(self.btn_Actualizar,0, Qt.AlignHCenter|Qt.AlignVCenter)

    #-----boton 3---------
    self.btn_Eliminar= Cbutton1("Eliminar","eliminar_cliente.png")
    self.verticalLayout_4.removeWidget(self.pushButton_3)
    self.pushButton_3.deleteLater()
    self.verticalLayout_4.addWidget(self.btn_Eliminar,0, Qt.AlignHCenter|Qt.AlignVCenter)
    self.spacer_2 = self.verticalLayout_4.itemAt(0)
    self.verticalLayout_4.removeItem(self.spacer_2)
    self.verticalLayout_4.addItem(self.spacer_2)
    cargarClientes(self)
    self.btn_Registar.clicked.connect(lambda:registroForm(self))

    self.showMaximized()

def FuncionMenuBtn(self):
    print("se preciono un boton del menu")

def clienteForm(self):
    #en esta funcuon debe ir la informacion del cliente pasada por parametros
    Frame = QFrame(self)
    ui = loadUi("app/views/frameDatos.ui",Frame)
    return Frame

def cargarClientes(self):
    for item in range(20):
        custom_widget = clienteForm(self)
        list_item = QListWidgetItem()
        list_item.setSizeHint(custom_widget.sizeHint())
        self.tw_clientes.addItem(list_item)
        self.tw_clientes.setItemWidget(list_item, custom_widget)

def registroForm(self):
    dialog = configRegistraClienteForm.registrarClienteFormConfig()
    dialog.exec()
    # configRegistraClienteForm.registrarClienteFormConfig(self)
    # # dialog = QDialog(self)
    # # dialog = loadUi('Resource/Views/registrarClienteForm.ui',dialog)
    # # dialog.exec()
