
######Faca um programa que dado o salario bruto(SB) de um funcionario, calcular o salario liquido (SL) aplicando o desconto

###10% sobre SB se 500<= SB <800
###15% sobre SB  se SB>=800 e <1000
###80% sobre SB se SB>=1000
### Sem desconto caso SB<500

salario_bruto=float(input("Digite o salario bruto: "))
desconto=0
salario_liquido=salario_bruto

if salario_bruto>500:

    if salario_bruto >= 500 and salario_bruto < 800:
        desconto = (salario_bruto * 10) / 100
        salario_liquido = salario_bruto - desconto
        
    if salario_bruto >= 800 and salario_bruto < 1000:
        desconto = (salario_bruto * 15) / 100
        salario_liquido = salario_bruto - desconto
        
    if salario_bruto >= 1000:
        desconto = (salario_bruto * 80) / 100
        salario_liquido = salario_bruto - desconto
        
else:
    salario_liquido=salario_bruto

print(salario_bruto,salario_liquido,desconto)


