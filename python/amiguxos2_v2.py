# primeiro numero
for i in range(1000,1499,1):

  # soma dos divisores do primeiro numero
  s1= 0
  for k in range(1,i-1,1):
	  if (i%k==0):
		  s1=s1+k
  
  # soma dos dividores do numero gerado s1
  s2=0
  for k in range(1,s1-1,1):
      if (s1%k==0):
        s2=s2+k
                  # impede numeros repetidos 
  if (s2==i) and (s1 > i):
    print(i," e ",s1," sao amiguxos!")
