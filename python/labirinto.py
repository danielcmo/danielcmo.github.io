# dimensões do labirinto
n = 5
m = 5

# aloca labirinto
lab = []
for i in range(n):
  linha=[0]*m
  lab.append(linha)

# preenche labirinto. O jogador é representado por "O" e as paredes por "X"
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

# variavel que checa vitoria
fim = False

# posiçao inicial do jogador
Ji,Jj = 0,0

while (not fim):
    
    ent = input("w-cima s-baixo a-esquerda d-direita: ")
    
    # 1) Movimenta jogador, cuidado com jogadas irregulares (em cima de paredes e fora do tabuleiro)
    #    e cuidado para não deixar "rastros"
    
    # imprime labirinto
    for i in range(n):
        print(lab[i])

    # 2) Checa vitória (chegar na posição 4,4)   
     
