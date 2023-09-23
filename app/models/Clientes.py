
class Clientes():
    def __init__(self):
        super().__init__()

    def MapeoCliente(self, cedula, apellidos, nombres, correo, telefono, direccion, barrio, ciudad, fechaNa):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.barrio = barrio
        self.ciudad = ciudad
        self.fechaNa = fechaNa
        self.usuario =""

    def setfotamto(self):
        datoCliente={
            '1cedula':self.cedula,
            '2apellidos':self.apellidos,
            '3nombres': self.nombres,
            '4correo':self.correo ,
            '5telefono':self.telefono ,
            '6direccion':self.direccion ,
            '7barrio':self.barrio,
            '8ciudad':self.ciudad,
            '9fechaNa':self.fechaNa,
            '9usuario':self.usuario
        }
        return datoCliente

