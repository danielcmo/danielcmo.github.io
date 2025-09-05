denovo = 1

while denovo==1 :
    inf = 0
    sup = 100
    med = 50
    c   = 1

    print("numero eh ", med, "? (0-menor 1-acertou 2-maior)")
    resp = int(input())
    while resp != 1:
        c = c + 1
        if resp == 0:
            inf = med + 1
        else:
            if resp == 2:
                sup = med - 1
            
        med = (inf + sup) // 2
        print("numero eh ", med, "? (0-menor 1-acertou 2-maior)")
        resp = int(input())
    
    print ("ACERTEI em " , c , "tentativas")
    
    denovo = int(input("de novo? 1-Sim 2-Nao"))

