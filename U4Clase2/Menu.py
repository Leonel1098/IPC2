from colorama import Fore
from Actor import Actor
from ListaSimpleEnlazada import ListaSimpleEnlazada
from Pelicula import Pelicula
import xml.etree.ElementTree as ET

def menu():
    opcion = ''
    listaActores = ListaSimpleEnlazada()
    while opcion != '8':
        print(Fore.CYAN + "-----------------MENU---------------")
        print(Fore.CYAN + "1 --- CREAR ACTOR")
        print(Fore.CYAN + "2 --- IMPRIMIR ACTORES")
        print(Fore.CYAN + "3 --- AGREGAR PELICULA A ACTOR")
        print(Fore.CYAN + "4 --- MOSTRAR PELICULAS POR ACTOR")
        print(Fore.CYAN + "5 --- CARGAR DESDE ARCHIVO")
        print(Fore.CYAN + "6 --- GRAFICAR LISTA DE ACTORES")
        print(Fore.CYAN + "8 --- SALIR")

        opcion = input(Fore.YELLOW + "Seleccione una opcion del menu \n")

        if opcion == '1':
            c = input(Fore.BLUE + "Ingrese los datos del actor en el siguiente formato nombre-edad-nacionalidad\n")
            datos = c.split('-')
            nuevoActor = Actor(datos[0], datos[1], datos[2])
            listaActores.append(nuevoActor)
            print(Fore.GREEN + "Se registro el actor con exito!! \n")
        elif opcion == '2':
            listaActores.print()
        elif opcion == '3':
            nombre = input(Fore.BLUE + "Ingresar nombre de actor: \n")
            actor = listaActores.buscarActorByNombre(nombre)

            if actor is None:
                print(Fore.RED + "El actor no se encuentra registrado en la lista")
            else:
                c = input(Fore.BLUE + "Ingrese los datos de la pelicula en el siguiente formato nombre-papel-anio-duracion\n") 
                datos = c.split('-')
                nuevaPelicula = Pelicula(datos[0], datos[1], datos[2], datos[3])
                actor.peliculas.append(nuevaPelicula)
                print(Fore.GREEN + "Se registro la pelicula con exito!! \n")
        elif opcion == '4':
            nombre = input(Fore.BLUE + "Ingresar nombre de actor: \n")
            actor = listaActores.buscarActorByNombre(nombre)

            if actor is None:
                print(Fore.RED + "El actor no se encuentra registrado en la lista")
            else:
                actor.peliculas.print()
        elif opcion == '5':
            nombreArchivo = input(Fore.BLUE + "Ingrese el nombre del archivo XML\n")
            ruta = './' + nombreArchivo
            listaActores = cargaArchivo(ruta)
            print(Fore.GREEN + "Se cargo el archivo con exito!!\n")
        elif opcion == '6':
            listaActores.graficar()


def cargaArchivo(ruta):
    tree = ET.parse(ruta)
    actores = tree.getroot()
    listaActoresDesdeXml = ListaSimpleEnlazada()
    for actorXml in actores:
        nuevoActor = Actor(actorXml.attrib['nombre'], actorXml.attrib['edad'], actorXml.attrib['nacionalidad'])
        listaActoresDesdeXml.append(nuevoActor)
        for peliculaXml in actorXml.iter('pelicula'):
            nuevaPelicula = Pelicula(peliculaXml.attrib['nombre'], peliculaXml.attrib['papel'], peliculaXml.attrib['anio'], peliculaXml.text )
            nuevoActor.peliculas.append(nuevaPelicula)
    return listaActoresDesdeXml



menu()

