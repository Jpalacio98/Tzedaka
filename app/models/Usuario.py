class Usuario():
    def __init__(self):
        super().__init__()

    def MapeoUsuario(self, cedula, correo, username, password, nombres, apellidos,telefono, direccion, barrio, ciudad, fechaNa,roll,color,cargo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.barrio = barrio
        self.ciudad = ciudad
        self.fechaNa = fechaNa
        self.username = username
        self.password = password
        self.roll=roll
        self.color = color
        self.cargo = cargo

    def setfotamto(self):
        datoUser={
            'cedula':self.cedula,
            'correo':self.correo,
            'username':self.username,
            'password':self.password,
            'nombres': self.nombres,
            'apellidos':self.apellidos,
            'telefono':self.telefono,
            'direccion':self.direccion ,
            'barrio':self.barrio,
            'ciudad':self.ciudad,
            'fechaNa':self.fechaNa,
            'roll':self.roll,
            'color':self.color,
            'cargo':self.cargo
        }
        return datoUser
