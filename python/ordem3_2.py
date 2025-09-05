
######Faca um programa que dado 3 numeros inteiros distintos, 
# imprima em ordem crescente

a = int(input())
b = int(input())
c = int(input())

if (a<b and a<c):
	print(a)
	if (b<c):
		print(b,c)
	else:
		print(c,b)
else:
	if (b<c):
		print(b)
		if (c<a):
			print(c,a)
		else:
			print(a,c)
	else:
		print(c)
		if (b<a):
			print(b,a)
		else:
			print(a,b)

