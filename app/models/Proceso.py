from datetime import datetime

class Proceso():

    def __init__(self):
        super().__init__()

    def MapeoProceso(self,num,cedula,area,abono,descripcion):
        self.cedula = cedula
        self.area = area
        self.abono = abono
        self.estado = "Iniciado"
        self.descripcion = descripcion
        self.fechaInicio = datetime.now().strftime("%d/%m/%Y")
        self.NumProceso = num
        self.fechaFinal = ""
        self.usuario =""
    
    def setformato(self):
        datoProceso={
            '1num':self.NumProceso,
            '2estado':self.estado,
            '3fechainicio':self.fechaInicio,
            '4cedula':self.cedula,
            '5area':self.area,
            '6descripcion':self.descripcion,
            '7abono':self.abono,
            '8fechafin':self.fechaFinal,
            '9usuario':self.usuario
        }
        return datoProceso