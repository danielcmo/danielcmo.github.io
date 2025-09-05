def nul(mat):
    l = 0
    c = 0
    a = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            a = a + abs(mat[i][j])
        if a == 0:
            l = l + 1
        a = 0
    
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            a = a + abs(mat[j][i])
        if a == 0:
            c = c + 1
        a = 0
    print(l, c)

vetor = []
matriz = []
n = int(input())
m = int(input())
for i in range(n):
    for j in range(m):
        vetor.append(int(input()))
    matriz.append(vetor)
    vetor = []
print(matriz)
nul(matriz)
