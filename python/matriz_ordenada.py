# receba uma matriz A, de dimensoes n por m e imprima ela ordenada

n=int(input("n"))
m=int(input("m"))

#cria matriz de zeros 
a=[]
for i in range(n):
    linha=[0]*m
    a.append(linha)

#recebe matriz no vetor
v=[]
for i in range(n*m):
    num = int(input())
    v.append(num)

#ordena vetor
for i in range(n*m):
    for j in range((n*m)-1):
        if (v[j] > v[j+1]):
            t      = v[j]
            v[j]   = v[j+1]
            v[j+1] = t
 
#passa vetor para matriz 
ind=0 
for i in range(n):
    for j in range(m):
       a[i][j] = v[ind]
       ind = ind + 1
         
#imprime matriz
for i in range(n):
    print(a[i])
     
   
