# Implemente um programa que leia um arquivo texto (“ips.txt”) contendo uma lista de endereços IP e gere dois outros arquivos (“v.txt” e “i.txt”), 
# um contendo os endereços IP validos e outro contendo os enderecos invalidos. O formato de um endereco IP eh NUM1.NUM.NUM.NUM, 
# onde NUM1 vai de 1 a 255 e NUM vai de 0 a 255.


arq1=open('ips.txt','r')
arq2=open('v.txt','w')
arq3=open('i.txt','w')

for l1 in arq1:
    n1,n2,n3,n4 = l1.split(".")
    print(n1,n2,n3,n4)

    if (int(n1)<=255 and int(n1)>=0) and (int(n2)<=255 and int(n2)>=1) and (int(n3)<=255 and int(n3)>=1) and (int(n4)<=255 and int(n4)>=1):
        arq2.write(l1)
    else:
       arq3.write(l1) 


    
arq1.close()
arq2.close()
arq3.close()
