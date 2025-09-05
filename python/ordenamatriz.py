# Dada uma matriz A(nxm) fornecida pelo usuario, ordene 
# cada uma das linhas da matriz em ordem crescende

M=[]
n=int(input())
m=int(input())

for i in range(n):
	l=[]
	for j in range(m):
		l.append(int(input()))
	M.append(l)

for i in range(n):
	for k in range(m):
		for j in range(m-1):
			if (M[i][j] > M[i][j+1]):
				temp      = M[i][j]
				M[i][j]   = M[i][j+1]
				M[i][j+1] = temp

for i in range(n):
	print(M[i])


