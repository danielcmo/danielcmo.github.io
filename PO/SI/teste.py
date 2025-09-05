from mip import *

############################ ENTRADAS DO ARQUIVO #######################

arq  = open("TPI_COL_1.txt", "r")
line = arq.readline().strip().split()
n, m, F = map(int, line[2:])

#conj. de arestas
E = []

# Obtendo arestas
for _ in range(m):
    line = arq.readline().strip().split()
    i, j =  map(int, line[1:])
    E.append((i, j)) 

############################################################################

# CRIA MODELO
model = Model(name="Coloração", sense=MINIMIZE, solver_name=CBC)

#CRIANDO VARIÁVEIS
x = [[model.add_var(name=f"x_{i+1}_{j+1}", var_type=BINARY) for j in range(F)] for i in range(n)]
w = [model.add_var(name=f"w_{j+1}", var_type=BINARY) for j in range(F)]

#CRIANDO RESTRIÇÕES:

#i só tem uma cor
for i in range(n):
    exp = 0
    for j in range(F):
        exp += x[i][j]
    model.add_constr(exp == 1, name=f"v_{i+1}")


#vizinhos não podem ter a mesma cor
for j in range(F):
    for i, k in E:
        model.add_constr(x[i - 1][j] + x[k - 1][j] <= 1, name=f"v_{i}_e_{k}_usa_{j+1}")
        
# cor usada
for i in range(n):
    for j in range(F):
        model.add_constr(x[i][j] <= w[j], name=f"v_{i+1}_usa_{j+1}")

#FUNÇÃO OBJETIVO

func = 0
for j in range(F):
    func += w[j]

model.objective = minimize(func)

# escreve modelo
model.write("modelo.lp")

model.optimize()

print("\n\nSolução: ", model.objective_value)

# valores das variaveis
variaveis = model.vars

for i in range(len(variaveis)):
    if (variaveis[i].x > 0.0001):
        print(variaveis[i].name," = ",variaveis[i].x)
