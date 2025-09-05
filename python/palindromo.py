# faca um programa que receba um inteiro de 5 digitos e diga se ele eh palindromo
num = int(input())
aux = num

d5  = aux % 10
aux = int(aux/10)

d4 = aux % 10
aux = int(aux/10)

d3 = aux % 10
aux = int(aux/10)

d2 = aux % 10
aux = int(aux/10)

d1 = aux 

if (d5==d1) and (d4==d2):
	print('palindromo')
else:
	print('nao eh palindromo')


 
