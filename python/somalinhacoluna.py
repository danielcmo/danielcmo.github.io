#Faca um programa que le uma matriz A mxn (informado pelo usuario) e cria dois
# vetores SL de dimensao n e SC de dimensao m, que contenham respectivamente,
# as somas das linhas e das colunas de A. No fim imprimir A, SC e SL

n=int(input("n?"))
m=int(input("m?"))

A = []
for i in range(n):
    l = []
    for j in range(m):
        l.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
    A.append(l)
    
SL = [0]*n
SC = [0]*m

for i in range(n):
    for j in range(m):
        SL[i]=SL[i]+A[i][j]
        
for i in range(m):
    for j in range(n):
        SC[i]=SC[i]+A[j][i]
        
print(A)
print(SL)
print(SC)