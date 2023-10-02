from data.Firebase.connect import ConnecionFB

class UserService():
    def __init__(self):
        super().__init__()
        self.cn = ConnecionFB()

    def insertUser(self,user):
        res = self.cn.insertTabla('Users',user.setfotamto())
        return res
    
    def deleteUser(self,id):
        lista = self.listUsers2()
        for i in range(len(lista)):
            if lista[i][1]['cedula']==id:
                res = self.cn.deleteTabla('Users',lista[i][0])
                return res
        return f"No se encontri el registro {id}"
    
    def updateUser(self,id,newUser):
        res1 = self.deleteUser(id)
        res2 = self.insertUser(newUser)
        return res1, res2

    def listUsers2(self):
        res = self.cn.consultarTabla('Users')
        users =[]
        for i in range(len(res)):
            users.append((res[i][0],res[i][1]))
        return users

    def authenticateUser(self,username,password):
        if self.cn.estado == True:
            lista = self.listUsers2()
            for i in range(len(lista)):
                if lista[i][1]['username'] == username or lista[i][1]['correo'] == username:
                    if lista[i][1]['password'] == password:
                        return True,"Iniciando Secion",lista[i]
                    else:
                        return False,"Contraseña incorrerta...",None
            return False,"Usuario No resgistado...",None
        else:
            return False,"No hay conexion a internet",None


