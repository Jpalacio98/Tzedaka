
import sys
from Lib.Components.listItem import Ui_Frame
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

# def clienteForm(self):
#     #en esta funcuon debe ir la informacion del cliente pasada por parametros
#     Frame = QFrame(self)
#     ui = Ui_Frame()
#     ui.setupUi(Frame)
#     return Frame

# def cargarClientes(self):
#     for item in range(10):
#         custom_widget = clienteForm(self)
#         list_item = QListWidgetItem()
#         list_item.setSizeHint(custom_widget.sizeHint())
#         self.tw_clientes.addItem(list_item)
#         self.tw_clientes.setItemWidget(list_item, custom_widget)