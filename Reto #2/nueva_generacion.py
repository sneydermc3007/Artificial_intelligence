import random
import pandas as pd
import numpy as np
from sympy import pprint


def nueva_generacion(poblacion, porcentajes):
    # Añadiendo columna porcentajes
    poblacion = np.column_stack((poblacion, porcentajes[:, 4]))
    print("\tIndividuo con su respectivo porcentaje:")
    print(poblacion)

    # ordenando
    poblacion = poblacion[poblacion[:, 11].argsort()[::-1]]
    print("\n\t Individuos ordenados de mayor a menor")
    print(poblacion)

    print('Nueva generacion')
    generacion = poblacion[poblacion[0:3,11].argsort()[::-1]]
    print(generacion)