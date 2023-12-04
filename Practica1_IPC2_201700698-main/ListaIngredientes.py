from nodoIngrediente import nodoIngrediente
class ListaIngredientes:
    def __init__(self):
        self.primero = None
        self.siguiente = None
        self.size = 0
    def ingresarNuevoIngrediente(self,nombreIngrediente,tiempoIngrediente):
        nuevoIngrediente = nodoIngrediente(nombreIngrediente, tiempoIngrediente)    
        self.size += 1
        if self.primero is None : 
            self.primero = nuevoIngrediente
            self.ultimo = nuevoIngrediente
        else :
            self.ultimo.setSiguienteIngrediente(nuevoIngrediente)
            self.ultimo = nuevoIngrediente

    def mostrarIngredientes(self):
        tmp = self.primero
        print("-------Lista de  Ingrediente de la Pizza-----------")
        for i in range(self.size):
            print(i+1)
            print("Nombre : ", tmp.getNombreIngrediente())
            print("Tiempo : ", tmp.gettiempoIngrediente())
            tmp = tmp.getSiguienteIngrediente()
        print("--------------------------------------")
    def TiempoTotal(self):
        tiempo = 0
        temp = self.primero
        for i in range(self.size):
            tiempo += int(temp.gettiempoIngrediente())
            temp = temp.getSiguienteIngrediente()
        print("--------------------------------------")
        print(" Tiempo de De Preparacion de Cada Pizza : ", tiempo ,"min")
        print("--------------------------------------")
        return tiempo

  

