#Craps
import random

dados = random.randint(1,6) + random.randint(1,6)
print("dados=",dados)
 
#primeira rodada
if dados == 7 or dados == 11:
    print("Venceu")
else:
    if dados == 2 or dados == 3 or dados == 12:
        print("Perdeu")
    else:
        # demais rodadas
        ponto = dados
        jogar = True
        
        while jogar:
            dados = random.randint(1,6) + random.randint(1,6)
            print("dados=",dados)
        
            if dados == ponto:
                print("Venceu")
                jogar=False
            else:
                if dados == 7:
                    print("Perdeu")
                    jogar=False


