n = int(input("entrer la valeur de N "))
while(n < 10 or n >50):
  n = int(input("entrer la valeur de N "))
tab = []
pos = 0
seq = 0
longueur = 1
for i in range (n):
  val = 0
  while(val <= 0 or val > 100):
    val = int(input("entrer une valeur à la cellule "+str(i)+" ::"))
  tab.append(val)
i = 0
while(i < n-1):
  if(tab[i]<tab[i+1]):
    seq += 1
    if(seq > longueur):
      longueur = seq
      pos = (i + 1) - longueur + 1
  else:
    seq = 1
  i += 1
print("la plus longue séquence est : ",longueur," qui commence à la position ",pos)
