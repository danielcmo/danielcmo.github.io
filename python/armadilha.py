import random

#tamanho do tabuleiro
nt=20
#numero de atalhos e armadilhas
na=5
#amplitude de atalhos e armadilhas (quanto pode andar)
ap=2
#faces do dado
nd=3


v        =[0]*(nt+1)
t        =['x']*(nt+1) 

#--- gera tabuleiro (inteiro) ---

#atalho
i=0
while (i<na):
    p   = random.randint(1,nt)
    if (v[p]==0):
        v[p]= random.randint(1,ap)
        i=i+1
        
#armadilha
i=0
while (i<na):
    p   = random.randint(1,nt)
    if (v[p]==0):
        v[p]= -random.randint(1,ap)
        i=i+1

#--- gera tabuleiro (string) ---
for i in range(1,nt+1):
    if (v[i]==0):
        t[i]="x"
    if (v[i]>0):
        t[i]="+"+str(v[i])
    if (v[i]<0):
        t[i]=str(v[i])
t[0]='J12'
print(t)    
    
vitoria = False
rodada  = 0
j1      = 0
j2      = 0

while (not vitoria):
    dado = random.randint(1,nd)
    
    #jogador 1
    if (rodada%2==0):
        #vitoria
        if (j1+dado>=nt):
            print("VITORIA DO JOGADOR 1")
            vitoria = True
        else:
            print("Jogador 1 tirou ",dado)
            
            # armadilha ou atalho               
            if (v[j1+dado]!=0):
                dado=dado+v[j1+dado]
            
            #origem
            if (t[j1]=='J12'):
                t[j1]     = "J2"
            else:
                if (v[j1]==0):
                    t[j1]="x"
                if (v[j1]>0):
                    t[j1]="+"+str(v[j1])
                if (v[j1]<0):
                    t[j1]=str(v[j1])
                
            #destino    
            if (t[j1+dado]=='J2'):
                t[j1+dado]= 'J12'
            else:
                t[j1+dado]= "J1"
                
            j1 = j1+dado
            
    #jogador 2
    else:
        #vitoria
        if (j2+dado>=nt):
            print("VITORIA DO JOGADOR 2")
            vitoria = True
        else:
            print("Jogador 2 tirou ",dado)
            
            # armadilha ou atalho
            if (v[j2+dado]!=0):                           
                dado=dado+v[j2+dado]
            
            #origem
            if (t[j2]=='J12'):
                t[j2]     = "J1"
            else:
                if (v[j2]==0):
                    t[j2]="x"
                if (v[j2]>0):
                    t[j2]="+"+str(v[j2])
                if (v[j2]<0):
                    t[j2]=str(v[j2])
                
            #destino    
            if (t[j2+dado]=='J1'):
                t[j2+dado]= 'J12'
            else:
                t[j2+dado]= "J2"
                
            j2 = j2+dado
            
    #impressao do tabuleiro
    print(t,"\n")
    rodada = rodada+1
