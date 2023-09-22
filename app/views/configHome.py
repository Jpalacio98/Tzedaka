from static.resource import *
from app.components.CustomButton1 import CustomButton as Cbutton1
from app.components.reloj import get_date, get_hours
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi


def homeConfig(self):
    self.estado = True
    self.ui=loadUi('app/views/home.ui',self)
    self.setWindowFlags(Qt.FramelessWindowHint)

    #-----boton 1---------
    self.btn_Clientes_1= Cbutton1("Clientes","cliente.png")
    self.horizontalLayout_4.replaceWidget(self.btn_Clientes,self.btn_Clientes_1)
    self.btn_Clientes.close()
    
    #-----boton 2---------
    self.btn_Procesos= Cbutton1("Procesos","proceso.png")
    self.horizontalLayout_4.replaceWidget(self.btn_Clientes_2,self.btn_Procesos)
    self.btn_Clientes_2.close()

    #-----boton 3---------
    self.btn_Calculos= Cbutton1("Calculos","widget.png")
    self.horizontalLayout_4.replaceWidget(self.btn_Clientes_3,self.btn_Calculos)
    self.btn_Clientes_3.close()

    #-----boton 4---------
    self.btn_DashBoard= Cbutton1("DashBoard","finanzas.png")
    self.horizontalLayout_4.replaceWidget(self.btn_Clientes_4,self.btn_DashBoard)
    self.btn_Clientes_4.close()

    #-----boton 5---------
    self.btn_Ajustes= Cbutton1("Ajustes","ajustamiento.png")
    self.horizontalLayout_4.replaceWidget(self.btn_Clientes_5,self.btn_Ajustes)
    self.btn_Clientes_5.close()

    self.btn_cerrar.clicked.connect(self.close)
    self.btn_minmax.clicked.connect(self.restablecer)
    self.btn_minimizar.clicked.connect(self.minimizar)
    self.btn_Clientes_1.clicked.connect(self.close)
    self.timer = QTimer()
    self.timer.timeout.connect(lambda:reloj(self))
    self.timer.start(1000)
    self.show()

def reloj(self):
    self.hora.setText(get_hours())
    self.fecha.setText(get_date())
    