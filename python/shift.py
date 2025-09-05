# Faca um programa que leia um vetor de inteiros de 42 posicoes e depois da leitura, faca um processamento para empurrar
# todos os valores 13 para as ultimas posicoes do vetor

n        =42
v        =[0]*n

for i in range(n):
    v[i]=(int(input("num. "+str(i))))

# ultimo elemento diferente de 13
for i in range(n-1,0,-1):
    if (v[i] != 13):
       ultimo = i
       break

for i in range(n):
    # identifica o zero
    if (v[i] == 13):
        temp      = v[i]
        v[i]      = v[ultimo]
        v[ultimo] = temp
        ultimo    = ultimo - 1

    # parar se alcancar o ultimo elemento diferente de 13
    if (i>=ultimo):
        break
                                            
