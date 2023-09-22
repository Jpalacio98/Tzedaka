from PyQt5 import QtCore, QtGui, QtWidgets


class CustomButton(QtWidgets.QPushButton):
    def __init__(self, etiqueta,icono):
        super().__init__()
        self.setFixedSize(220,220)
        sizePolicy2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy2.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy2)
        layout =  QtWidgets.QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(0, 0, 0, 0)
        spacerItem =  QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        icon = QtWidgets.QLabel()
        icon.setMinimumSize(100,100)
        icon.setScaledContents(True)
        icon.setStyleSheet(f"background-color: rgba(255, 255, 255, 0);border-image: url(:/source/{icono});")
        self.texto = QtWidgets.QLabel()
        self.texto.setText(etiqueta)
        self.texto.setStyleSheet("color: rgb(255, 255, 255); \n font: 75 20pt Century Schoolbook; \n background-color: rgba(255, 255, 255, 0);")
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.setVisible(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texto.sizePolicy().hasHeightForWidth())
        self.texto.setSizePolicy(sizePolicy)
        layout.addWidget(icon,0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        layout.addWidget(self.texto,0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem =  QtWidgets.QSpacerItem(20, 21,  QtWidgets.QSizePolicy.Minimum,  QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        self.setStyleSheet( '''
                QPushButton {
                    background-color: rgba(255, 255, 255, 0);
                    font: bold 14px Century Schoolbook;
                    border-radius:110px;
                }
                QPushButton:hover {
                    border-radius: 110px;
                   
                }
                QPushButton:pressed {
                    background-color: rgba(100, 100, 100, 200);
                    border: 5px inset #adadad;
                }
                
            ''')
        self.setLayout(layout)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.texto.setVisible(True)
        #self.setFixedSize(QtCore.QSize(230, 230))

    def leaveEvent(self, event):
        self.texto.setVisible(False)
        #self.setFixedSize(QtCore.QSize(200, 200))
