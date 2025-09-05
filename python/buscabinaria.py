#vetor de teste
vet = [4, 10, 80, 90, 91, 99, 100, 101]
num = int(input("numero"))

esquerda, direita, achou = 0, len(vet)-1, False
while esquerda <= direita:
	meio = (esquerda + direita) // 2
	aux_num = vet[meio]
	print (esquerda,meio,direita)
	if num == aux_num:
		print("posicao= ",meio)
		achou = True
		break
	else:
		if num > aux_num:
			esquerda = meio + 1
		else:
			direita = meio - 1

if (not achou):
	print("nao achou :(")
		
