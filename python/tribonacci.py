# faca uma funcao para imprimir o n primeiros numeros
# da serie de Tribonacci

def tribonacci(n):
    t = []
    trib = [1, 1, 2]
    if n <= 3:
        for i in range(n):
            t.append(trib[i])
    else:
        t = [1, 1, 2]
        for i in range(3, n):
            t.append(t[i-1] + t[i-2] + t[i-3])
    return t

n = int(input('Quantos termos de Tribonacci deseja ver?'))
print(tribonacci(n))