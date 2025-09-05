import random

# aloca rua de tamanho 16 (posicao 0 é a largada e 15 a chegada)
rua = ['  ']*16
rua[0] = 'XY'

# aloca buracos (faz voltar) e vitaminas (faz andar)
burvit    = ['  ']*16
burvit[0] = '00'
burvit[1] = '00'
burvit[2] = '-1'
burvit[3] = '+1'
burvit[4] = '00'
burvit[5] = '00'
burvit[6] = '-2'
burvit[7] = '00'
burvit[8] = '-1'
burvit[9] = '+1'
burvit[10] = '00'
burvit[11] = '-1'
burvit[12] = '-2'
burvit[13] = '00'
burvit[14] = '-4'
burvit[15] = '00'

# imprime rua com buracos e vitaminas
print("+ ou - = ",burvit)
print("rua    = ",rua)
print('')

fim = False  # marca o fim do jogo
vez = True   # de quem é a vez
x,y = 0,0    # posicao dos jogadores


while (not fim):
       
    if vez :
        # Jogador X
        
        # 1) joga dado (aleatorio entre 1 e 6) e calcula nova posicao de X  
        # 2) checa vitoria (se chegou ou passou da posicao 15), atualiza variavel fim e quebra laço
        # 3) adiciona buracos e vitaminas a posicao de X (use função int() para converter o texto do vetor burvit e descobrir quanto adiciona ou diminui)
        # 4) atualiza impressao do tabuleiro (só depois de calcular posicao final com +dado+vitamina ou +dado-buraco) 
           # 4.1) origem (cuidado que pode ESTAR junto com o Y, não apague o Y)
           # 4.2) destino (cuidado que pode FICAR junto com o Y, não apague o Y)
             
        
    else :
        # Jogador Y
        
        # mesma coisa do X, só que para Y
        
    
    # imprime rua com buracos e vitaminas depois da jogada
    print("+ ou - = ",burvit)
    print("rua    = ",rua)
    print('')
    
    # inverte jogador
    vez = not vez
    
     
    
   