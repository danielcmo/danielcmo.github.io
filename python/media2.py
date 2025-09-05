# Implemente um programa que abre 2 arquivos (nomes.txt e notas.txt). O primeiro arquivo contem nomes de
# alunos e o segundo arquivo contem as notas dos alunos.  No primeiro arquivo, cada linha corresponde ao nome
# de um aluno e no segundo arquivo,   cada   linha   corresponde   a uma ou mais notas do aluno (separado por espacos),
# os dois arquivos tem o mesmo numero de linhas.  Leia   os   dois arquivos e gere um terceiro (medias.txt)
# que armazene o nome e a media de cada aluno.

# *** OBS ***
# Para evitar problemas de quebras de linha "\n", podemos usar a funcao "strip" da string para retirar qualquer 
# caractere indesejado da string
# ***********

arq1=open('nomes.txt','r')
arq2=open('notas.txt','r')
arq3=open('medias.txt','w')

l1 =arq1.readline()
l2 =arq2.readline()

while (l1 != ""):

        m   =0.0
        cont=0
        for n in l2.split(" "):
            m = m+float(n)
            cont=cont+1

        n=l1.strip("\n")
        arq3.write(n+" "+str(m/cont)+"\n")

        l1 =arq1.readline()
        l2 =arq2.readline()


arq1.close()
arq2.close()
arq3.close()
