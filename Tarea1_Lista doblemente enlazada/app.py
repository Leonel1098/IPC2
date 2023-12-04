from Persona import Persona
from lista_doble import lista_doble

persona1= Persona(202001534,"Lionel Messi", 36)
persona2= Persona(202100000,"Cristiano Ronaldo", 38)
persona3= Persona(202200000,"Ronaldinho Gaucho", 43)

lista_doble = lista_doble()

lista_doble.insertar_ordenado(persona1)
lista_doble.insertar_ordenado(persona2)
lista_doble.insertar_ordenado(persona3)
lista_doble.recorrer()
