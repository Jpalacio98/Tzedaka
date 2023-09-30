#from data.services import serviceUser as service

class ControlUserAuth:
    def __init__(self):
        self.response = None
        self.message = ""
        self.user_credential = None
        #self.service = service.Peticioneslogin()

    async def crear_usuario(self, email, password):
        # Llama a la función de registro de usuario y maneja la respuesta
        self.response = await self.registrar_usuario_en_servicio(email, password)
        await self.controlar_usuario(self.response)

    async def consultar_usuario(self):
        # Llama a la función para consultar usuario y maneja la respuesta
        self.response = await self.consultar_usuario_en_servicio()
        await self.controlar_usuario(self.response)

    async def ingresar_usuario(self, email, password):
        # Llama a la función para ingresar usuario y maneja la respuesta
        print("estoy en el contoladore")
        self.response = await self.ingresar_usuario_en_servicio(email, password)
        print(self.response);
        await self.controlar_usuario(self.response)

    async def recuperar_contrasena(self, email):
        # Llama a la función para recuperar contraseña y maneja la respuesta
        self.response = await self.recuperar_contrasena_en_servicio(email)
        await self.controlar_usuario(self.response)

    async def cerrar_sesion(self):
        # Llama a la función para cerrar sesión y maneja la respuesta
        self.response = await self.cerrar_sesion_en_servicio()
        await self.controlar_usuario(self.response)

    async def registrar_usuario_en_servicio(self, email, password):
        response = await self.service.crear_registro_email(email, password)
        return response

    async def consultar_usuario_en_servicio(self):
        response = await self.service.consultar_usuario()
        return response

    async def ingresar_usuario_en_servicio(self, email, password):
        response = await self.service.ingresar_email(email, password)
        return response

    async def recuperar_contrasena_en_servicio(self, email):
        response = await self.service.recuperar_contrasena(email)
        return response

    async def cerrar_sesion_en_servicio(self):
        response = await self.service.abandonar_sesion()
        return response

    async def controlar_usuario(self, respuesta):
        if respuesta is None:
            self.message = "Por favor, intente de nuevo."
        elif respuesta.get("status") in ["1", "2"]:
            self.message = "Por favor, intente de nuevo."
        else:
            self.user_credential = respuesta

    @property
    def estado_usuario(self):
        return self.response

    @property
    def mensajes_usuario(self):
        return self.message

    @property
    def usuario_valido(self):
        return self.user_credential
