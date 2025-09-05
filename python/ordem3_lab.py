
# Ordem 3 -- Receba 3 valores inteiros. Se os tres forem iguais, imprime "iguais". 
# Se apenas dois deles forem iguais, imprima a soma dos numeros iguais menos o numero diferente. 
# Se os 3 forem distintos, imprima de forma decrescente.

a = int(input())
b = int(input())
c = int(input())

if (a == b) and (b == c):
  print("iguais")
else:
  if (a == b):
    print(a+b-c)
  else:
    if (a == c):
      print(a+c-b)
    else:
      if (b == c):
        print(b+c-a)
      else:
          # ordena de forma decrescente
          if (a>b and a>c):
	          print(a)
	          if (b>c):
		          print(b,c)
	          else:
		          print(c,b)
          else:
	          if (b>c):
		          print(b)
		          if (c>a):
			          print(c,a)
		          else:
			          print(a,c)
	          else:
		          print(c)
		          if (b>a):
			          print(b,a)
		          else:
			          print(a,b)

