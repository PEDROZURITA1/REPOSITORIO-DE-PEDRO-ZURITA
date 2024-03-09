# Función para convertir grados centígrados a Fahrenheit y Kelvin
def conversor(grados_cent):
  fahrenheit = (9/5) * grados_cent + 32
  kelvin = 273.15 + grados_cent
  return fahrenheit, kelvin

# Solicitar los grados centígrados al usuario
centigrados = int(input("Ingrese los grados centígrados: "))

# Convertir los grados
result_fahrenheit, result_kelvin = conversor(centigrados)

# Imprimir los resultados
print(centigrados, "grados centígrados es igual a", result_fahrenheit ,"grados Fahrenheit")
print(centigrados, "grados centígrados es igual a ",result_kelvin, "grados Kelvin")
