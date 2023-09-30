import pyrebase

class Peticioneslogin:
    def __init__(self):
        self.auth = pyrebase.auth()
    
    @staticmethod
    async def crear_registro_email(self, email, password):
        try:
            user = await self.auth.create_user(email=email, password=password)
            return user
        except pyrebase.auth.AuthError as e:
            if e.code == 'weak-password':
                return 'Contraseña Debil'
            elif e.code == 'email-already-exists':
                return 'Correo ya Existe'
        except Exception as e:
            print(e)

    @staticmethod
    async def consultar_usuario(self):
        try:
            user = await self.auth.get_user_by_uid('user_id')  # Reemplaza 'user_id' con el ID del usuario que deseas consultar
            return user
        except self.auth.AuthError as e:
            if e.code == 'user-not-found':
                print('Usuario no encontrado')
            else:
                print(e)
        except Exception as e:
            print(e)

    @staticmethod
    async def ingresar_email(self, email, password):
        try:
            user = await self.auth.sign_in_with_email_and_password(email=email, password=password)
            print(user.uid)
            return user
        except self.auth.AuthError as e:
            if e.code == 'user-not-found':
                print('Correo no encontrado')
                return '1'
            elif e.code == 'wrong-password':
                print('Contraseña incorrecta')
                return '2'
            else:
                print(e)
        except Exception as e:
            print(e)

    @staticmethod
    async def recuperar_contrasena(self, email):
        try:
            await self.auth.generate_password_reset_link(email)
            return "Correo Enviado"
        except Exception as e:
            print(e)

    @staticmethod
    async def abandonar_sesion(self):
        try:
            await self.auth.revoke_refresh_tokens('user_id')  # Reemplaza 'user_id' con el ID del usuario
            return "Sesión Cerrada"
        except Exception as e:
            print(e)
