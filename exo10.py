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

taille = int(input("entrer la taille du tableau"))
tab = []
for i in range(0,taille):
  print("entrer la valeur "+str(i + 1)+" : ")
  tab = int(input())

for j in tab:
  print(tab[j])
"""
a = int(input("Entrer A :"))
b = int(input("Entrer B  :"))
c = int(input("Entrer C  :"))
A=[a,b,c]
print(A)
for i in range(0,len(A)-1):
  for j in range(1,len(A)):
    if A[i]>A[j]:
      e=A[i]
      A[i]=A[j]
      A[j]=e
print("les valeurs de A,B et C sont dans l’ordre:")
for i in range(len(A)):
  print(A[i])
print(A)

