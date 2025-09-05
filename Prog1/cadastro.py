n_max = 4 # numero de alunos maximo
n_p   = 4  # numero de provas

# numero de alunos cadastrados. Este valor começa com 0, mas a medida que você
# for cadastrando alunos, esse valor vai aumentando
n_al  = 0  

# cria vetor nomes dos alunos e matriz de notas
nomes = [' ']*n_max
notas = []
for i in range(n_max):
  linha = [0.0]*n_p
  notas.append(linha)

print(nomes)
print()
for i in range(n_max):
    print(notas[i])

# função de imprimir menu
def menu():
    print('')
    print("-- Menu --")
    print("1) Inserir Nome aluno/Notas")
    print("6) Imprimir relatório Completo")
    print("7) Sair")

op=0
while (op != 7):
  menu()
  op = int(input("opc:"))
  
  #if (op == 1):
  #  in_aluno_notas()
  #elif (op == 6):
  #  al_nome()  

  
   

