
######Faca um programa que dado o nome do produto, preco e quantidade. Escreva o nome do produto e o valor total pago segundo o desconto

### ate 10 unidades -> valor total
### de 11 a 20      -> 10%
### de 21 a 50      -> 20%
### acima de 50     -> 90%

n = input('nome?')
p = float(input('preco?'))
q = int(input('qtd?'))
tt=0

if q<=10:
	tt=q*p
else:
	if (q<=20):
		tt=q*p*0.9
	else:
		if (q<=50):
			tt=q*p*0.8
		else:
			tt=q*p*0.1

print("produto=",n," total=",tt)


