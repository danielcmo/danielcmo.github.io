from mip import *

############################ leitura de arquivo ###################################
arq = open("TPI_F_0.txt", "r")

line             = arq.readline().strip().split()
ni, nj, c, q, nl = map(int, line)

#matriz de adjacência 
matriz_g_p = [[-1 for _ in range(nj)] for _ in range(ni)]

for i in range(nl):
    line                                = arq.readline().strip().split()
    facilidade, cliente, g_ij, p_ij     = map(eval, line)
    matriz_g_p[facilidade-1][cliente-1] = (g_ij, p_ij) # veja que estamos descontando -1 para começar do 0

print(ni,nj,c,q,nl)
print(matriz_g_p)
####################################################################################
