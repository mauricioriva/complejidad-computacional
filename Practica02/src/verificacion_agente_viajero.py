import itertools
from agente_viajero import leer_ejemplar


class TLP(object):
    def __init__(self, ruta, cota) -> None:
        self.cota = cota
        (self.nodos,
        self.aristas,
        self.arista_max,
        self.arista_min) = leer_ejemplar(ruta)

    def get_permutaciones(self):
        return list(itertools.permutations(self.nodos))

    def __get_peso_arista(self, v, v_1):
        for i in self.aristas:
            u, u_1, peso = i
            if v == u and v_1 == u_1:
                return int(peso)
        return 0

    def verifica(self, certificado):
        costo = 0

        for i, v in enumerate(certificado):
            if i == len(certificado) - 1:
                v_1 = certificado[0]
            else:
                v_1 = certificado[i + 1]
            costo += self.__get_peso_arista(v, v_1)

        if self.cota < costo:
            return "El certificado no satisface el problema.", None
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

            tlp = TLP(ruta, cota)
            permutaciones = tlp.get_permutaciones()

            for i, permutacion in enumerate(permutaciones):
                print(f"[{i}] {permutacion}")
                if i > 10:
                    break

            print("Por favor eliga una permutación: ")
            permutacion = int(input(""))
            error, costo = tlp.verifica(permutaciones[permutacion])

            print(f"\nNúmero de vertices: {len(tlp.nodos)}")
            print(f"Número de aristas: {len(tlp.aristas)}")
            print(f"Cota: {tlp.cota}")

            if error is None:
                print(f"Costo: {costo}")
                print("El certificado satisface el problema.\n")
            else:
                print("El certificado no satisface el problema.\n")
        else:
            print("Opción inválida, favor de ingresar una opción nuevamente\n")
        print("Favor de introducir una nueva opción: ")
        print(MENU)
        opcion = int(input(""))
    print("Hasta la proxima.\n")
