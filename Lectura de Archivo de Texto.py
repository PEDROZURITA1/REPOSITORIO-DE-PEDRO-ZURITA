# Lectura del archivo my_notes.txt
with open("my_notes.txt", "r") as file:
    # Leyendo el contenido línea por línea
    for line in file:
        # Mostrando cada línea leída en la consola
        print(line.strip())  # strip() para eliminar los caracteres de nueva línea

# El archivo se cierra automáticamente después de salir del bloque 'with'