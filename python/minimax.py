#Na teoria de sistemas defini-se um elemento minimax de uma matriz como 
#sendo o menor elemento da linha em que se encontra o maior elemento da matriz
# ( considere que nao existem elementos repetidos na matriz). Faça um programa
# que receba uma matriz 10x10 e determine a posicao do elemento minimax da matriz

m = []
for i in range(10):
    l = []
    for j in range(10):
        l.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
    m.append(l)

maior    = m[0][0]
l_maior  = 0
for i in range(10):
    for j in range(10):
        if (m[i][j] > maior):
            maior = m[i][j]
            l_maior = i
            
menor = m[l_maior][0]
c_menor=0
for j in range(10):
    if (m[l_maior][j] < menor):
        menor = m[l_maior][j]
        c_menor = j
        
print("posicao minimax é linha",l_maior," e coluna ",c_menor)
