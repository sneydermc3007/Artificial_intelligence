import random
import numpy as np
import pandas as pd
from evaluacion import *
from seleccion import *
from cruce import *

#Cantidad de generaciones
cant = int(input("Ingrese la cantidad de generaciones que desea generar: "))

#Paso 1, Generacion de población inicial
cromosomas, genes = 5, 10

#Datos del problema: Leche de soya (500,0.5), Galletas (300,0.1), Agua (100,0.5), Pan (700,0.25), 
# Huevo (300,0.15), Nueces (400,0.15), Yogurt (500,0.5), Manzana (400,0.3) 
# barra de chocolate (560, 0.2), Pan (260, 0.15)

Pesos=[0.5,0.1,0.5,0.25,0.15,0.15,0.5,0.3,0.2,0.15]
Calorias=[500,300,100,700,300,400,500,400,560,260]

poblacion = np.zeros([cromosomas,genes])

for i in range(cromosomas):
  n=1
  while n>0:
    Apt_p = 0
    Apt_c = 0
    for j in range(genes):
        poblacion[i,j] = random.randint(0, 1)
        Apt_p = Apt_p + poblacion[i,j]*Pesos[j]
        Apt_c = Apt_c + poblacion[i,j]*Calorias[j]
    #Castigo al individuo que no cumpla el peso
    if Apt_p<=2 and Apt_c>=2300:
      n=0

print("\n\tPOBLACION INICIAL",poblacion.shape)
print(poblacion)


for i in range(cant):
    #Paso 2, Evaluación de la aptitud de cada individuo
    poblacion_evaluada = evaluacion(poblacion, cromosomas, genes, Pesos, Calorias)
    
    #Paso 3, Selección de individuos
    seleccion_poblacion = seleccion(poblacion, poblacion_evaluada)
    
    #Paso 4, Cruce de individuos
    poblacion_mutada = cruce(seleccion_poblacion)
    
    #Paso 5, Mutación de los hijos

    #Paso 6, Evaluación de los hijos

    #Paso 7, Generando población nueva
