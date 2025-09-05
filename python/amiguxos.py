# Escreva um programa para identificar e dois numeros sao AMIGUXOS. 
# Dois numeros sao amiguxos quando cada um eh iguala soma dos divisores do outro numero (excluindo apenas o proprio numero). 
# Ex: 220 e 284 sao amiguxos pois a soma dos divisores de 220 (1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110) eh igual a 284 e a soma dos divisores de 284 (1, 2, 4, 71, 142) eh igual a 220


a = int(input())
b = int(input())
s1 = 0
s2 = 0

for x in range(1,a):
    if a % x == 0:
        s1 = s1 + x

for y in range(1,b):
    if b % y == 0:
        s2 = s2 + y

if s2 == a and s1 == b:
    print("amiguxos")
else:
    print("nao amiguxos")

