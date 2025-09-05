# Dizemos que uma matriz A nxn eh um Quadrado Magico se a soma dos elementos da cada linha,
# a soma dos elementos de cada coluna, e a soma dos elementos das diag. Principal e secundaria
# sao iguais. Faca um programa para ler uma matriz A nxn (informado pelo usuario) e dizer se eh
# ou nao eh um quadrado magico

n=int(input("n?"))

A = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
    A.append(l)

#diagonal principal
magico=0
for i in range(n):
    magico = magico + A[i][i]
    
#diagonal secundaria
soma=0
for i in range(n):
    soma = soma + A[i][n-1-i]
if (soma != magico):
    print("nao eh magico")
    exit()

#linhas
for i in range(n):
    soma=0
    for j in range(n):
        soma=soma+A[i][j]
    if (soma != magico):
        print("nao eh magico")
        exit()
        
#colunas
for j in range(n):
    soma=0
    for i in range(n):
        soma=soma+A[i][j]
    if (soma != magico):
        print("nao eh magico")
        exit()
        
print("eh magico")


