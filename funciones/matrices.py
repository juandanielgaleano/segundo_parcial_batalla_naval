
def crear_matriz(filas = 10, columnas = 10, valor = 0, dificultad = 0)->list:
    """crea una matriz por defecto de 10 * 10

    Args:
        filas (int, optional): cantidad de filas. Defaults to 10.
        columnas (int, optional): cantidad de columnas. Defaults to 10.
        valor (int, optional): los casilleros se inicializaran en 0. Defaults to 0.
        dificultad (int, optional): _description_. Defaults to 0.

    Returns:
        list: Devuelve una matriz cuadrada
    """
    matriz = []
    for i in range(filas):
        if dificultad == 2 or dificultad == 4:
            fila = ([valor] * columnas * dificultad) * dificultad    
        else:
            fila = ([valor] * columnas) 
        matriz +=[fila]
    
    return matriz