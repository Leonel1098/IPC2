#Pruebas 
from lista_doble_enlazada import ListaDobleEnlazada
lista = ListaDobleEnlazada()

lista.agregar_final(12)
lista.agregar_final(14)
lista.agregar_final(18)
lista.agregar_final(35)
lista.agregar_final(987)
lista.recorrer_inicio()

print("================================")


print("Eliminar dato del inicio ")
lista.eliminar_inicio()
lista.recorrer_inicio()

print("Eliminando dato el final ")
lista.eliminar_Final()
lista.recorrer_inicio()