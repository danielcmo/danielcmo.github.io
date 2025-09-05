# Implemente um programa que abre 1 arquivo (notas.txt). Este arquivo contem as notas dos alunos, 
# cada linha corresponde a uma ou mais notas do aluno (separado por espacos),
# Leia o arquivo e gere um segundo (medias.txt)
# que armazene a media de cada aluno.

arq1=open('notas.txt','r')
arq2=open('medias.txt','w')

l1 =arq1.readline()

while (l1 != ""):

        m   =0.0
        cont=0
        for n in l1.split(" "):
            m = m+float(n)
            cont=cont+1

        arq2.write(str(m/cont)+"\n")

        l1 =arq1.readline()

arq1.close()
arq2.close()

