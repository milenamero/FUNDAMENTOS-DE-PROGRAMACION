# ejercicio 2 matriz de de 3 x 3
matriz = [
    [5,2,9],
    [4,10,3],
    [7,1,8]
]
print(matriz)
#metodo de ordenamiento buble_sort
def buble_sorf(fila):
    #algritmo buble sord
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1]= fila[j-1], fila[j]
                print(fila)

print("matriz original ")
print(matriz)
buble_sorf(matriz[0])
print(matriz)