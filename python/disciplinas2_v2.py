
np1=10
np2=5
np3=7
cont=0
p1=[0]*np1
p2=[0]*np2
p3=[0]*np3
print("PROG1")
for i in range(np1):
    print("mat. ",i,")")
    p1[i]=int(input())
print("PROG2")
for i in range(np2):
    print("mat. ",i,")")
    p2[i]=int(input())
print("PROG3")    
for i in range(np3):
    print("mat. ",i,")")
    p3[i]=int(input())

for i in range(np1):
    achou=False
    for j in range(np2):
        if (p1[i]==p2[j]):
            achou=True

    if (achou):       
      for k in range(np3):
        if (p1[i]==p3[k]):
          print("Aluno ",p1[i]," irregular")
          cont=cont+1

print("total =",cont)

