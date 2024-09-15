# Definir una matriz 3D con valores numéricos
matriz = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

# Inicializar la variable de suma
suma = 0

# Iterar a través de los niveles, filas y columnas para sumar elementos
for nivel in matriz:
    for fila in nivel:
        for elemento in fila:
            suma += elemento

# Mostrar el resultado de la suma
print("La suma de todos los elementos de la matriz 3D es:", suma)
