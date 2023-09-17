from PyQt5 import QtCore, QtGui, QtWidgets

class CustomButton(QtWidgets.QPushButton):
    def __init__(self, etiqueta,icono):
        super().__init__()
        self.setFixedSize(140,140)
        sizePolicy2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy2.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy2)
        layout =  QtWidgets.QVBoxLayout()
        layout.setSpacing(5)
        layout.setContentsMargins(0, 0, 0, 0)
        spacerItem =  QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        layout.addItem(spacerItem)
        icon = QtWidgets.QLabel()
        icon.setMinimumSize(60,60)
        icon.setScaledContents(True)
        icon.setStyleSheet(f"background-color: rgba(255, 255, 255, 0);border-image: url(:/source/{icono});")
        texto = QtWidgets.QLabel()
        texto.setText(etiqueta)
        texto.setStyleSheet("color: rgb(255, 255, 255); \n font: 75 20pt Century Schoolbook; \n background-color: rgba(255, 255, 255, 0);")
        texto.setAlignment(QtCore.Qt.AlignCenter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(texto.sizePolicy().hasHeightForWidth())
        texto.setSizePolicy(sizePolicy)
        layout.addWidget(icon,0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        layout.addWidget(texto,0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem =  QtWidgets.QSpacerItem(20, 21,  QtWidgets.QSizePolicy.Minimum,  QtWidgets.QSizePolicy.Fixed)
        layout.addItem(spacerItem)
        self.setStyleSheet( '''
                QPushButton {
                    background-color: rgba(255, 255, 255, 0);
                    font: bold 14px Century Schoolbook;
                    padding: 6px;
                }
                QPushButton:hover {
                    border-radius: 85px;
                    background-color: #000000;
                    font-size: 16px;
                    border-style: solid;
                }
                QPushButton:pressed {
                    background-color: rgba(55, 155, 5, 70);
                    border-style: solid;
                    border-width: 5px;
                }
                
            ''')
        self.setLayout(layout)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.setFixedSize(QtCore.QSize(170, 170))

    def leaveEvent(self, event):
        self.setFixedSize(QtCore.QSize(140, 140))
