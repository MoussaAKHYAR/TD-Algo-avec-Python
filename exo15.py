n = int(input("Entrer le nombre de départ"))
som = 0
for i in range (1,int(n+1)):
  som = som + i
  print(i)
print("la somme des valeurs comprises entre 1 et ",n," est : ",som)
for i in range (1,n):
  som = som + i
moy = som/n
print("la moyenne est : ",moy)