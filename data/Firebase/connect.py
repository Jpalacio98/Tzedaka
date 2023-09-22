from firebase import firebase
import requests

class ConnecionFB():
    def __init__(self):
        super().__init__()
        self.estado = self.conexion()

    def conexion(self):
        try:
            response =  firebase.FirebaseApplication("https://tzedaka-db-default-rtdb.firebaseio.com/",None)
            self.db = response
            return True
        except response:
            return False

    def consultarTabla(self,tabla):
        if self.estado:
            datos= self.db.get(f'/TzedakaBD/{tabla}','')
            if datos != None:
                listaDatos= list(datos.items())
            else:
                listaDatos =[]
            return listaDatos
        else:
            return "No hay coneccion a Firebase"

    def insertTabla(self,tabla,dato):
        res = self.db.post(f'/TzedakaBD/{tabla}',dato)
        return res

    def deleteTabla(self,tabla,id):
        res = self.db.delete(f'/TzedakaBD/{tabla}',f'{id}')
        return res

