def dibujaMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()
    print("\n")

def rotaMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_rotada = []
    for i in range(columnas):
        fila = []
        for j in range(filas):
            fila.append(matriz[filas-j-1][i])
        matriz_rotada.append(fila)
    return matriz_rotada

m = [[0,0,1,0,0],
     [0,1,1,1,0],
     [0,0,1,0,0],
     [0,0,1,0,0]]

dibujaMatriz(m)
matriz_rotada = rotaMatriz(m)
for fila in matriz_rotada:
    print(fila)