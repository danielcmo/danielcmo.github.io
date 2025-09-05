#Gere uma jogada de 3 dados (de 6 lados) aleatoriamente. 
# O programa deve imprimir a soma dos numeros se eles (os 3) forem consecutivos, caso contrario, 
# retorne a multiplicacao dos numeros que sao iguais (se eles existirem), se nao existirem imprima "nao deu"

import random

d1 = random.randint(1,6)
d2 = random.randint(1,6)
d3 = random.randint(1,6)
print (d1,d2,d3)

if ((d1==d2+1) and (d1==d3+2) or 
    (d1==d3+1) and (d1==d2+2) or
    (d2==d1+1) and (d2==d3+2) or
    (d2==d3+1) and (d2==d1+2) or
    (d3==d1+1) and (d3==d2+2) or
    (d3==d2+1) and (d3==d1+2)):
    print(d1+d2+d3)
else:
  if ((d1==d2) and (d2==d3)):
    print(d1*d2*d3)
  else:
    if (d1==d2):
      print (d1*d2)
    else:
      if (d1==d3):
        print (d1*d3)
      else:
        if (d2==d3):
          print(d2*d3)
        else:
          print("nao deu") 
