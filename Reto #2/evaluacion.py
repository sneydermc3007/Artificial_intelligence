
import random
import pandas as pd
import numpy as np
from sympy import pprint

def evaluacion (poblacion, cromosomas, genes, Pesos, Calorias):
    
    Apt_peso=np.zeros([cromosomas,1])
    Apt_cal=np.zeros([cromosomas,1])
    for i in range (0,cromosomas,1):
        for j in range (0,genes,1):
            Apt_peso[i,0] = Apt_peso[i,0] + poblacion[i,j]*Pesos[j]
            Apt_cal[i,0] = Apt_cal[i,0] + poblacion[i,j]*Calorias[j]

    P_peso=np.zeros([cromosomas,1])
    P_cal=np.zeros([cromosomas,1])
    Sumpeso=sum(Apt_peso)
    Sumcalorias=sum(Apt_cal)
    for i in range(0,cromosomas):
        P_peso[i,0]=Apt_peso[i,0]/Sumpeso
        P_cal[i,0]=Apt_cal[i,0]/Sumcalorias

    np.round(P_peso, decimals=1)
    np.round(P_cal, decimals=1)    

    #Probabilidad total
    P_total=np.zeros([cromosomas,1])
    for i in range(0,cromosomas):
        P_total[i,0]=P_peso[i,0] + P_cal[i,0]


    print("\n\tEvaluación de la población [Peso, Calorias, Promedio Peso, Promedio Claorias, Pormedio Total]")
    #Mostrar una sola tabla con toda la evaluación 
    np.set_printoptions(suppress=True)
    evaluacion_poblacion = np.concatenate((Apt_peso, Apt_cal, P_peso, P_cal, P_total), axis=1)
    evaluacion_poblacion = np.round(evaluacion_poblacion, decimals=3)
    print(evaluacion_poblacion, "\n")
    return evaluacion_poblacion