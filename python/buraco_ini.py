# inicio da questao do jogo do buraco 

import random

tam      = 15  # tamanho do tabuleiro
numb     = 5   # numero de buracos
tamd     = 3   # numero de faces do dado

# vetor de 0's e 1's indicando se a posicao tem uma trilha (0) ou um buraco (1)
v        =[0]*(tam+1) 

# vetor do tabuleiro (que deve ser impresso)
t        =[' ']*(tam+1) 

#--- gera tabuleiro (inteiro) ---

#gera 'numb' buracos, lembrando que tem que gerar buracos apenas em posicoes que nao existam buracos ainda
i=0
while (i<numb):
    p   = random.randint(1,tam)
    if (v[p]==0):
        v[p]=1 
        i=i+1

#--- gera tabuleiro (string) ---

# de acordo com o vetor 'v', atualiza o vetor 't' com buracos, trilhas e jogadores para ser impresso
for i in range(1,tam+1):
    if (v[i]==0):
        t[i]="x"
    else:
        t[i]="o"
t[0]='J12'
print("Inicio")
print(t)    

.....
