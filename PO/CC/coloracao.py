from mip import *

############################ ENTRADAS DO ARQUIVO #######################

arq  = open("TPI_COL_1.txt", "r")
line = arq.readline().strip().split()
n, m, F = map(int, line[2:])

#conj. de arestas
E = []

# Obtendo arestas
for _ in range(m):
    line = arq.readline().strip().split()
    i, j =  map(int, line[1:])
    E.append((i, j))
    
print(n,m,F)
print(E)

############################################################################

