"""
Exercice 10 : Ecrire un algorithme qui lit trois valeurs entières ( A, B et C)
et qui permet de les trier par échanges successifs Et enfin les afficher dans l'ordre 4.
"""

""""
i = 1
tab = range(3)
print(len(tab))

while(i <= 3):
  val = int(input("entrer une valeur"))
  tab = [].insert(i,val)
  i += 1
for nombre in tab:
  print(nombre)
"""
taille = int(input("entrer la taille du tableau"))
tab = []
for i in range(0,taille):
  print("entrer la valeur "+str(i + 1)+" : ")
  tab = int(input())

for j in tab:
  print(tab[j])

