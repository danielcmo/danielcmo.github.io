mport random

# dimensões do labirinto
n = 5
m = 5

# aloca labirinto
lab = []
for i in range(n):
  linha=[0]*m
  lab.append(linha)

# preenche labirinto
lab[0][0] = "O"
lab[0][1] = "X"
lab[0][2] = "X"
lab[0][3] = " "
lab[0][4] = "X"

lab[1][0] = " "
lab[1][1] = " "
lab[1][2] = "X"
lab[1][3] = " "
lab[1][4] = "X"

lab[2][0] = "X"
lab[2][1] = " "
lab[2][2] = " "
lab[2][3] = " "
lab[2][4] = " "

lab[3][0] = " "
lab[3][1] = " "
lab[3][2] = "X"
lab[3][3] = "X"
lab[3][4] = " "

lab[4][0] = "X"
lab[4][1] = " "
lab[4][2] = " "
lab[4][3] = " "
lab[4][4] = " "

# Que os jogos comecem ...

# jogador
Ji,Jj = 0,0

# inimigo
Ii,Ij = 0,0
fim = False
while (not fim):
    Ii = random.randint(0,n-1)
    Ij = random.randint(0,m-1)
    if (lab[Ii][Ij] == " "):
        lab[Ii][Ij] = "W"
        fim = True

# inimigo esperto
fim = False
I2i,I2j = 0,0
while (not fim):
    I2i = random.randint(0,n-1)
    I2j = random.randint(0,m-1)
    if (lab[I2i][I2j] == " "):
        lab[I2i][I2j] = "Z"
        fim = True

# imprime labirinto
for i in range(n):
    print(lab[i])

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
        if ((i==0)and(j!=0)) or ((i!=0)and(j==0)): # proibi diagonais
          if (0 <= Ii+i < n) and (0 <= Ij+j < m) and (lab[Ii+i][Ij+j] != "X") and (lab[Ii+i][Ij+j] != "Z"): # proibi movimento invalido
            if (lab[Ii][Ij] == "W"):
              lab[Ii][Ij] = " "
            Ii = Ii + i
            Ij = Ij + j
            lab[Ii][Ij] = "W"
            teste = True
    
     # movimento do inimigo esperto
    i,j=0,0
    if (Ji < I2i) and (lab[I2i-1][I2j] != "X") and (lab[I2i-1][I2j] != "W"):
        i=-1
    else:
        if (Ji > I2i) and (lab[I2i+1][I2j] != "X") and (lab[I2i+1][I2j] != "W"):
            i=1
        else:
            if (Jj < I2j) and (lab[I2i][I2j-1] != "X") and (lab[I2i][I2j-1] != "W"):
                j=-1
            else:
                if (Jj > I2j) and (lab[I2i][I2j+1] != "X") and (lab[I2i][I2j+1] != "W"):
                    j=1
        
    if (lab[I2i][I2j] == "Z"):
        lab[I2i][I2j] = " "
            
    I2i = I2i + i
    I2j = I2j + j
    lab[I2i][I2j] = "Z"

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

    # derrota
    if (Ji==I2i) and (Jj==I2j):
        print("!!!DERROTA!!!")
        fim=True    
