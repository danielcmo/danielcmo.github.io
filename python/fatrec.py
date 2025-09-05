# faca um fatorial recursivo

def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n-1)
num = int(input("Digite n: "))
print(fat(num))