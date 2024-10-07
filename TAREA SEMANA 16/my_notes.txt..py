# 1. Escritura en el archivo
with open('my_notes.txt', 'w') as file:
    file.write("Esta es mi primera nota.\n")
    file.write("Segunda nota: Recuerda comprar leche.\n")
    file.write("Tercera nota: Terminar el proyecto de Python.")

# 2. Lectura del archivo
with open('my_notes.txt', 'r') as file:
    for line in file:
        print(line.rstrip())

# El archivo se cierra automáticamente al salir del bloque with