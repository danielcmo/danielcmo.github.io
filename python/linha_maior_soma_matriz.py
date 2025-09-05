#Faça um programa que leia uma matriz nxm (informado pelo usuário) de inteiros e retorne
# a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma.

n=int(input("n?"))
m=int(input("m?"))

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
    matriz.append(linha)

l_max    = -1
soma_max = -1
for i in range(n):
    soma  = 0
    for j in range(m):
        soma = soma + matriz[i][j]
    if (i==0):
        l_max=i
        soma_max=soma
    else:
        if (soma > soma_max):
            l_max=i
            soma_max=soma

print('linha', l_max, ' soma ',soma_max)
