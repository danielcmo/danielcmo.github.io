#
# x = SUM(i=0 ate 100)  1/(2i)!
#


n=101
x=0.0

for i in range(1,n,1):
        fat=1
        for j in range(1,2*i,1):
             fat=fat*j
        x=x+(1.0/fat)

print("x=",x)
