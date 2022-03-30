import random
import pandas as pd
import numpy as np
from sympy import pprint


def nueva_generacion(poblacion, porcentajes, num):
    # Añadiendo columna porcentajes
    poblacion = np.column_stack((poblacion, porcentajes[:, 4]))
    print("\tIndividuo con su respectivo porcentaje:")
    print(poblacion)

    # ordenando
    poblacion = poblacion[poblacion[:, 11].argsort()[::-1]]
    print("\n\t Individuos ordenados de mayor a menor")
    print(poblacion)

    print('\n\tNueva generacion')
    generacion = poblacion[poblacion[0:3,11].argsort()[::-1]]
    print(generacion)

    cromosomas,genes = 3,11

    Pesos = [0.5, 0.1, 0.5, 0.25, 0.15, 0.15, 0.5, 0.3, 0.2, 0.15, 0.2]
    Calorias = [500, 300, 100, 700, 300, 400, 500, 400, 560, 260, 90]

    nueva_poblacion = np.zeros([cromosomas, genes])

    for i in range(cromosomas):
        n = 1
        while n > 0:
            Apt_p = 0
            Apt_c = 0
            for j in range(genes):
                nueva_poblacion[i, j] = random.randint(0, 1)
                Apt_p = Apt_p + nueva_poblacion[i, j] * Pesos[j]
                Apt_c = Apt_c + nueva_poblacion[i, j] * Calorias[j]
            # Castigo al individuo que no cumpla el peso
            if Apt_p <= 2 and Apt_c >= 2300:
                n = 0

    print("\n\tNUEVA POBLACION GENERADA", nueva_poblacion.shape)
    print(nueva_poblacion)


    gen=generacion[0:10,0:11]
    matriz= np.concatenate((gen, nueva_poblacion))
    print("\n\tPOBLACION, generación",num+1, matriz.shape)
    print(matriz)
    return matriz