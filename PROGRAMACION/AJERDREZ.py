def dibujaMatriz(m):
  for i in range(len(m)):
    for j in range(len(m[i])):
      print(m[i][j],end=" ")
    print()
  print("\n")

def llenaTableroCerosUnos(matriz):
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
       if ((i+j) % 2==0):
         matriz[i][j] = "B"
       else:
         matriz[i][j] = "N"

  return matriz

def llenaTableroMovTorre(fila,columna):
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if (i==fila):
        matriz[i][j]="T"
      

  return matriz



matriz = [["2","7","9","77","7","7","7","7"],
          ["2","7","9","77","7","7","7","7"],
          ["2","7","9","77","7","7","7","7"],
          ["2","7","9","77","7","7","7","7"],
          ["2","7","9","77","7","7","7","7"],
          ["2","7","9","77","7","7","7","7"],
          ["2","7","9","77","7","7","7","7"],
          ["2","7","9","77","7","7","7","7"]]

matriz = llenaTableroCerosUnos(matriz)

dibujaMatriz(matriz)

matriz = llenaTableroMovTorre(2,1)

dibujaMatriz(matriz)