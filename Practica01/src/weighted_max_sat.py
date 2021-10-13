# Función que lee el ejemplar y optiene los datos
def leer_ejemplar(ruta):
    clausulas = []
    variables = set()
    num_clausulas = None
    with open(ruta) as ejemplar:
        suma_pesos = 0
        contador = 0
        lineas = ejemplar.readlines()
        # Verificación de tipo de archivo
        if lineas[0] != "TIPO=weighted_max_sat\n":
            return "Tipo de ejemplar incorrecto", None
        for indice, linea in enumerate(lineas):
            if indice != 0:
                contador += 1 
                suma_pesos += int(linea.split()[0])
                num_clausulas = clausulas.append(linea[0].strip())
                for i in linea:
                    if(i != " " and i != "\n" and i != "-" and not i.isdigit()):
                        variables.add(i[0])
        num_clausulas= len(clausulas)
        promedio = suma_pesos / contador
        num_variables=len(variables)
    ejemplar.close()
    return None, (num_clausulas, num_variables, promedio)

if __name__ == "__main__":
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
            error, res = leer_ejemplar(ruta)
            if error is None:
                numero_clausulas, numero_variables, promedio = res
                print(f"Número de variables: {numero_variables}")
                print(f"Número de clausulas: {numero_clausulas}")
                print(f"Promedio de pesos: {promedio}\n")
            else:
                print(f"""
                ---------------------------------------
                {error}
                ---------------------------------------
                """)
        else:
            print("Opción inválida, favor de ingresar una opción nuevamente\n")
        print("Favor de introducir una nueva opción: ")
        print(MENU)
        opcion = int(input(""))
    print("Hasta la proxima.\n")
