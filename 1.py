# Creación y escritura en el archivo my_notes.txt
with open("my_notes.txt", "w") as file:
    # Escribiendo notas personales en el archivo
    file.write("1. SACAR A PASEAR AL PERRO.\n")
    file.write("2. HACER EL ARROZ.\n")
    file.write("3. IR DE COMPRAS.\n")

# Lectura del archivo my_notes.txt
with open("my_notes.txt", "r") as file:
    # Leyendo el contenido línea por línea
    for line in file:
        # Mostrando cada línea leída en la consola
        print(line.strip())  # strip() para eliminar los caracteres de nueva línea

# El archivo se cierra automáticamente después de salir del bloque 'with'
