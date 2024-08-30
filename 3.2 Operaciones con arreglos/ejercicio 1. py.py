
#FUNDAMENTOS DE PROGRAMACION
# Matriz de 3 x 3
matriz = [
    [7,2,10],
    [5,8,3],
    [6,1,4]
]
print(matriz)

# funcion buscar_valor especifico

def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j
valor_buscado = 8
#print(buscar_valor(matriz,valor_buscado))

if valor_buscado == valor_buscado:
    print("valor encontrado en la posicion",buscar_valor(matriz,valor_buscado))
else:
    print("valor incorrercto")

