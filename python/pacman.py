# Pac-Man
import random
import colorama

# dimensões do labirinto
n          = 8
m          = 7
n_past     = 32 #número de pastilhas
vita_t_max = 10 # numero de rodadas que pac-man passa vitaminado

# strings dos personagens (colocando cores e negrito nas strings)
sP  = '\033[33m' + '\033[1m' + 'P' +'\033[0m' # amarelo negrito
sZ  = '\033[31m' + '\033[1m' + 'Z' +'\033[0m' # vermelho negrito
sW  = '\033[34m' + '\033[1m' + 'W' +'\033[0m' # azul negrito
sO  = '\033[32m' + '\033[1m' + 'O' +'\033[0m' # verde negrito

# posicoes de inicio do Pac-Man e dos inimigos (fantasmas)
xP = 5
yP = 3
xW = 0
yW = 3
xZ = 0 
yZ = 4

# aloca labirinto
lab = []
for i in range(n):
  linha=['-']*m
  lab.append(linha)

# preenche labirinto
lab[0][0]   = sO
lab[0][2]   = "X"
lab[xW][yW] = sW
lab[xZ][yZ] = sZ
lab[0][5]   = "X"
lab[0][6] = sO

lab[1][0] = "X"
lab[1][2] = "X"
lab[1][5] = "X"

lab[2][2] = "X"
lab[2][3] = "X"

lab[3][0] = "X"

lab[4][0] = "X"
lab[4][1] = "X"
lab[4][3] = "X"
lab[4][4] = "X"

lab[xP][yP] = sP

lab[6][1] = "X"
lab[6][3] = "X"
lab[6][5] = "X"
lab[6][6] = "X"

lab[7][0] = sO
lab[7][3] = "X"
lab[7][6] = sO

# Que os jogos comecem ...

# jogador
Ji,Jj      = xP,yP
pastilhas  = 0
vitaminado = False  # se pac-man esta vitaminado
vita_t     = 0      # quando tempo resta de vitamina

# inimigos
Ii,Ij       = xW,yW
I_pastilha  = False # se na posicao do inimigo tem uma pastilha ou em branco
I2i,I2j     = xZ,yZ
I2_pastilha = False # se na posicao do inimigo tem uma pastilha ou em branco

# imprime labirinto
print('*************************')
for i in range(n):
    print('* ',end='')
    for j in range(m):
        print(" "+lab[i][j]+" ",end='')
    print(' *')
print('*************************')
print("\npastilhas  = ",pastilhas)
print("vitaminado = ",vitaminado," (",vita_t,"s)","\n")


