import itertools
from agente_viajero import leer_ejemplar


class TLP(object):
    '''Clase TLP del algoritmo de verificacion del agente viajero'''
    def __init__(self, ruta, cota) -> None:
        '''Constructor'''
        self.cota = cota
        (self.nodos,
        self.aristas,
        self.arista_max,
        self.arista_min) = leer_ejemplar(ruta)

    def get_permutaciones(self):
        '''Obtenemos la lista con todas las permutaciones posibles'''
        perm_iterator = itertools.permutations(self.nodos)
        lp = []
        cont = 0
        for perm in perm_iterator:
            lp.append(perm)
            cont = cont + 1
            if cont > len(self.nodos):
                break
        return lp

    def __get_peso_arista(self, v, v_1):
        '''Obtenemos el peso de la arista dados 2 nodos'''
        for i in self.aristas:
            u, u_1, peso = i
            if v == u and v_1 == u_1:
                return int(peso)
        return 0

    def verifica(self, certificado):
        '''Algoritmo de Verificacion'''
        costo = 0 # Costo total
        # Recorre el certificado
        for i, v in enumerate(certificado):
            if i == len(certificado) - 1:
                v_1 = certificado[0]
            else:
                v_1 = certificado[i + 1]
            costo += self.__get_peso_arista(v, v_1) # Suma el peso de la arista
        # Comparamos el costo respecto a la cota
        if self.cota < costo:
            return "El certificado no satisface el problema.", costo
        return None, costo


if __name__ == '__main__':
    MENU = """
    [1] Ingresar un ejemplar
    [2] Salir
    """

    print("---------------------------------------------------------------")
    print("---------------------------------------------------------------")
    print("Bienvenido, Favor de seleccionar una opción: ")
    print(MENU)
    opcion = int(input(""))

    while opcion != 2:
        if opcion == 1:
            print("Por favor ingrese la ruta del archio con el ejemplar: ")
            ruta = input("")
            print("Por favor ingrese una cota: ")
            cota = int(input(""))

            tlp = TLP(ruta, cota) # Creamos un objeto TLP
            permutaciones = tlp.get_permutaciones()
            # El usuario escoge la permutacion
            for i, permutacion in enumerate(permutaciones):
                print(f"[{i}] {permutacion}")

            print("Por favor eliga una permutación: ")
            permutacion = int(input(""))
            error, costo = tlp.verifica(permutaciones[permutacion])

            print(f"\nNúmero de vertices: {len(tlp.nodos)}")
            print(f"Número de aristas: {len(tlp.aristas)}")
            print(f"Cota: {tlp.cota}")
            print(f"Costo: {costo}")

            if error is None:
                print("El certificado satisface el problema.\n")
            else:
                print("El certificado no satisface el problema.\n")
        else:
            print("Opción inválida, favor de ingresar una opción nuevamente\n")
        print("Favor de introducir una nueva opción: ")
        print(MENU)
        opcion = int(input(""))
    print("Hasta la proxima.\n")
