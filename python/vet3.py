n=int(input("n?"))
a=[]
b=[]
c=[]
d=[]
for i in range(n):
    print("a[",i,"]")
    a.append(int(input()))

for i in range(n):    
    print("b[",i,"]")
    b.append(int(input()))

for i in range(n):    
    print("c[",i,"]")
    c.append(int(input()))
    
for i in range(n):
   d.append(a[i])
   d.append(b[i])
   d.append(c[i])
  
print(d)

