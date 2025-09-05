def funcao(n,m):
    valor1=0
    valor2=0
    r=0
    for x in range(m+1):
        for y in range(n+1):
            p=x*y-x**2+y
            if p>r:
                r=p
                valor1=x
                valor2=y
    print(valor1)
    print(valor2)
    
m=int(input())
n=int(input())
funcao(n,m)
