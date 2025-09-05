for i in range(1,1000,1):
    if (i%2==0):
        s=0
        for j in range(0,i-3,1):
            s=j*(j+1)*(j+2)
            if (s==i):
		print(i,"triangular (",j,j+1,j+2,")")


