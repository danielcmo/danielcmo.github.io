s   = 0.0
a   = 2
b   = 3
inc = 1

for i in range(1,31,1):
    
    if (i % 2 == 0):
        s   = s - (a / b)
        print ("-",a," / ",b,)
    else:
        s   = s + (a / b)
        print (a," / ",b,)
        
    a   = a + 4
    inc = inc + 1
    b   = b + inc
    
print("s=",s)
