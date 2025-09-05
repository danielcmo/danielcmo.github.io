# primeiro numero
for i in range(1000,1499,1):

	# soma do divisores do primeiro numero
	s1= 0
        for k in range(1,i-1,1):
		if (i%k==0):
			s1=s1+k

	# segundo numero
	for j in range(i+1,1500,1):

		# soma dos divisores do  segundo numero
		s2= 0
		for k in range(1,j-1,1):
			if (j%k==0):
				s2=s2+k
        
		# checagem
		if ((s1==j) and (s2==i)):
			print(i," e ",j," sao amiguxos!")
