from funciones import matrices
import random


def posicionar_submarino(matriz:list)->list:
    
    filas = len(matriz)
    columnas = len(matriz[0])

    while True:        
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)        
        if matriz[fila][columna] == 0:
            matriz[fila][columna] = 1
            break

    return matriz
    

def posicionar_destructor(matriz:list)->list:

    filas = len(matriz)
    columnas = len(matriz[0])

    while True:        
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 2)        
        if matriz[fila][columna] == 0 and  matriz[fila][columna+1] == 0:
            matriz[fila][columna] = 1
            matriz[fila][columna+1] = 1
            break

    return matriz

def posicionar_crucero(matriz:list)->list:

    filas = len(matriz)
    columnas = len(matriz[0])

    while True:        
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 3)        
        if matriz[fila][columna] == 0 and matriz[fila][columna+1] == 0 and matriz[fila][columna+2] == 0:
            matriz[fila][columna] = 1
            matriz[fila][columna+1] = 1
            matriz[fila][columna+2] = 1
            break
        
    return matriz

def posicionar_acorazado(matriz:list)->list:

    filas = len(matriz)
    columnas = len(matriz[0])

    while True:        
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 4)        
        if matriz[fila][columna] == 0 and matriz[fila][columna+1] == 0 and matriz[fila][columna+2] == 0 and matriz[fila][columna+3] == 0:
            matriz[fila][columna] = 1
            matriz[fila][columna+1] = 1
            matriz[fila][columna+2] = 1
            matriz[fila][columna+3] = 1
            break
        
    return matriz