n = int(input("n?"))        
v =[0]*(n)

for i in range(n):
    v[i]=(int(input("num. "+str(i))))

for i in range(n):
    for j in range(n-1):
        if (v[j]>v[j+1]):
            t      = v[j]
            v[j]   = v[j+1]
            v[j+1] = t
print(v)

resp=True
while (resp):
  num = int(input("numero a ser procurado?"))
  e,d,achou = 0,len(v)-1,False

  while (e <= d):
    m = (e+d)//2
    if (num == v[m]):
      achou=True
      break
    else:
      if (num > v[m]):
        e=m+1
      else:
        d=m-1

  if (achou):
    print("numero ",num," na posicao ",m)
  else:
    print(-1)

  x=int(input("Quer procurar outro numero? 1-Sim, 0-Nao"))
  if (x==1):
    resp = True
  else:
    resp = False
