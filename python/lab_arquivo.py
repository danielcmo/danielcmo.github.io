import random

arq=open('lab.txt','r')

# dimensoes
l =arq.readline()
str1,str2 = l.split(" ")
n,m = int(str1), int(str2)
print ("dimensoes ",n,"x",m)

# aloca labirinto
lab = []
for i in range(n):
  linha=[0]*m
  lab.append(linha)

# carrega labirinto
for i in range(n):
   l = arq.readline()
   j = 0
   for cel in l.split(" "):
     if cel.strip('\n') == "0":
         lab[i][j] = " "
     else:
         lab[i][j] = "X"
     j=j+1
     
# jogador     
Ji,Jj = 0,0
lab[Ji][Jj] = "O"
     
# inimigo
fim = False
Ii,Ij = 0,0
while (not fim):
    Ii = random.randint(0,n-1)
    Ij = random.randint(0,m-1)
    if (lab[Ii][Ij] == " "):
        lab[Ii][Ij] = "W"
        fim = True

    
# imprime labirinto
for i in range(n):
    print(lab[i])
    
# jogo
fim = False

while (not fim):
    
    # movimento do jogador
    ent = input("w-cima s-baixo a-esquerda d-direita")
    if (ent=="w") and (Ji-1 >= 0) and (lab[Ji-1][Jj] != "X"):
        lab[Ji][Jj] = " "
        Ji = Ji - 1
        lab[Ji][Jj] = "O"
    if (ent=="s") and (Ji+1 < n) and (lab[Ji+1][Jj] != "X"):
        lab[Ji][Jj] = " "
        Ji = Ji + 1
        lab[Ji][Jj] = "O"
    if (ent=="a") and (Jj-1 >= 0) and (lab[Ji][Jj-1] != "X"):
        lab[Ji][Jj] = " "
        Jj = Jj - 1
        lab[Ji][Jj] = "O"    
    if (ent=="d") and (Jj+1 < n) and (lab[Ji][Jj+1] != "X"):
        lab[Ji][Jj] = " "
        Jj = Jj + 1
        lab[Ji][Jj] = "O"    
    
    # movimento do inimigo
    teste=False
    while (not teste):
        i = random.randint(-1,1)
        j = random.randint(-1,1)
        if ((i==0)or(j==0)): # proibi diagonais
          if (0 <= Ii+i < n) and (0 <= Ij+j < m) and (lab[Ii+i][Ij+j] != "X"): # proibi movimento invalido
            if (lab[Ii][Ij] == "W"):
              lab[Ii][Ij] = " "
            Ii = Ii + i
            Ij = Ij + j
            lab[Ii][Ij] = "W"
            teste = True
    
    # imprime labirinto
    for i in range(n):
        print(lab[i])

    # vitoria
    if (Ji==n-1) and (Jj==m-1):
        print("!!!VITORIA!!!")
        fim=True    
     
    # derrota
    if (Ji==Ii) and (Jj==Ij):
        print("!!!DERROTA!!!")
        fim=True    
