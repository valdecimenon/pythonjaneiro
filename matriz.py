#matriz.py

print("Matriz usando lista...")

matriz = [
                   [3, 2, 6],  #sublista = linha da matriz
                   [3, 3, 8],
                   [1, 2, 5]
              ]

#imprime a matriz, uma linha por vez
for linha in matriz:
    print(linha)

lin = int(input("Numero da linha: "))
col = int(input("Numero da coluna: "))

print(matriz[lin][col])

#criando uma matriz por multiplicação
linha = [0] * 5  #5 colunas
matriz = [linha] * 3 #3 linhas
print(matriz)
