from nodeLista import nodoLista
import os 
import webbrowser

class lista: 
    
    ##-----------Constructor---------##
    def __init__(self):
        self.inicio=None 

    ##-----Insertar----------##
    def insertar(self,anime):
        nuevoNodo = nodoLista(anime)
        if self.inicio==None:
            self.inicio=nuevoNodo
        else:
            auxNodo = self.inicio 
            while auxNodo.siguiente is not None: 
                auxNodo=auxNodo.siguiente
            auxNodo.siguiente=nuevoNodo

    ## ----------- Imprimir ----------- ##
    def imprimirFormaUno(self):
        auxNodo = self.inicio
        strGrafica=" digraph G { \n"
        ##----------while para crear nodos
        while auxNodo is not None:
            strGrafica += '{}[label="{}",color = "green",arrowhead = "diamond",fillcolor="red",style="filled",shape="box"];\n'.format(auxNodo.anime,auxNodo.anime)
        
            auxNodo=auxNodo.siguiente
        ##----------while para Unir nodos
        auxNodo=self.inicio
        while auxNodo is not None:
            if auxNodo.siguiente is None:
                None
            else: 
                strGrafica += '{}->{};\n'.format(auxNodo.anime,auxNodo.siguiente.anime)
            auxNodo=auxNodo.siguiente
        ##-------------Creacion de texto plato y conversion
        strGrafica+="}"
        documentotxt="listaForma1.txt"
        with open(documentotxt,'w') as grafica: 
            grafica.write(strGrafica)
        pdf="listaForma1.pdf"
        os.system("neato -Tpdf "+documentotxt+" -o "+pdf)
        webbrowser.open(pdf)

    
