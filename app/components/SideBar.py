from PyQt5 import QtCore, QtGui, QtWidgets

class Sidebar(QtWidgets.QFrame):
    def __init__(self,datos):
        super().__init__()
        self.toggle=True
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setFixedWidth(80)
        self.setStyleSheet('''
            QFrame {
                background-color: #000000;
            }
        ''')
        self.layout_pp =QtWidgets. QVBoxLayout()
        self.layout_pp .setContentsMargins(10, 10, 10, 20)
        self.layout_pp .setSpacing(10)
        self.setLayout(self.layout_pp)
        self.frameUser = QtWidgets.QFrame(self)
        self.frameUser.setFixedHeight(60)
        self.frameUser.setFixedWidth(60)
        #self.frameUser.setStyleSheet("background-color:#9e0000")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameUser.sizePolicy().hasHeightForWidth())
        self.frameUser.setSizePolicy(sizePolicy)
        self.UserLayout =QtWidgets.QVBoxLayout()
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setMaximumSize(QtCore.QSize(50, 50))
        self.label_5.setPixmap(QtGui.QPixmap(":source/usuarios.png"))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255,0);\n")
        self.label_5.setScaledContents(True)
        self.UserLayout.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.UserName = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserName.sizePolicy().hasHeightForWidth())
        self.UserName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(80)
        self.UserName.setText("Jeferson Martinez")
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("background-color: rgba(255, 255, 255,0);\n""color: rgb(255, 255, 255);\n""font:12 20px")
        self.UserName.setAlignment(QtCore.Qt.AlignCenter)
        self.UserLayout.addWidget(self.UserName)
        self.UserRoll = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserRoll.sizePolicy().hasHeightForWidth())
        self.UserRoll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        #font.setFamily("SimSun")
        font.setPointSize(6)
        #font.setBold(True)
        font.setWeight(75)
        self.UserRoll.setFont(font)
        self.UserRoll.setText("Abogado(ADMIN)")
        self.UserRoll.setStyleSheet("color: rgb(255, 255, 255);\n""font:7 12px")
        self.UserRoll.setAlignment(QtCore.Qt.AlignCenter)
        self.UserRoll.setObjectName("UserRoll")
        self.UserRoll.setVisible(False)
        self.UserName.setVisible(False)
        self.UserLayout.addWidget(self.UserRoll)
        self.frameUser.setLayout(self.UserLayout)
        self.layout_pp.addWidget(self.frameUser,0, QtCore.Qt.AlignHCenter)
        
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 100)
        self.layout.setSpacing(10)
        self.frame_pp = QtWidgets.QFrame(self)
        self.frame_pp.setFixedWidth(60)
        self.frame_pp.setFixedHeight(500)
        self.frame_pp.setLayout(self.layout)
        #self.frame_pp.setStyleSheet("background-color:#9e0a20")
        self.layout_pp.addWidget(self.frame_pp)

        self.label_pie = QtWidgets.QLabel()
        self.label_pie .setMinimumSize(QtCore.QSize(30, 30))
        self.label_pie.setMaximumSize(QtCore.QSize(60, 50))
        self.label_pie.setPixmap(QtGui.QPixmap("source/Imagenes/logo2.png"))
        self.label_pie.setScaledContents(True)
        #self.label_5.setStyleSheet("background-color:#9e0000")
        self.layout_pp.addWidget(self.label_pie, 0, QtCore.Qt.AlignHCenter)

        self.icons = datos

        self.setupIcons()

    def visible(self):
        if self.toggle:
            self.setVisible(False)
            self.toggle=False
        else:
            self.setVisible(True)
            self.toggle=True
    
    def asignarAcion(self,lista):
        for i in range(len(lista)):
            item_frame = self.layout.itemAt(i).widget()
            item_frame.clicked.connect(lista[i])

    def setupIcons(self):
        for icon_text, icon_path, funcion in self.icons:
            item_frame= Menubutton(icon_text,icon_path)
            item_frame.clicked.connect(funcion)
            self.layout.addWidget(item_frame,0,QtCore.Qt.AlignHCenter)

    def enterEvent(self, event):
        self.setFixedWidth(200)
        self.UserRoll.setVisible(True)
        self.UserName.setVisible(True)
        self.frameUser.setFixedWidth(180)
        self.frameUser.setFixedHeight(120)
        self.frame_pp.setFixedWidth(200)
        for i in range(self.layout.count()):
            item_frame = self.layout.itemAt(i).widget()
            item_frame.setFixedWidth(200)
            text_label = item_frame.findChild(QtWidgets.QLabel, 'text')
            text_label.setVisible(True)
            #lyout = item_frame.findChild(QHBoxLayout, 'margen')
            #lyout.setContentsMargins(20, 0, 20, 0)

    def leaveEvent(self, event):
        self.setFixedWidth(80)
        self.UserRoll.setVisible(False)
        self.UserName.setVisible(False)
        self.frameUser.setFixedWidth(60)
        self.frameUser.setFixedHeight(60)
        self.frame_pp.setFixedWidth(60)
        for i in range(self.layout.count()):
            item_frame = self.layout.itemAt(i).widget()
            item_frame.setFixedWidth(50)
            text_label = item_frame.findChild(QtWidgets.QLabel, 'text')
            text_label.setVisible(False)
            #lyout = item_frame.findChild(QHBoxLayout, 'margen')
            #lyout.setContentsMargins(0, 0, 0, 0)


class Menubutton(QtWidgets.QPushButton):
    def __init__(self, etiqueta,icono):
        super().__init__()
        self.icon_label = QtWidgets.QLabel()
        self.icon_label.setPixmap(QtGui.QPixmap( icono))
        self.icon_label.setObjectName('icon')
        self.icon_label.setFixedHeight(32)
        self.icon_label.setFixedWidth(32)
        self.icon_label.setScaledContents(True)
        self.icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_label.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.text_label = QtWidgets.QLabel(etiqueta)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(80)
        self.text_label.setFont(font)
        self.text_label.setStyleSheet("color:#FFFFFF;\n""background-color:rgba(0,0,0,0)")
        self.text_label.setObjectName('text')
        self.text_label.setFixedHeight(20)
        self.text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.text_label.setVisible(False)
        self.icon_label2 = QtWidgets.QLabel()
        self.icon_label2.setPixmap(QtGui.QPixmap( icono))
        self.icon_label2.setObjectName('icon')
        self.icon_label2.setFixedHeight(32)
        self.icon_label2.setFixedWidth(32)
        self.icon_label2.setScaledContents(True)
        self.icon_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_label2.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.icon_label2.setVisible(False)
        item_layout = QtWidgets.QHBoxLayout()
        item_layout.addWidget(self.icon_label)
        item_layout.addWidget(self.text_label)
        item_layout.addWidget(self.icon_label2)
        item_layout.setObjectName('margen')
        item_layout.setSpacing(10)
        item_layout.setContentsMargins(10, 0, 10, 0)

        self.setLayout(item_layout)
        self.setFlat(True)
        self.setStyleSheet('''
            QPushButton {
                color:#ffffff
            }
            QPushButton:hover {
                border:8px solid #ffffff;
                background-color: rgba(0, 0, 0, 210);
                border-top:none;
                border-right:none;
                border-bottom:none;
            }
            QPushButton:pressed {
                background-color: #000000;
                border-top:none;
                border-right:none;
                border-bottom:none;
            }
            
        ''')
        self.setObjectName('item')
        self.setFixedHeight(50)
        self.setFixedWidth(50)
        
        
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.setFixedSize(QtCore.QSize(180, 90))
        self.icon_label.setVisible(False)
        self.icon_label2.setVisible(True)
        self.text_label.setVisible(True)

    def leaveEvent(self, event):
        self.setFixedSize(QtCore.QSize(180, 50))
        self.icon_label.setVisible(True)
        self.icon_label2.setVisible(False)
        self.text_label.setVisible(True)
