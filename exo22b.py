N = 0
while(N <= 0 or N >50):
  N =int(input("Donner le nombre de cellule du tableau ::"))

tab = []
for i in range(N):
  val = 0
  while(val <= 0 or val >100):
    val = int(input("Cellule "+str(i)+" ::"))

  tab.append(val)
posD = 0
taille = 1
maxlong = 1
i = 0
while (i < N-1):
  if(tab[i] < tab[i+1]):
    taille += 1
  else:
    if(maxlong < taille ):
      maxlong = taille
      posD = i - taille + 1
    taille = 1

  i = i + 1
taille = maxlong + posD

print("La plus longue séquence est :: \n")
i = posD
while(i < taille):
  print(tab[i] , " * ",end="")
  i += 1

print("\nElle debute a la position ",posD, " et elle a une longueur de ",maxlong," cellule .")