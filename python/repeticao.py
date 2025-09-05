n        =10
v        =[0]*n

max_cont =0
max_pos1 =-1

for i in range(n):
    print("num",i,")")
    v[i]=int(input())

for i in range(n):
    cont =0

    for j in range(n):
          if (v[i]==v[j]):
              cont=cont+1

    if (max_cont<cont):
          max_cont =cont
          max_pos1 =i

print("numero ",v[max_pos1], "aparece primeiro em ",max_pos1," e ",max_cont," vezes")
