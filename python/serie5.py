#
# S = X + 2*X**2/3 - 4*X**3/8 + 8*X**2/23 - 14*X**3/68 + 22*X**2/203 + ...
#

x = int(input("X?"))

s     = x
a     = 2
b     = 2
c     = 3
sinal = 1
inc   = 2
print(a,'X^',b,"/",c)

for i in range(1,30):
    s = s + (sinal * (a*(x**b))/(c*1.0))
    
    a     = a + inc
    inc   = inc + 2

    if (b==2):
      b=3
    else:
      b=2
    c     = (3*c) - 1 
    sinal = sinal * -1
    print(a,'X^',b,"/",c)
    
print("s=",s)

