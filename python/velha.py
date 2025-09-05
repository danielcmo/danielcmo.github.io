# Tabuleiro (todas as 9 posições do tabuleiro começam apenas com números)
t1,t2,t3,t4,t5,t6,t7,t8,t9 = '1','2','3','4','5','6','7','8','9'

# diz de quem é a vez. Se vez=True então a vez será do jogador 1 (X)
# caso contrário, se vez=False, será a vez do jogador 2 (O)
vez    = True

# variavel que indica se alguem venceu
venceu = False

# variável que conta o número total de jogadas (jogador 1 mais jogador 2)
acc    = 0

# enquanto ninguem vencer, o jogo continua
while not venceu :
    
    # imprime tabuleiro
    print( 'Jogo da Velha\n*****')
    print(t1,t2,t3)
    print(t4,t5,t6)
    print(t7,t8,t9)
    print( '*****\n')
    
    # diz qual jogador vai jogar (jogador1=X mais jogador2=O)
    if vez :
        print( "Jogador 1:")
    else :
        print( "Jogador 2:")
        
    # recebe do jogador corrente o número referente a posição a ser jogada
    pos = int(input("qual posicao (1-9) :"))
    
    ####### 1) se jogada invalida (numero fora do intervalo de 1-9) não faz nada e passa a vez para o outro jogador
    if (<.COMPLETAR.>):
        print('Jogada Invalida, passa a vez')
        vez = not vez
        continue
    
    ####### 2) se jogada repetida (posicao ja marcada) não faz nada e passa a vez para o outro jogador
    if (<.COMPLETAR.>):
        print('Jogada Repetida, passa a vez')
        vez = not vez
        continue
       
    
    ####### 3) marcar no tabuleiro a jogada (a posição escolhida vai ser marcada com a marca do jogador da vez)
    if vez :
        marca = 'X'
    else :
        marca = 'O'
        
    <.COMPLETAR.>
        
    ####### 4) checar condições de vitória (linhas, colunas e diagonais)
    if (<.COMPLETAR.>): # ds
       venceu = True
       continue
    
    ####### 5) checar se deu velha (empate)
    <.COMPLETAR.>
    
    ####### 6) alternar a vez para o outro jogador
    vez = not vez
        
    acc=acc+1

# imprime tabuleiro
print( 'Jogo da Velha\n*****')
print(t1,t2,t3)
print(t4,t5,t6)
print(t7,t8,t9)
print( '*****\n')

# determina o vencedor 
if (<.COMPLETAR.>):
    print ("Jogador 1 ganhou!\n")
if (<.COMPLETAR.>):
    print ("Jogador 2 ganhou!\n")
# ou se deu velha
if (<.COMPLETAR.>):
    print("deu velha")
