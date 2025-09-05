# Faca um programa que receba um N e um vetor de inteiros de
# tamanho N e ordene e imprima o vetor pelo metodo de ordenacao
# da selecao

n = int(input("n?"))
v        =[0]*(n)

for i in range(n):
    v[i]=(int(input("num. "+str(i))))

for i in range(n-1):
    for j in range(i+1,n):
        if (v[i]>v[j]):
            t      = v[i]
            v[i]   = v[j]
            v[j]   = t

print(v)
