#DICCIONARIO DE INFORMACION PERSONAL

# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "María",
    "edad": 18,
    "ciudad": "Cascales",
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Policia"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0989724087"

# Eliminar la clave "------"
del informacion_personal["profesion"]

# Imprimir el diccionario resultante
print(informacion_personal)

