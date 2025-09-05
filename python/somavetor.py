n = int(input("n?"))        
a        =[0]*(n+1)
b        =[0]*(n+1)
c        =[0]*(n+1)

for i in range(1,n+1):
    a[i]=(int(input("num. "+str(i))))
for i in range(1,n+1):
    b[i]=(int(input("num. "+str(i))))

vaium=0
for i in range(n,0,-1):
    s     = a[i]+b[i]+vaium
    c[i]  = s%10
    vaium = s//10
    
c[0]=vaium
print(c)

