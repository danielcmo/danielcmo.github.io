# Faca um jogo de pedra papel e tesoura, onde o jogador e o computador escolhem entre 1-papel 2-tesoura 3-pedra 
# (a jogado do computador eh aleatoria). Ganha o jogo quem vender 3 vezes primeiro


# Jogo da pedra, tesoura e papel
import random
v=0
d=0

sair=False
while (not sair):
    j1=random.randint(1, 3)
    j2=int(input("qual sua jogada: 1-papel 2-tesoura 3-pedra"))
    
    if (j2==1):
        
        if (j1==3):
            print("pedra, voce ganhou")
            v=v+1
        
        if (j1==2):
            print("tesoura, voce perdeu")
            d=d+1
        
        if (j1==1):
            print("papel, empatou")
    
    if (j2==2):
        
        if (j1==3):
            print("pedra, voce perdeu")
            d=d+1
        
        if (j1==2):
            print("tesoura, empatou")
        
        if (j1==1):
            print("papel, voce ganhou")
            v=v+1
            
    if (j2==3):
        
        if (j1==3):
            print("pedra, empatou")
        
        if (j1==2):
            print("tesoura, ganhou")
            v=v+1
        
        if (j1==1):
            print("papel, voce perdeu")
            d=d+1
            
    if (v==3 or d==3):
        sair=True

if (v==3):
    print("VITORIA :)")
else:
    print("DERROTA :(")

