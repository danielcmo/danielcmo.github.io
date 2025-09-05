s = 1.0
a = 3
b = 3
c = 2
print (c," / (",a,"**",b,")")

for i in range(1,50,1):
    s = s + (c / (a**b))
    a = a + 2
    b = b + 1
    c = c * 2
    print (c," / (",a,"**",b,")")
    
print("s=",s)

