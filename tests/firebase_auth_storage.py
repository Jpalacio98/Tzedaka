import sys
import pyrebase
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
config = {
    'apiKey': "AIzaSyAnE6WxkeYDZ9Oro8moJUbTDWwML2VtdyY",
    'authDomain': "tzedaka-db.firebaseapp.com",
    'databaseURL': "https://tzedaka-db-default-rtdb.firebaseio.com",
    'projectId': "tzedaka-db",
    'storageBucket': "tzedaka-db.appspot.com",
    'messagingSenderId': "818074652781",
    'appId': "1:818074652781:web:d4f7c6b994745a5a59af64",
    'measurementId': "G-0Y4L73XMB7"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()
class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.username_label = QLabel("Correo Electrónico:")
        self.layout.addWidget(self.username_label)

        self.username_input = QLineEdit(self)
        self.layout.addWidget(self.username_input)

        self.password_label = QLabel("Contraseña:")
        self.layout.addWidget(self.password_label)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Iniciar Sesión", self)
        self.login_button.clicked.connect(self.onLogin)
        self.layout.addWidget(self.login_button)
    
    def onLogin(self):
        email = 'jpalacio@tzedaka.sas'#self.username_input.text()#

        password = 'jpalacio2023'#self.password_input.text()
        bandera=False
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            if user:
                bandera = True
                #QMessageBox.information(self, "Éxito", "Inicio de sesión exitoso.")
                
            
        except Exception as e:
            bandera=False
            QMessageBox.critical(self, "Error de Inicio de Sesión", str(e))

        if bandera == True:
            self.openSecondWindow(user)

    def openSecondWindow(self,user):
        self.second_window = SecondWindow(user)
        self.second_window.show()
        self.close()

class SecondWindow(QMainWindow):
    def __init__(self,user):
        super().__init__()
        self.initUI(user)

    def initUI(self,user):
        self.setWindowTitle("Registro de Usuarios")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.name_label = QLabel("Nombre:")
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit(self)
        self.layout.addWidget(self.name_input)

        self.lastname_label = QLabel("Apellido:")
        self.layout.addWidget(self.lastname_label)

        self.lastname_input = QLineEdit(self)
        self.layout.addWidget(self.lastname_input)

        self.color_label = QLabel("Color Favorito:")
        self.layout.addWidget(self.color_label)

        self.color_input = QComboBox(self)
        self.color_input.addItems(["Rojo", "Azul", "Verde", "Amarillo", "Otro"])
        self.layout.addWidget(self.color_input)

        self.role_label = QLabel("Rol:")
        self.layout.addWidget(self.role_label)

        self.role_input = QLineEdit(self)
        self.layout.addWidget(self.role_input)

        self.photo_label = QLabel("Foto de Perfil:")
        self.layout.addWidget(self.photo_label)

        self.photo_path = None

        self.photo_button = QPushButton("Seleccionar Foto", self)
        self.photo_button.clicked.connect(self.selectPhoto)
        self.layout.addWidget(self.photo_button)

        self.register_button = QPushButton("Registrar", self)
        self.register_button.clicked.connect(self.registerUser)
        self.layout.addWidget(self.register_button)

        # Almacena el usuario autenticado para su uso en el registro
        self.auth_user = user

    def selectPhoto(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Images (*.png *.jpg *.jpeg *.gif *.bmp);;All Files (*)", options=options)

        if file_path:
            self.photo_path = file_path
            pixmap = QPixmap(file_path)
            self.photo_label.setPixmap(pixmap)
            self.photo_label.setScaledContents(True)
    
    def registerUser(self):
        name = self.name_input.text()
        lastname = self.lastname_input.text()
        color = self.color_input.currentText()
        role = self.role_input.text()

        if not name or not lastname or not color or not role:
            QMessageBox.critical(self, "Error", "Por favor, complete todos los campos.")
            return

        try:
            user_data = {
                "name": name,
                "lastname": lastname,
                "color": color,
                "role": role
            }
            db = firebase.database()
            db.child("users").child(self.auth_user["localId"]).set(user_data)
            
            if self.photo_path:
                storage.child("profile_photos").child(self.auth_user["localId"]).put(self.photo_path, self.auth_user["idToken"])
            
            QMessageBox.information(self, "Éxito", "Usuario registrado con éxito.")
        except Exception as e:
            QMessageBox.critical(self, "Error de Registro", str(e))
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    first_window = FirstWindow()
    first_window.show()
    sys.exit(app.exec_())
