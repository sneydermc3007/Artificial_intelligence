import numpy as np

def cruce(poblacion):
   hijo1 = np.append(poblacion[0, :4], poblacion[1, 4:11])
   hijo2 = np.append(poblacion[1, :4], poblacion[0, 4:11])
   hijo3 = np.append(poblacion[2, :4], poblacion[3, 4:11])
   hijo4 = np.append(poblacion[3, :4], poblacion[2, 4:11])
   hijo5 = np.append(poblacion[4, :4], poblacion[5, 4:11])
   hijo6 = np.append(poblacion[5, :4], poblacion[4, 4:11])

   HIJOS = [hijo1, hijo2, hijo3, hijo4, hijo5, hijo6]
   print("\n\tCruce entre padres\n\t HIJOS:")
   HIJOS = np.array(HIJOS)
   print(HIJOS)