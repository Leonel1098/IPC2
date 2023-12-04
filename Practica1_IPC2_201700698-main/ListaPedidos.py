from nodoPedido import nodoPedido
import graphviz
class ListaPedidos:
    def __init__(self):
        self.primero = None
        self.siguiente = None
        self.size = 0
    def ingresarPedido(self, nombrCliente,direccionCliente,NumeroCliente,cantidadDePizzas):
        nuevoPedido = nodoPedido(nombrCliente, direccionCliente, NumeroCliente, cantidadDePizzas)   
        self.size += 1
        if self.primero is None:
            self.primero = nuevoPedido
            self.ultimo = nuevoPedido
        else :
            self.ultimo.setSiguientePedido(nuevoPedido)
            self.ultimo = nuevoPedido
        
        return nuevoPedido
    
    def Time(self, tiempoPreparacion):
        tiempoEspera = 0 
        tmp = self.primero
        for i in range(self.size):
            if tmp.getTiempo() is None :
                tiempoEspera += tiempoPreparacion
                return tiempoEspera
            else:
                tiempoEspera += int(tmp.getTiempo())
            tmp = tmp.getSiguientePedido()
        tiempoEspera += tiempoEspera+tiempoPreparacion
        return tiempoEspera

    def MostrarListaDePedidos(self):
        tmp = self.primero
        print("--------------------Lista de Pedidos ----------------------------------")
        for i in range(self.size):
            print(i+1)
            print("TIEMPO DE ESPERA ESTIMADO --> ", tmp.getTiempo()," min")
            print("----------INFO DEL CLIENTE ---------------------")
            print("Nombre :      ", tmp.getNombreCliente())
            print("Direccion :   ", tmp.getDirreccion())
            print("Numero :      ", tmp.getNumeroCliente())
            print("-----INFO DEL PEDIDO  ----")
            print("Cantidad de Pizzas Pedidas: " , tmp.getCandtida())
            tmp.ListaIngredientes.mostrarIngredientes()
            tmp = tmp.siguiente
        print("-------------------------------------------------------------------------")

            
    
    def eliminar_dato(self):
        actual = self.primero
        anterior = self.primero
        tiempo = actual.getTiempo()
        for i in range(self.size):
            
            if i == 0:
                print("salio Pirmero Pedido ")
                self.primero = actual.siguiente
                self.size -= 1
                
            else:
                print(actual.getNombreCliente())
                self.siguiente = actual.siguiente
                
               
            actual = actual.siguiente
        
        return tiempo
    def ActualizacionTiempo(self, tiempoArestar):
        tmp = self.primero
        for i in range(self.size):
            timeEspera =  tmp.getTiempo()
            actualizacion = timeEspera-tiempoArestar
            tmp.setTiempo(actualizacion)  

            tmp = tmp.siguiente

    def Graficar(self):
        tmp = self.primero

        grap = ""
        g = graphviz.Digraph('G',filename='structs_revisited.gv', node_attr={'shape': 'rarrow'})
        for i in range(self.size):
        
                grap +=  "'"+tmp.getNombreCliente()+"',"

                g.node('Estruct'+str(i)+'',"PEDIDO DE \n"+str(tmp.getNombreCliente()))                
                tmp = tmp.siguiente


        g.view()