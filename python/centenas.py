##########Escreva um programa que receba um numero inteiro menor que 1000 e divida a quantidade de centenas, dezenas e unidades

x=int(input("Digite o numero desejado: "))

cont_centenas=0
cont_dezenas=0
cont_unidades=0

if x>=100:
    if x%100!=0:
        cont_centenas=x//100
        cont_unidades=x%10
        x=x//10


        if x%10!=0:

            cont_dezenas=x%10

            print(cont_centenas,"centenas",cont_dezenas,"dezenas",cont_unidades,"unidades")

        else:
            cont_dezenas=0
            print(cont_centenas, "centenas", cont_dezenas, "dezenas", cont_unidades, "unidades")

else:

    cont_unidades = x % 10
    x = x // 10

    if x % 10 != 0:

        cont_dezenas = x % 10
        print(cont_centenas, "centenas", cont_dezenas, "dezenas", cont_unidades, "unidades")

    else:
        cont_dezenas = 0
        print(cont_centenas, "centenas", cont_dezenas, "dezenas", cont_unidades, "unidades")

