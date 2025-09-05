# dada uma matriz informada pelo usuario, fazer uma funcao
# que diga quantas linhas zeradas ela tem

def nulas(matriz,linhas,colunas):
    contador,zeradas = 0,0
    for a in range(linhas):
        contador = 0
        for b in range(colunas):
            if matriz[a][b] == 0:
                contador = contador + 1
            if b == colunas -1:
                if contador == colunas:
                    zeradas = zeradas + 1
    print("Linhas nulas:",zeradas)

M = []
m = int(input("Colunas:"))
n = int(input("Linhas:"))
for x in range(n):
    A = [0]*m
    M.append(A)
for i in range(n):
    for j in range(m):
        M[i][j] = int(input("Elemento:"))

nulas(M,n,m)
            