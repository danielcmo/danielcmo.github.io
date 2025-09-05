n_max = 35 # numero de alunos maximo
n_p   = 4  # numero de provas
n_al  = 0  # numero de alunos cadastrados

# cria vetor nomes dos alunos e matriz de notas
nomes = [' ']*n_max
notas = []
for i in range(n_max):
  linha = [0.0]*n_p
  notas.append(linha)

# cria vetores de nomes e medias para ordenacao
nomed  = [' ']*n_max
medias = [0.0]*n_max

# -------------------------------- rotina de inserir aluno e notas
def in_aluno_notas():
  global n_al
  
  nomes[n_al]    =input("Nome do Aluno: ")
  notas[n_al][0] =float(input("Nota1: "))
  notas[n_al][1] =float(input("Nota2: "))
  notas[n_al][2] =float(input("Nota3: "))
  notas[n_al][3] =float(input("Nota4: "))
  
  n_al = n_al + 1

# --------------------------------- rotina para alterar nome do aluno
def al_nome():
  nome = input("Nome do Aluno: ")
  
  #procura indice do aluno
  achou=False
  for i in range(n_al):
    if (nome==nomes[i]):
      nome2    = input("Novo nome: ")
      nomes[i] = nome2
      print("aluno de indice ",i," mudou nome de ",nome," para ",nome2)
      achou=True
      break

  if (not achou):
    print("Aluno nao cadastrado")    

# --------------------------------- rotina para alterar notas
def al_nota():
  nome = input("Nome do Aluno: ")
  
  #procura indice do aluno
  achou=False
  for i in range(n_al):
    if (nome==nomes[i]):
      prova= int(input("Qual nota alterar (1,2,3 ou 4): "))
      nota = float(input("Nota: "))

      notas[i][prova-1] = nota
      print("aluno de indice ",i," nota ",prova," valor ",nota)
      achou=True
      break

  if (not achou):
    print("Aluno nao cadastrado")    

# ---------------------------------- rotina para remover aluno
def re_aluno():
  global n_al

  nome = input("Nome do Aluno: ")
  
  #procura indice do aluno
  achou=False
  for i in range(n_al):
    if (nome==nomes[i]):

      # faz um "shift" dos alunos da posicao i+1 para a i
      for j in range(i,n_al-1):    
        nomes[i]    = nomes[i+1]
        notas[i][0] = notas[i+1][0] 
        notas[i][1] = notas[i+1][1] 
        notas[i][2] = notas[i+1][2] 
        notas[i][3] = notas[i+1][3] 

      n_al = n_al-1
      achou=True
      break

  if (not achou):
    print("Aluno nao cadastrado")    

# -------------------------------- rotina de imprimir relatorio das medias ordenadas
def print_med_ord():

  # preenche vetores de nomes e medias
  for i in range(n_al):
    nomed[i]  = nomes[i]
    medias[i] = (notas[i][0]+notas[i][1]+notas[i][2]+notas[i][3])/4.0

  # ordena
  for i in range(n_al):
    for j in range(n_al-1):
      if (medias[j] > medias[j+1]):
        t           = medias[j]
        medias[j]   = medias[j+1]
        medias[j+1] = t

        n           = nomed[j]
        nomed[j]    = nomed[j+1]
        nomed[j+1]  = n

  # imprime relatorio
  for i in range(n_al):
    print(nomed[i],":\t", medias[i])


# --------------------------------- rotina de imprimir relatorio nomes/notas
def print_rel():
  for i in range(n_al):
    print(nomes[i],":\t\t", notas[i][0],notas[i][1], notas[i][2], notas[i][3])

# ---------------------------------- rotina para gravar relatorio nomes/notas
def save_rel():
  arq=open('relatorio.txt','w')
  for i in range(n_al):
    arq.write(nomes[i]+":\t"+str(notas[i][0])+" "+str(notas[i][1])+" "+str(notas[i][2])+" "+str(notas[i][3])+"\n")
  arq.close()

op=0
while (op != 8):
  print('')
  print("-- Menu --")
  print("1) Inserir Nome aluno/Notas")
  print("2) Alterar Nome aluno")
  print("3) Alterar Nota")
  print("4) Remover Aluno")
  print("5) Imprimir relatorio de medias ordenadas")
  print("6) Imprimir relatorio Completo")
  print("7) Gravar relatorio Completo")
  print("8) Sair")
  op = int(input("opc:"))
  print('')

  if (op == 1):
    in_aluno_notas()
  elif (op == 2):
    al_nome()  
  elif (op == 3):
    al_nota()
  elif (op == 4):
    re_aluno()
  elif (op == 5):
    print_med_ord()
  elif (op == 6):
    print_rel()
  elif (op == 7):
    save_rel()  
    
   

