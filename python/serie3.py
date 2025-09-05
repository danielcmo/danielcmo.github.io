
#
# S = X + 4*X**2/2 - 9*X**4/5 + 15*X**6/11 - 22*X**8/23
#

x = int(input("X?"))

s     = x
a     = 4
b     = 2
c     = 2
sinal = 1
inc   = 5
print(a,'X^',b,"/",c)

for i in range(1,30):
    s = s + (sinal * (a*(x**b))/(c*1.0))
    
    a     = a + inc
    inc   = inc + 1
    b     = b + 2
    c     = (2*c) + 1 
    sinal = sinal * -1
    print(a,'X^',b,"/",c)
    
print("s=",s)


