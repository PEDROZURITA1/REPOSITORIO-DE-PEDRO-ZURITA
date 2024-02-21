# ORDEN EN ARREGLO MULTIDIMENSIONAL

def ordenar_fila(matriz, fila):
    for i in range(len(matriz[fila]) - 1):
        for j in range(len(matriz[fila]) - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

    return matriz


matriz = [[1, 7, 4], [8, 6, 2], [9, 3, 5]]
fila_a_ordenar = 1

matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

print("Matriz desordenada:")
for fila in matriz:
    print(fila)

print("Matriz ordenada:")
print(matriz_ordenada[fila_a_ordenar])

