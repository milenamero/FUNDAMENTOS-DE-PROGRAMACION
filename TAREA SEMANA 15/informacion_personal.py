# 1. Crear un diccionario
informacion_personal = {
    "nombre": "Yandel Cevallos",
    "edad": 17,
    "ciudad": "Portoviejo"
}

# 2. Acceder y modificar valores
informacion_personal["ciudad"] = "Crucita"  # Cambiamos la ciudad
informacion_personal["profesion"] = "Programador"  # Agregamos una nueva clave-valor

# 3. Verificar existencia de claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "1234567890"

# 4. Eliminar una clave
del informacion_personal["edad"]

# 5. Imprimir el diccionario final
print(informacion_personal)

