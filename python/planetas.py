# Para uma possivel futura viagem espacial, foram coletados e escritos em um arquivo texto os dados de varias pessoas.
# Nesse arquivo cada linha contem o primeiro nome da pessoa, seu ultimo nome, seu ano de nascimento, seu peso na Terra
# e seu desejo de ir para Marte ou para Jupiter. Por exemplo, uma linha no arquivo seria: 
#    Maria Pacheco, 1965, 89, Marte
# Implemente um metodo para ler os dados do arquivo texto e criar dois novos arquivos: o primeiro contendo o nome das
# pessoas com menos de 30 anos que desejam ir para Marte e o peso da pessoa em Marte; o segundo contendo o nome das
# pessoas com menos de 40 anos que desejam ir para Jupiter e o peso da pessoa em Jupiter. Sabe-se que uma pessoa com
# peso 100 na Terra, pesa 38 em Marte e 264 em Jupiter. Para testar seu programa, voce deve criar um arquivo texto
# no formato especificado no primeiro paragrafo.

# *** OBS ***
# Para evitar problemas de quebras de linha "\n", podemos usar a funcao "strip" da string para retirar qualquer 
# caractere indesejado da string
# ***********

arq1=open('planetas.txt','r')
arq2=open('j.txt','w')
arq3=open('m.txt','w')

for l1 in arq1:
	n1,n2,n3,n4 = l1.split(",")

	if (n4.strip('\n')=="Marte") and (2017-int(n2)<30):
		arq3.write(n1+" "+str(float(n3)*0.38)+"\n")

	if (n4.strip('\n')=="Jupiter") and (2017-int(n2)<40):
		arq2.write(n1+" "+str(float(n3)*2.64)+"\n")

arq1.close()
arq2.close()
arq3.close()
