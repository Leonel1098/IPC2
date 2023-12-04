from Actor import Actor
import os

class ListaSimpleEnlazada:
    def __init__(self) -> None:
        self.raiz = Actor()
        self.ultimo = Actor()

    def append(self, nuevoActor):
        if self.raiz.nombre is None:
            self.raiz = nuevoActor
            self.ultimo = nuevoActor
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoActor
            self.ultimo = nuevoActor
        else:
            self.ultimo.siguiente = nuevoActor
            self.ultimo = nuevoActor
    
    def print(self):
        nodoAux = self.raiz

        cadena = ''

        while True:
            if nodoAux.nombre is not None:
                cadena += "(" + nodoAux.nombre + " " + nodoAux.nacionalidad + " " + nodoAux.edad + ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)

    def buscarActorByNombre(self, nombre):
        nodoAux = self.raiz

        while nodoAux.nombre != nombre:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None
        
        return nodoAux

    def graficar(self):
        nodoAux = self.raiz
        
        cadena = 'digraph { '  
        while True:
            if nodoAux.nombre is not None:
                cadena += nodoAux.nombre.replace(' ', '')
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        cadena += "}"
        file = open("./nodo.dot", "w+")
        file.write(cadena)
        file.close()
        os.system('dot -Tpng nodo.dot -o nodo.png')

