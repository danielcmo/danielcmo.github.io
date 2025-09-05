# Escreva um programa que le um vetor de 100 numeros inteiros e imprima o numero que aparece mais vezes
# (se houver empate, pode ser qualquer um). Alem disso, imprima a posicao da sua primeira aparicao no
# vetor e quantas vezes ele aparece.

n        =10
v        =[0]*n
cont     =0
pos1     =-1
max_cont =0
max_pos1 =-1

for i in range(n):
    v[i]=(int(input("num. "+str(i))))

for i in range(n):
    cont =0
    pos1 =-1
    for j in range(n):
        if (v[i]==v[j]):
            cont=cont+1
            
            if(pos1==-1):
                pos1=j
        
    if (max_cont<cont):    
        max_cont =cont
        max_pos1 =pos1

print("número ",v[max_pos1], "aparece primeiro em ",max_pos1," e ",max_cont," vezes")
