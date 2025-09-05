fvotos = open('votos.txt', 'r')

votos_Bart = 0
votos_Homer = 0
votos_Krusty = 0
votos_MrBurns = 0
votos_NedFlanders = 0
votos_nulos = 0

for voto in fvotos:
  voto = int(voto)
  if voto == 1:
    votos_Bart = votos_Bart + 1
  if voto == 2:
    votos_Homer = votos_Homer + 1
  if voto == 3:
    votos_Krusty = votos_Krusty + 1
  if voto == 4:
    votos_MrBurns = votos_MrBurns + 1
  if voto == 5:
    votos_NedFlanders = votos_NedFlanders + 1
  if voto < 1 or voto > 5:
    votos_nulos = votos_nulos + 1
    
max_votos = votos_Bart
mais_votado = "Bart"

if votos_Homer > max_votos:
  max_votos = votos_Homer
  mais_votado = "Homer"
if votos_Krusty > max_votos:
  max_votos = votos_Krusty
  mais_votado = "Krusty"
if votos_MrBurns > max_votos:
  max_votos = votos_MrBurns
  mais_votado = "Mr Burns"
if votos_NedFlanders > max_votos:
  max_votos = votos_NedFlanders
  mais_votado = "Ned Flanders"
  
min_votos = votos_Bart
menos_votado = 1
if votos_Homer < min_votos:
  min_votos = votos_Homer
  menos_votado = 2
if votos_Krusty < min_votos:
  min_votos = votos_Krusty
  menos_votado = 3
if votos_MrBurns < min_votos:
  min_votos = votos_MrBurns
  menos_votado = 4
if votos_NedFlanders < min_votos:
  min_votos = votos_NedFlanders
  menos_votado = 5
  
print(mais_votado," eleito com ",str(max_votos)," votos!")
print("Candidato ",menos_votado," foi o menos votado com ",str(min_votos)," voto(s)!")
print(str(votos_nulos)," pessoas votaram nulo!")
