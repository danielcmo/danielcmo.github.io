#Um professor armazena em um arquivo texto "classe.txt" o numero e o nome de cada aluno da turma da disciplina sob sua responsabilidade.
#Por questao de seguranca, ele prefere armazenar as notas obtidas pelos alunos em cada prova em um outro arquivo texto (avalia.txt), onde cada
#linha contem o numero do aluno e os valores das notas de 4 provas. Escreva um programa que permita consultar as notas de cada aluno a partir
#do seu nome. Seu programa deve receber o nome como entrada e buscar e imprimir a linha correspondente ao nome no
#arquivo "avalia.txt".

aluno = input('Digite o nome do aluno: ')

# cria objeto de leitura do arquivo classe.txt
fclasse = open('classe.txt', 'r')

id_aluno = -1

for linha in fclasse: # varre linhas de classe.txt
  linha = linha.split() # separa linha em lista de strings
  if linha[1] == aluno:
    id_aluno = int(linha[0]) # salva id do aluno 
    break

fclasse.close() # encerra conexao com o arquivo

if id_aluno == -1:
        print("Aluno inexistente!")
else:
  # cria objeto de leitura do arquivo notas.txt
  fnotas = open('avalia.txt', 'r')

  for linha in fnotas: # varre linhas de notas.txt
    linha_str = linha.split()
    if int(linha_str[0]) == id_aluno: # se for a linha desejada
      media = (float(linha_str[1])+float(linha_str[2])+float(linha_str[3])+float(linha_str[4]))/4
      print('notas = ',linha_str[1],linha_str[2],linha_str[3],linha_str[4])
      print('media = ',media)
      break

  fnotas.close()                        


