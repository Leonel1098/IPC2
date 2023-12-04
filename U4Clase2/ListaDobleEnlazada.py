from Pelicula import Pelicula

class ListaDobleEnlazada:
    def __init__(self) -> None:
        self.raiz = Pelicula()
        self.ultimo = Pelicula()

    
    def append(self, nuevaPelicula):
        if self.raiz.nombre is None:
            self.raiz = nuevaPelicula
            self.ultimo = nuevaPelicula
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaPelicula
            nuevaPelicula.anterior = self.raiz
            self.ultimo = nuevaPelicula
        else:
            self.ultimo.siguiente = nuevaPelicula
            nuevaPelicula.anterior = self.ultimo
            self.ultimo = nuevaPelicula

    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.nombre is not None:
                cadena += "(" + nodoAux.nombre + " " + nodoAux.papel + " " + nodoAux.anio +  " " + nodoAux.duracion + ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)     