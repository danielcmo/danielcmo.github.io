from mip import *

# cria modelo
model = Model(name="exemplo3",sense=MAXIMIZE, solver_name=CBC)

# le arquivo .lp
model.read('ex3.lp')
print('modelo tem', model.num_cols, 'variaveis')
print('e ', model.num_rows, ' restrições')

# otimiza
status = model.optimize()
print("\n",status)

# valores das variaveis
variaveis = model.vars

for i in range(len(variaveis)):
    print(variaveis[i].x)

# saida
print("sol = ", model.objective_value)