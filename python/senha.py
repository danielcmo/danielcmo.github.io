# Faca um programa que implementa o jogo da senha: O computador escolhe aleatoriamente uma senha 
# (valor inteiro entre 0 e 100) sem o conhecimento do jogador; O jogador  tem 10 chances para descobrir a senha; 
# A cada tentativa do jogador, o programa deve avisar se o valor digitado eh maior,menor ou igual a senha; 
# Se o valor digitado em uma tentativa tiver uma diferenca igual ou menor a 3 para a senha, o programa deve avisar que "TA QUENTE!".
# Neste caso, nenhuma outra mensagem deve ser emitida. Ao final do jogo, se for o caso, enviar a mensagem "Perdeu" ou "Ganhou"; 
# Ao final de uma partida, permita ao usuario jogar novamente.

import random
import math

denovo = 1

while (denovo == 1):
    rdn = random.randint(1,100)
    tent = 10
    print()
    print('Tente adivinhar o numero secreto de 1 a 100! Voce tera 10 tentativas!')
    print()
    while tent > 0:
        tent = tent - 1
        ch = int(input('Numero: '))
    
        if (ch == rdn):
            print('Parabens! Voce acertou! O numero secreto eh: %d' % rdn, "com",tent,"tentativas")
            break
        else:
            if (math.fabs(rdn-ch) <= 3):
                print("TA QUENTE")
            else:
                if ch > rdn:
                    print('O numero secreto eh menor!', "(",tent,"tentativas)")
                else:
                    if ch < rdn:
                        print('O numero secreto eh maior!', "(",tent,"tentativas)")
                
    if tent == 0:
        print()
        print('Que pena! Voce perdeu! Mais sorte da proxima vez!')
        print('O numero secreto eh: %d' % rdn)
    
    denovo = int(input("quer jogar de novo? 1-sim 2-nao"))

