# Sabendo que o numero neperiano eh 2,718281 e sabendo que este numero eh fruto da serie abaixo,
# crie um programa que calcule neperiano atraves dos primeiros N (informado pelo usuario) termos da serie
#
# e = SUM(i=0 ate INFINITO)  1/i!
#


n=int(input("n?"))
e=0.0

for i in range(1,n,1):
        fat=1
        for j in range(1,i,1):
             fat=fat*j
        e=e+(1.0/fat)

print("e=",e)
