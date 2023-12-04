from Persona import Persona

class ListaDobleEnlazada:
    def __init__(self) -> None:
        self.raiz = Persona()
        self.ultimo = Persona()

    
    def append(self, nuevaPersona):
        if self.raiz.nombre is None:
            self.raiz = nuevaPersona
            self.ultimo = nuevaPersona
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaPersona
            nuevaPersona.anterior = self.raiz
            self.ultimo = nuevaPersona
        else:
            self.ultimo.siguiente = nuevaPersona
            nuevaPersona.anterior = self.ultimo
            self.ultimo = nuevaPersona

    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.nombre is not None:
                cadena += "(" + nodoAux.nombre + " " + nodoAux.id + " " + nodoAux.edad + ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)     

    def Bubblesort (cadena):
        length = len(cadena)
        for i in range(length - 1):
            swapped = False
            for j in range(length - 1 - i):
             if cadena[j] > cadena[j + 1]:
                    swapped = True
                    cadena[j], cadena[j + 1] = cadena[j + 1], cadena[j]
            if not swapped:
                break
        return cadena