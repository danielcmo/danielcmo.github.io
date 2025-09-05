# dado m e n inteiros positivos, encontrar o par x,y onde
# 0<= x <= m, e 0<= y <= n que maximize a funcao
# xy - x² + y

def pares(m,n):
    maior= newx =newy = 0
    for x in range(0,m+1):
        for y in range(0,n+1):
            val = (x*y) - (x**2) +y
            if val> maior:
                maior = val
                newx=x
                newy = y
    return newx,newy

m = int(input("Digite m:"))
n = int(input("Digite n:"))
x,y = pares(m,n)
print(x,y)