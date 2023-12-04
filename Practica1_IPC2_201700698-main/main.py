#---Imports ---------
from ListaIngredientes import ListaIngredientes 
from ListaPedidos import ListaPedidos

Lpedidos = ListaPedidos()
LIngredientes = ListaIngredientes()


 #---Menú---------
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero:  "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
def menu():
    print("------------ PIZZA --------------  ")
    salir = False
    opcion = 0
    
    while not salir:
        
        print ("1. Ingresar Pedido  ")
        print ("2. Entregar Pedido  ")
        print ("3. Graficar Graphviz  ")
        print ("4. Mostrar Lista Pedidos   ")
        print ("5. Salir")
        
        print ("Elige una opcion")
    
        opcion = pedirNumeroEntero()
    
        if opcion == 1:
            print ("INGRESAR Pedido  ")
            IngresarPedido()
        elif opcion == 2:
            print ("Entregar Pedido ")
            tiempo = Lpedidos.eliminar_dato()
            Lpedidos.ActualizacionTiempo(int(tiempo))
        
        elif opcion == 3:
            print("Graficar  ")
            Lpedidos.Graficar()
        elif opcion == 4 : 
            Lpedidos.MostrarListaDePedidos()
        elif opcion == 5:
            salir = True
        
        
        else:
            print ("Introduce un numero entre 1 y 3")
    
    print ("Fin")
#-------------------------

def IngresarPedido():        
        print(" Ingrese Nombre del Cliente")
        nombreCliente = input()
        print(" Direccion del Cliente ")
        dirreccion = input()
        print(" Ingrese Numero de Telefono del Cliente ")
        numeroTelefonoCliente = input()
        print(" Ingrese Cantidad de PIzza ")
        cantidadDePizzas = input()
        print(" Ingrese Cantidad de Ingredientes ")
        CantidadDeIngredients = input()
        contador = 0 
        nuevoPedido = Lpedidos.ingresarPedido(nombreCliente, dirreccion, 
        numeroTelefonoCliente
        , cantidadDePizzas)
        while contador < int(CantidadDeIngredients):
                print ("1.  Pepperoni  ")
                print ("2.  Salchica  ")
                print ("3.  Carne ")
                print ("4.  Queso ")
                print ("5.  Piña ")
                print("  Ingrese Numero de Ingrediente ")
                opcion = int(input())
                if opcion == 1:
                    print("----------->")
                    print("SE Agrego Pepperoni ")
                    nuevoPedido.ListaIngredientes.ingresarNuevoIngrediente("Pepperoni", 3)
                    print("----------->")
                    contador += 1
                elif opcion == 2:
                    print("----------->")
                    print("SE Agrego Salchicha ")
                    nuevoPedido.ListaIngredientes.ingresarNuevoIngrediente("Salchicha", 4 )
                    print("----------->")
                    
                    contador += 1
                elif opcion == 3:
                    print("----------->")
                    print("SE Agrego Carne ")
                    nuevoPedido.ListaIngredientes.ingresarNuevoIngrediente("Carne", 10  )
                    print("----------->")
                   
                    contador += 1
                elif opcion == 4:
                    print("----------->")
                    print("SE Agrego Queso ")
                    nuevoPedido.ListaIngredientes.ingresarNuevoIngrediente( "Queso", 5  )
                    print("----------->")
               
                    contador += 1
                elif opcion == 5:
                    
                    print("----------->")
                    print("SE Agrego Piña  ")   
                    nuevoPedido.ListaIngredientes.ingresarNuevoIngrediente("Piña", 2 )

                    print("----------->")
                    contador += 1
                else :
                        print(" Numero O DATO INCORRECTOS ")
        print()
        tiempoPreparacion = nuevoPedido.ListaIngredientes.TiempoTotal()
        tiempoPreparacion = tiempoPreparacion*int(cantidadDePizzas)
        TiempoEspera = Lpedidos.Time(int(tiempoPreparacion))
        nuevoPedido.setTiempo(int(TiempoEspera))
        print()
        nuevoPedido.ListaIngredientes.mostrarIngredientes()
        print()
        


                    



if __name__ == "__main__":
    """nuevo = Lpedidos.ingresarPedido("nombrCliente", "direccionCliente"
    , "NumeroCliente", 1)
    nuevo.ListaIngredientes.ingresarNuevoIngrediente("nombreIngrediente", 5)
    nuevo2 = Lpedidos.ingresarPedido("nombrCliente22", "direccionCliente2"
    , "NumeroCliente4", 2)
    nuevo2.ListaIngredientes.ingresarNuevoIngrediente("nombreIngrediente3", 10)
    nuevo3 = Lpedidos.ingresarPedido("nombrCliente33", "direccionCliente9"
    , "NumeroCliente4", 5)
    nuevo3.ListaIngredientes.ingresarNuevoIngrediente("nombreIngrediente1", 10)"""

    menu()