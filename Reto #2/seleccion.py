import random
import pandas as pd
import numpy as np

def seleccion(poblacion, porcentajes):

    #Añadiendo columna porcentajes
    poblacion = np.column_stack((poblacion, porcentajes[:, 4]))
    print("\tIndividuo con su respectivo porcentaje:")
    print(poblacion)
    
    #ordenando
    poblacion = poblacion[poblacion[:, 10].argsort()[::-1]]
    print("\n\t Individuos ordenados de mayor a menor")
    print(poblacion)

    #obteniendo la mejor aptitud para ducplicarla
    mejor_Apt = poblacion[0]

    print("\n\t Población con mejor aptitud duplicada")
    nueva_poblacion = poblacion[:4,]
    nueva_poblacion = np.append(nueva_poblacion, [mejor_Apt], axis=0)
    print(nueva_poblacion)

    poblacion = nueva_poblacion[:, :10]
    
    return poblacion


