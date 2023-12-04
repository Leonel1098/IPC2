class nodoIngrediente:
    def __init__(self,nombreIngrediente,tiempoIngrediente):
        self.nombreIngrediente = nombreIngrediente
        self.tiempoIngrediente = tiempoIngrediente
        self.siguiente = None 
    
    def setSiguienteIngrediente(self,ingrediente):
        self.siguiente = ingrediente

    def getSiguienteIngrediente(self):
        return self.siguiente

    def getNombreIngrediente(self):
        return self.nombreIngrediente
    def gettiempoIngrediente(self):
        return self.tiempoIngrediente
    def setNombreIngresdiente(self,tiempoIngrediente):
        self.tiempoIngrediente = tiempoIngrediente
    def setPrecioIngresdiente(self,tiempoIngrediente):
        self.tiempoIngrediente = tiempoIngrediente