# Faca um programa que receba um inteiro qualquer  e imprima o numero correspondente ao inverso dele. Ex: 12345 → 54321 → 108642.
# OBS:  Nao trabalhar com strings, apenas com inteiros, isto eh, receber o numero com int(input()) e nao converter para string. 
# Resolva a questao matematicamente.

num = int(input("numero:"))
invertido = 0
while num>0:
    invertido = invertido * 10 + num % 10
    num = num // 10
print (2*invertido)

