from firebase import firebase
import psutil
import requests

class ConnecionFB():
    def __init__(self):
        super().__init__()
        self.estado = self.conexion()

    def conexion(self):
        try:
            response =  firebase.FirebaseApplication("https://tzedaka-db-default-rtdb.firebaseio.com/TzedakaBD/Users/-NYqNA0M0SA7DOE2fhBz",None)
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

    # def closeConnection(self):
    #     for process in psutil.process_iter(attrs=['pid', 'name']):
    #         if process.info['name'] == process_name:
    #             try:
    #                 p = psutil.Process(process.info['pid'])
    #                 p.terminate()  # Terminar el proceso
    #                 print(f"Proceso {process_name} terminado con éxito.")
    #             except Exception as e:
    #                 print(f"No se pudo terminar el proceso {process_name}: {str(e)}")