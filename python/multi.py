m = int(input())
n = int(input())
p = int(input())

a=[]
for i in range (n):
    j=[0]*m
    a.append(j)
    
b=[]
for i in range (m):
    j=[0]*p
    b.append(j)
    
c=[]
for i in range (n):
    j= [0]*p
    c.append(j)
    
for i in range (n):
    for j in range (m):
        a[i][j] = int(input())

for i in range (m):
    for j in range (p):
        b[i][j]= int(input())
        
for i in range (n):
    for j in range (p):
        for k in range (m):
            c[i][j] = c[i][j] + (a[i][k] * b[k][j])

for i in range (n):
    print(a[i])

for i in range (m):
    print(b[i])

for i in range (n):
    print(c[i])