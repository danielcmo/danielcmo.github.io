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

# imprime labirinto
for i in range(n):
    print(lab[i])

# Que os jogos comecem ...
# jogo
fim = False
Ji,Jj = 0,0

while (not fim):
    
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
    
    # imprime labirinto
    for i in range(n):
        print(lab[i])

    # vitoria
    if (Ji==n-1) and (Jj==m-1):
        print("!!!VITORIA!!!")
        fim=True    
     
