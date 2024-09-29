# Creación de la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=20):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función desde el programa principal
monto_total_1 = 2500  # Ejemplo de monto total de la compra
monto_total_2 = 5500  # Otro ejemplo de monto total de la compra
porcentaje_descuento_2 = 25  # Porcentaje de descuento personalizado para la segunda compra

# Primera llamada: solo se proporciona el monto total, se usa el porcentaje de descuento por defecto (10%)
descuento_1 = calcular_descuento(monto_total_1)

# Segunda llamada: se proporcionan tanto el monto total como un porcentaje de descuento personalizado (15%)
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)

# Mostrar los resultados de las dos llamadas a la función
print(f"Monto total 1: ${monto_total_1}")
print(f"Descuento aplicado (20% por defecto): ${descuento_1}")
print(f"Monto final después del descuento: ${monto_total_1 - descuento_1}\n")

print(f"Monto total 2: ${monto_total_2}")
print(f"Descuento aplicado (25%): ${descuento_2}")
print(f"Monto final después del descuento: ${monto_total_2 - descuento_2}")
