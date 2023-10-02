import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi


class infoClientConfig(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = loadUi('app/views/infoclients.ui',self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.btn_cerrar.clicked.connect(self.close)
        self.btn_voltear.clicked.connect(self.voltear)
        self.toggle =True
        self.mouse_pressed = False
        self.old_pos = None
        self.label_7.setVisible(False)
        self.label_8.setVisible(False)
        self.label_10.setVisible(False)
        self.label_12.setVisible(False)
        self.frame_4.enterEvent = lambda event: self.frame_4.setStyleSheet("""
        border-image: url(:/source/logo.png);
        border-radius:0px;
        """)
        self.frame_4.leaveEvent = lambda event: self.frame_4.setStyleSheet("""
        border-image: url(:/source/biometrico.png);
        border-radius:0px;
        """)
        self.frame_6.enterEvent = lambda event: self.label_7.setVisible(True)
        self.frame_6.leaveEvent = lambda event: self.label_7.setVisible(False)
        self.frame_7.enterEvent = lambda event: self.label_8.setVisible(True)
        self.frame_7.leaveEvent = lambda event: self.label_8.setVisible(False)
        self.frame_8.enterEvent = lambda event: self.label_10.setVisible(True)
        self.frame_8.leaveEvent = lambda event: self.label_10.setVisible(False)
        self.frame_9.enterEvent = lambda event: self.label_12.setVisible(True)
        self.frame_9.leaveEvent = lambda event: self.label_12.setVisible(False)
        self.comboBox.setPlaceholderText("Filtrar Por Estado")
        style = """
        QComboBox {
            background-color:rgba(255,255,255,100); /* Color de fondo */
            color: #ffffff; /* Color del texto */
            selection-background-color: #007BFF; /* Color de fondo de la selección */
            selection-color: white; /* Color del texto de la selección */
        }
        QComboBox::drop-down {
            /*width: 30px;  Ancho del selector (flecha) */
            /*height: 20px;  Alto del selector (flecha) */
            border: none; /* Sin borde en el selector (flecha) */
            background-color: #ff0000; /* Color de fondo del selector (flecha) */
            color:#FFFFFF;

        }
        QComboBox::placeholder {
            color: #000000; /* Color del marcador de posición */
        }
        """
        style2 = """
        QComboBox {   
        }
        QComboBox::drop-down {
        }
        QComboBox::placeholder {
            color: #000000; /* 
        }
        """
        
        self.comboBox.setStyleSheet(style2)


    def close(self):
        self.reject()
    
    def voltear(self):
        if self.toggle:
            self.sw_info.setCurrentIndex(1)
            self.btn_voltear.setIcon(QIcon(':source/giro2.png'))
            self.toggle = False
        else:
            self.sw_info.setCurrentIndex(0)
            self.btn_voltear.setIcon(QIcon(':source/giro.png'))
            self.toggle = True
    
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