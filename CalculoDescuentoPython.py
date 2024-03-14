# calculadora de descuento

def calcular_descuento(monto_total, porcentaje_descuento=10):
 
  descuento = monto_total * porcentaje_descuento / 100
  total_con_descuento = monto_total - descuento
  return descuento, total_con_descuento

# subtotal y descuento
monto_compra = 200
porcentaje_descuento = 20

descuento, total_con_descuento = calcular_descuento(monto_compra, porcentaje_descuento)

print(f"Subtotal: {monto_compra}")
print(f"Descuento ({porcentaje_descuento}%): {descuento}")
print(f"Total con descuento: {total_con_descuento}")
