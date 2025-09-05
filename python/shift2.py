n        =10
v        =[0]*n

for i in range(n):
    v[i]=(int(input("num. "+str(i))))
print(v)

fim=n
for i in range(fim):
	# identifica 13
	teste    =True    
    
	while (v[i] == 13) and (teste):
        	teste=False
        
        	# shift do 13 para o fim
        	for j in range(i,fim-1):
           		v[j]=v[j+1]
            
            		if (v[j]!=13):
                		teste=True
                
        	v[fim-1]=13
		fim=fim-1


	if (i>=fim):
		break



print(v)
