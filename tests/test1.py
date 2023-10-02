import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

class CustomComboBox(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Personalización de QComboBox')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout(self)

        # Crea un QComboBox personalizado
        combo_box = QComboBox(self)
        combo_box.setGeometry(50, 50, 200, 30)
        # Agrega elementos al combo box
        combo_box.addItem('Filtrar Por Estado')  # Marcador de posición
        combo_box.addItem('Opción 1')
        combo_box.addItem('Opción 2')
        combo_box.addItem('Opción 3')

        # Configura el elemento marcador de posición como deshabilitado
        combo_box.model().item(0).setEnabled(False)

        # Define el estilo del QComboBox utilizando hojas de estilo (CSS)
        style = """
        QComboBox {
            background-color: #F7F7F7; /* Color de fondo */
            color: #333333; /* Color del texto */
            selection-background-color: #191919; /* Color de fondo de la selección */
            selection-color: white; /* Color del texto de la selección */
        }
        QComboBox::high-light {
            color: #ff0000;
        }
        QComboBox::drop-down {
            width: 20px; /* Ancho del selector (flecha) */
            height: 20px; /* Alto del selector (flecha) */
 
            color: #333333;
        }
        """
        combo_box.setStyleSheet(style)

        layout.addWidget(combo_box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    main_widget = CustomComboBox()
    window.setCentralWidget(main_widget)
    window.show()
    sys.exit(app.exec_())
