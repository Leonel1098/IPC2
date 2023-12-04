from ListaIngredientes import ListaIngredientes
class nodoPedido:
    def __init__(self,nombrCliente,direccionCliente,NumeroCliente,cantidadDePizzas):
        self.nombrCliente = nombrCliente
        self.direccionCliente = direccionCliente
        self.NumeroCliente = NumeroCliente
        self.cantidadDePizzas = cantidadDePizzas
        self.ListaIngredientes = ListaIngredientes()
        self.tiempo  = None 
        self.siguiente = None 

    def getSiguientePedido(self):
        return self.siguiente
    def setSiguientePedido(self,nuevoPedido):
        self.siguiente = nuevoPedido
    
    #gets
    def getNombreCliente(self):
        return self.nombrCliente
    def getDirreccion(self):
        return self.direccionCliente
    def getNumeroCliente(self):
        return self.NumeroCliente

    def getCandtida(self):
        return self.cantidadDePizzas
    #set
    def setTiempo(self,tiempo):
        self.tiempo = tiempo
    def getTiempo (self):
        return self.tiempo
