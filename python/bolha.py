# Faca um programa que receba um N e um vetor de inteiros de
# tamanho N e ordene e imprima o vetor pelo metodo de ordenacao
# da bolha

n = int(input("n?"))
v        =[0]*(n)

for i in range(n):
    v[i]=(int(input("num. "+str(i))))

for i in range(n):
    for j in range(n-1):
	    if (v[j]>v[j+1]):
		t      = v[j]
		v[j]   = v[j+1]
		v[j+1] = t

print(v)
