np1=10
np2=5
cont=0
p1=[0]*np1
p2=[0]*np2
print("PROG1")
for i in range(np1):
    p1[i]=(int(input("mat. "+str(i)+") ")))
print("PROG2")
for i in range(np2):
    p2[i]=(int(input("mat. "+str(i)+") ")))    
    
for i in range(np1):
    for j in range(np2):
        if (p1[i]==p2[j]):
            print("Aluno ",p1[i]," irregular")
            cont=cont+1
            
print("total =",cont)
