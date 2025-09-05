# Faca um programa que leia dois valores x e y, e calcula o valor da divisao inteira de x por y
# Nao eh permitido usar as operacoes de divisao e resto de
# divisao do Python (use apenas soma e subtracao).

x     = int(input("x?"))
y     = int(input("y?"))
cont  = 0
acc   = 0

for i in range(y,x+1,y):
        cont = cont + 1
        acc  = acc + y

print ("divisao=",cont)    
