''' Implementación del problema de Máxima satisfactibilidad con pesos - MAX-SAT'''

with open('ejemplarMAXSAT.txt') as file:
    clausulas = []
    variables = set([])
    sum = 0
    count = 0
    for line in file:
        count += 1 
        sum += int(line.split()[0])
        num_clausulas= clausulas.append(line[0].strip())
        for i in line:
            if(i != " " and i != "\n" and i != "-" and not i.isdigit()):
                variables.add(i[0])
    num_clausulas= len(clausulas)
    promedio = sum / count
    num_variables=len(variables)
file.close()


#Imprime el número de variables
print("Número de variables:", num_variables)
#Imprime el número de cláusulas
print("Número de cláusulas:", num_clausulas)
#Imprime el promedio de pesos
print("Promedio de pesos:", promedio)
