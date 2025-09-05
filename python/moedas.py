# Faça um programa que, a partir de um valor informado em centavos, indique a menor quantidade de moedas que representa esse valor. Considere moedas de 1,5,10,25 e 50 centavos e 1 real.

x=(int(input()))
a=(x//100)
s=(x%100)
print(a,"x 1 real")

if (s != 0):
  b=(s//50)
  s=(s%50)
  print(b,"x 50cc")

  if (s != 0):
    c=(s//25)
    s=(s%25)
    print(c,"x 25cc")

    if (s != 0):
      d=(s//10)
      s=(s%10)
      print(d,"x 10cc")

      if (s != 0):
        e=(s//5)
        s=(s%5)
        print(e,"x 5cc")

        if (s != 0):
          f=s
          print(f,"x 1cc")



