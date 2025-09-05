x=int(input("n?"))
t1=2
t2=5
t3=8
for i in range (0,x):
  if (i==0):
    print("2")
  if (i==1):
    print("5")
  if (i==2):
    print("8")
    
  if (i>2):
    t4=(t3-(t1+t2)) 
    t1=t2
    t2=t3
    t3=t4
    print(t3)
