n     = int(input("n?"))
t     = False

for i in range(1,n-2,1):
    if ((i*(i+1)*(i+2)) == n):
        print("numero triangular ", n,"=",i,"*",i+1,"*",i+2)
        t = True
        break

if (not t):
    print ("numero nao triangular")

