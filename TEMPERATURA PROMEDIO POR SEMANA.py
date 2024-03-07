def calcular_temperatura_promedio(datos, semana):
    temperaturas_promedio = {}
    for ciudad, semanas in datos.items():
        total_temperaturas = sum(semanas[semana])
        total_dias = len(semanas[semana])
        temperatura_promedio = total_temperaturas / total_dias
        temperaturas_promedio[ciudad] = temperatura_promedio
    return temperaturas_promedio

# DATOS DE TEMPERATURAS DE CASCALES,LAGO AGRIO Y SEVILLA
datos = {
    'CASCALES': [[15,
                  26,
                  37,
                  48,
                  59],
                 [54,
                  45,
                  36,
                  27,
                  18],
                 [13,
                  24,
                  35,
                  46,
                  57],
                 [52,
                  43,
                  34,
                  25,
                  16]],
    'LAGO AGRIO': [[10,
                    21,
                    32,
                    43,
                    54],
                   [59,
                    40,
                    31,
                    22,
                    13],
                   [18,
                    29,
                    30,
                    41,
                    52],
                   [57,
                    48,
                    39,
                    20,
                    11]],
    'SEVILLA': [[10,
                 21,
                 32,
                 43,
                 54],
                [59,
                 40,
                 31,
                 22,
                 13],
                [18,
                 29,
                 30,
                 41,
                 52],
                [57,
                 48,
                 39,
                 20,
                 11]]
}

# Solicitar al usuario que ingrese el número de semana
semana = int(input("Ingresa el número de la semana (0, 1, 2, 3): "))

# Verificar si el número de semana es válido
if semana < 0 or semana >= len(next(iter(datos.values()))):
    print("Número de semana inválido.")
else:
    # Calcula la temperatura promedio de cada ciudad para la semana dada
    temperaturas_promedio = calcular_temperatura_promedio(datos, semana)

    # Muestra los resultados
    for ciudad, temperatura in temperaturas_promedio.items():
        print(f"La temperatura promedio en {ciudad} durante la semana {semana} es {temperatura:.2f} grados.")
