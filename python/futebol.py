import random
import math

# recebe 4 times com suas medias de gols. Os times irao compor 
# as duas semifinais e a final 
nA = input('nome do time A:')
mA = float(input('media de gols do time A:'))
nB = input('nome do time B:')
mB = float(input('media de gols do time B:'))
nC = input('nome do time A:')
mC = float(input('media de gols do time A:'))
nD = input('nome do time B:')
mD = float(input('media de gols do time B:'))
nV1 = ''
mV1 = 0.0
nV2 = ''
mV2 = 0.0

print(nA)
print(nB)
print(nC)
print(nD)

print(mA)
print(mB)
print(mC)
print(mD)

# o numero de gols do time na partida eh um numero aleatorio 
# entre 0 e o teto da media de gols do time
print('Semifinal 1')
gA = random.randint(0,math.ceil(mA))
gB = random.randint(0,math.ceil(mB))
print(nA,' ',gA,' x ',gB,' ',nB)

# em caso de empate, o primeiro time avanca sempre
if (gA >= gB):
	print(nA,' se classificou')
	nV1 = nA
	mV1 = mA
else:
	print(nB,' se classificou')
	nV1 = nB
	mV1 = mB

print('Semifinal 2')
gC = random.randint(0,math.ceil(mC))
gD = random.randint(0,math.ceil(mD))
print(nC,' ',gC,' x ',gD,' ',nD)

# em caso de empate, o primeiro time avanca sempre
if (gC >= gD):
	print(nC,' se classificou')
	nV2 = nC
	mV2 = mC
else:
	print(nD,' se classificou')
	nV2 = nD
	mV2 = mD

print('Final')
gV1 = random.randint(0,math.ceil(mV1))
gV2 = random.randint(0,math.ceil(mV2))
print(nV1,' ',gV1,' x ',gV2,' ',nV2)

# em caso de empate, penalts (random de 0 a 5), se empatar nos penalts, joga moeda
if (gV1 > gV2):
	print(nV1,' CAMPEAO!')
elif (gV2 > gV1):
	print(nV2,' CAMPEAO!')
else:
	# penalidades
	print('Penalidades')
	gV1 = random.randint(0,5)
	gV2 = random.randint(0,5)
	print(nV1,' ',gV1,' x ',gV2,' ',nV2)

	if (gV1 > gV2):
		print(nV1,' CAMPEAO!')
	elif (gV2 > gV1):
		print(nV2,' CAMPEAO!')
	else:
		# moeda, 'cara' o primeiro eh campeao, 'coroa' o segundo
		print('Moeda')
		moeda = random.randint(0,1)
		if (moeda==0):
			print('cara, ',nV1,' CAMPEAO!')
		else:
			print('coroa, ',nV2,' CAMPEAO!')





