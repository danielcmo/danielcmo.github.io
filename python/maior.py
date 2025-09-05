
######Faca um programa que dado 3 numeros inteiros distintos, imprima o maior

a = int(input())
b = int(input())
c = int(input())

if (a>b and a>c):
	print(a)
else:
	if (b>a and b>c):
		print(b)
	else:
		print(c)
