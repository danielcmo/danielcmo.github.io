c3  = 0
tot = 0.0
for i in range(1,11,1):
    sal  = float(input("salario?"))
    cla  = int(input("classe?"))
    sal2 = 0.0
    nome = ""
    
    if (cla==1):
        sal2 = 2*sal
        nome = "bom"
    
    if (cla==2):
        sal2 = sal + sal/2
        nome = "medio"
        
    if (cla==3):
        sal2 = sal
        c3 = c3+1
        nome = "tsk tsk"
        
    tot = tot + sal2
    print("salario=", sal2," classe=",nome)

print("classe3=",c3," total=",tot)

