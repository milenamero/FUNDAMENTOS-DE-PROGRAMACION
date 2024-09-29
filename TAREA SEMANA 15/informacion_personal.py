# Creación del diccionario con información ficticia
informacion_personal = {
    "nombre": "Yandel Cevallos",
    "edad": 17,
    "ciudad": "Portoviejo",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado a la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"  # Modificar la ciudad a Guayaquil

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"  # Número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)

# Imprimir el diccionario final después de todas las operaciones
print("Diccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

