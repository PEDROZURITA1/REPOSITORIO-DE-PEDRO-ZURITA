# busqueda de arreglo multidimensional

def buscar_valor(matriz, valor):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == valor:
                return True, (i, j)

    return False, None


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
valor_a_buscar = 5

encontrado, posicion = buscar_valor(matriz, valor_a_buscar)

if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición ({posicion[0]}, {posicion[1]})")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz")