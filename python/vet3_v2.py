n=int(input("n?"))
a=[0]*(n)
b=[0]*(n)
c=[0]*(n)
d=[0]*(3*n)
for i in range(n):
    print("a[",i,"]")
    a[i] = int(input())

for i in range(n):
    print("b[",i,"]")
    b[i] = int(input())

for i in range(n):
    print("c[",i,"]")
    c[i] = int(input())

j=0
for i in range(n):
   d[j]   = a[i]
   d[j+1] = b[i]
   d[j+2] = c[i]
   j      = j+3

print(d)
