import random

def mutacion(hijos):
    
    print("\n\tPosiciones aleatorias para mutar")
    for i in range(1, len(hijos)): # Para los ultimos 5
        numero_aleatorio = random.randint(0, 10)
        print(i, numero_aleatorio)
        if(hijos[i,numero_aleatorio] == 0):
            hijos[i,numero_aleatorio] = 1
        else:
            hijos[i,numero_aleatorio] = 0

    print("\tHijos mutados aleatoriamente")
    print(hijos)    
    return hijos