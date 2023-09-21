from PyQt5 import QtCore, QtGui, QtWidgets

class CustomButton(QtWidgets.QPushButton):
    def __init__(self, etiqueta,icono):
        super().__init__()
        self.setFixedSize(120,120)
        sizePolicy2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy2.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy2)
        self.setSizePolicy(sizePolicy2)
        layout =  QtWidgets.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        spacerItem =  QtWidgets.QSpacerItem(10, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        layout.addItem(spacerItem)
        icon = QtWidgets.QLabel()
        icon.setMinimumSize(60,60)
        icon.setScaledContents(True)
        icon.setStyleSheet(f"background-color: rgba(255, 255, 255, 0);border-image: url(:/source/{icono});")
        self.texto = QtWidgets.QLabel()
        self.texto.setText(etiqueta)
        self.texto.setStyleSheet("color: rgb(255, 255, 255); \n font: 75 14pt Century Schoolbook; \n background-color: rgba(255, 255, 255, 0);")
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.setVisible(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texto.sizePolicy().hasHeightForWidth())
        self.texto.setSizePolicy(sizePolicy)
        layout.addWidget(icon,0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        layout.addWidget(self.texto,0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem =  QtWidgets.QSpacerItem(10, 11,  QtWidgets.QSizePolicy.Minimum,  QtWidgets.QSizePolicy.Fixed)
        layout.addItem(spacerItem)
        self.setStyleSheet( '''
                QPushButton {
                    background-color: rgba(255, 255, 255, 0);
                    font: bold 12px Century Schoolbook;
                    padding: 6px;
                    border:none;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0);
                    font-size: 12px;
                    
                }
                QPushButton:pressed {
                    background-color: rgba(0, 0, 0, 70);
                    border:3px solid #fff;
                    border-radius: 60px;
                }
                
            ''')
        self.setLayout(layout)
        self.setMouseTracking(True)
        
    def enterEvent(self, event):
        self.texto.setVisible(True)  # Mostrar el texto en el mouse sobre
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.texto.setVisible(False)  # Limpiar el texto cuando el mouse sale
        super().leaveEvent(event)