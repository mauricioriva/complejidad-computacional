import re

# Función que busca la arista de mayor costo
def max_costo(lista):
    max_valor = None
    for i in lista:
        if not max_valor:
            max_valor = i
        elif int(i[2]) > int(max_valor[2]):
            max_valor = i
    return max_valor

#Función que busca la arista de menor costo
def min_costo(lista):
    min_valor = None
    for i in lista:
        if not min_valor:
            min_valor = i
        elif int(i[2]) < int(min_valor[2]):
            min_valor = i
    return min_valor

#Función que parsea una cadena mediante el caracter , y crea una lista
def convertirCadena(string):
    lista = list(string.split(","))
    return lista

#Función que parsea una cadena mediante el caracter " " y crea una lista
def convertirLista(string):
    lista = list(string.split(" "))
    return lista

#Función que crea una lista de listas
def hacerListaDeListas(lista):
    aristas = []
    for item in lista:
        arista = convertirCadena(item);
        aristas.append(arista)
    return aristas

#Definición de las opciones del menú
def menu():
    print("[1] Ingresar un ejemplar")
    print("[2] Salir")

print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("Bienvenido, Favor de seleccionar una opción: ")
menu()
opcion = int(input(""))

while opcion != 2:
    if opcion == 1:
        print("")
        print("")
        print("Favor de ingresar la ruta del archivo que contiene el ejemplar: ")
        entrada = input('')

        grafo = []

        with open(entrada) as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                lugarActual = linea[:-1]
                grafo.append(lugarActual)

        nodos = grafo[0]
        nodos = re.sub("\[|\]","",nodos)
        nodos = convertirCadena(nodos)

        aristas = grafo[1]
        aristas = re.sub("\[|\]","",aristas)
        aristas = convertirLista(aristas)
        aristas = hacerListaDeListas(aristas)

        arista_mayor = max_costo(aristas)
        arista_menor = min_costo(aristas)

        print("")
        print ("Número total de vértices: ", len(nodos))
        print ("Número total de aristas: ", len(aristas))
        print ("La arista de peso máximo es: [", arista_mayor[0], ",", arista_mayor[1], "] con peso:", arista_mayor[2])
        print ("La arista de peso mínimo es: [", arista_menor[0], ",", arista_menor[1], "] con peso:", arista_menor[2])
        print("---------------------------------------------------------------")
        print("---------------------------------------------------------------")
        print("")
        print("")
        pass
    else:
        print("Opción inválida, favor de ingresar una opción nuevamente")
        print("")
    print("Favor de introducir una nueva opción: ")
    menu()
    opcion = int(input(""))

print("Gracias por usar nuestro programa. Adios");
print("---------------------------------------------------------------")
