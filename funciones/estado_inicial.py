from funciones import matrices
import random


def posicionar_submarino(matriz:list)->list:
    """Recibe una matriz en la que se busca una posicion aleatoria vacia para cargarla con el valor 1

    Args:
        matriz (list): Recibe una matriz cuadrada

    Returns:
        list: Devuelve una matriz en la que se cargo en una posicion aleatorio el valor 1
    """
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
    """Recibe una matriz en la que se cargan 2 valores consecutivos en una posicion aleatorio los valores 1

    Args:
        matriz (list): Matriz cuadrada

    Returns:
        list: Devuelve una matriz en la que se cargo en una posicion aleatoria 2 valores consecutivos
    """
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
    """Recibe una matriz donde se carga en una posicion aleatorio vacia 3 valores consecutivos

    Args:
        matriz (list): Matriz cuadrada

    Returns:
        list: Devuelve una matriz cargada en una posicion aleatoria 3 valores consecutivos en 1
    """
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
    """La funcion recibe una matriz y verifica si una posicion aleatorio esta libre para cargar 4 valores consecutivos en 1

    Args:
        matriz (list): Matriz cuadrada

    Returns:
        list: Devuelve una matriz donde se cargo en una posicion aleatorio 4 valores consecutivos en 1
    """
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