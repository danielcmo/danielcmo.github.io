# A coordenacao do curso de computacao deseja saber quantos alunos estao cursando ( de forma irregular )
# as disciplinas de PROG1 e PROG2 ao mesmo tempo. Faca um programa que (i) leia as matriculas (inteiro)
# dos 30 alunos de PROG1 e dos 40 alunos de PROG2, (ii) imprima as matriculas dos alunos irregulares e
# (iii) imprima no fim a quantidade de alunos irregulares

np1=30
np2=40
cont=0
p1=[0]*np1
p2=[0]*np2
for i in range(np1):
    p1[i]=(int(input("mat. "+str(i))))
for i in range(np2):
    p2[i]=(int(input("mat. "+str(i))))    
    
for i in range(np1):
    for j in range(np2):
        if (p1[i]==p2[j]):
            print("Aluno ",p1[i]," irregular")
            cont=cont+1
