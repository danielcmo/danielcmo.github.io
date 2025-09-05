%Exercicio: Implemente um campo minado de dimensoes nxn. Voce pode representar o campo como uma matriz nxn. Nao se esqueca de:
%- gerar o campo aleatoriamente com n bombas espalhadas. O valor da posicao equivale ao numero de bombas adjacentes (0-8).
%DICA 1) Voce pode representar a bomba com valor 9 por exemplo
%- proibir jogadas irregulares (espacos ja descobertos ou fora do campo).
%- imprimir o campo a cada jogada
%DICA 2) Se precisar imprimir um valor X sem quebrar a linha, voce pode usar print(X,end='')
%- testar as condicoes de derrota (se escolher a bomba, morre)
%DICA 3) Mantenha uma matriz auxiliar nxn para saber quais posicoes estao visiveis e quais nao estao

import random

n=int(input("tamanho do campo?"))

# campo
campo = []
for x in range (n) :
    campo.append(["X"]*n)
    
# minas
minas = []
for x in range (n) :
    minas.append([0]*n)

# coloca minas aleatorias. Minas são marcadas com valor 9
num_minas = n
while (num_minas > 0):
    i = random.randint(0,n-1)
    j = random.randint(0,n-1)
    
    if (minas[i][j]==0):
        minas[i][j]=9
        
        if (i-1>0):
            if (minas[i-1][j] != 9):
                minas[i-1][j]=minas[i-1][j]+1
                
        if (i+1<n):
            if (minas[i+1][j]!=9):
                minas[i+1][j]=minas[i+1][j]+1   
        
        if (j-1>0):
            if minas[i][j-1]!=9:
                minas[i][j-1]=minas[i][j-1]+1
            if (i-1>0):
                if (minas[i-1][j-1]!=9):
                    minas[i-1][j-1]=minas[i-1][j-1]+1
            if (i+1<n):
                if (minas[i+1][j-1]!=9):
                    minas[i+1][j-1]=minas[i+1][j-1]+1
                    
        if (j+1<n):
            if minas[i][j+1]!=9:
                minas[i][j+1]=minas[i][j+1]+1
            if (i-1>0):
                if (minas[i-1][j+1]!=9):
                    minas[i-1][j+1]=minas[i-1][j+1]+1
            if (i+1<n):
                if (minas[i+1][j+1]!=9):
                    minas[i+1][j+1]=minas[i+1][j+1]+1
            
        num_minas=num_minas-1
    
# rotulos
rotulos=[]
for x in range (n) :
    rotulos.append(str(x))

terminou = False
while not terminou :
    
    #------ imprime campo ------
    print("      ",end='')
    for i in range(n):
        print("",i,"",end='')
    print("\n")
    for i in range(n):
        print(i,")   ",end='')
        for j in range(n):
            if (campo[i][j]=="X"):
                print(" X ",end='')
            else:
                print("",str(minas[i][j]),"",end='')
        print("\n")    

    print("informe posicao da jogada (x,y)")
    x=int(input("x?"))
    y=int(input("y?"))
    
    if (x<0 or x>=n or y<0 or y>=n or campo[x][y]=="O"):
        print("*********** jogada invalida ***********")
        continue
    campo[x][y]="O" 
    
    if (minas[x][y]==9):
        print("BUMMMMMM !","\nVoce Perdeu")
        break
    
# imprime minas 
for i in range(n):
    print(minas[i])
