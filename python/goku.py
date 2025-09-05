###### Escreva um programa que recebe 3 numeros e retorna a soma deles, porem se houver numeros repetidos, o valor deles
###### nao e contabilizado. Alem disso se 2 dos 3 numeros forem consecutivos, so o maior sera considerado. Se os 3 forem
###### consecutivos imprima "Goku"

x=input("Digite o numero: ")
y=input("Digite o numero: ")
z=input("Digite o numero: ")

soma=0
if x!=y and x!=z and y!=z:
    if x+1==y and y+1==z:
        print("Goku")

    if x+1==y:
        soma=y+z

    if x-1==y:
        soma=x+z

    if x + 1 == z:
        soma = y + z

    if x - 1 == z:
        soma = x + y

    if z+1== y:
        soma=y+x

    if z-1== y:
        soma=z+x

    else:
        soma=x+y+z

if x==y or x==z or y==z:
    if x==y:
        soma=z
    if x==z:
        soma=y
    if y==z:
        soma=x

    if x==y and x==z:
        soma=0

print(soma)