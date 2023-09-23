import random
import string



class Abono():
    def __init__(self):
        super().__init__()

    def mapeo(self,numP,monto,pAbono):
        self.numAbono= self.generar_codigo()
        self.numProceso=numP
        self.monto=monto
        self.listaAbonos =[pAbono]
        self.calcularDeuda()

    def añadirAbono(self,val):
        self.numAbono.append(val)
        self.calcularDeuda()

    def calcularDeuda(self):
        res = int(self.monto)
        for i in self.listaAbonos:
            res = res - int(i)
        
        self.restante =  res

    def setformato(self):
        datoAbono={
            '1num':self.numAbono,
            '2numProceso':self.numProceso,
            '3monto':self.monto,
            '4abonos':self.listaAbonos.__str__()[1:-1],
            '5restante':self.restante
        }
        return datoAbono

    def generar_codigo(self):
        caracteres = string.ascii_letters + string.digits
        codigo = ''.join(random.choice(caracteres) for _ in range(8))
        return codigo