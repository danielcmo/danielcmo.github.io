for i in range(1000,10000,1):
    n1 = i//100
    n2 = i % 100
    
    if ((n1+n2)**2 == i):
        print(i)

