import math
"""
Exercice 4
    Ecrire un programme qui saisit un réel x et un entier n et affiche x à la puissance n.
    Version 1 : utiliser la fonction pow  du fichier d’en-tête <math.h>  ex : pow(x,n)
    Version 2 : en utilisant un boucle
"""
nombre = float(input("saisir un nombre "))
n = float(input("entrer la puissance "))
print("{} puissance {} est {} : ".format(nombre,n,math.pow(nombre,n)))
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")
i = 1
res = 1
while(i <= nombre):
  res = res * nombre
  i += 1
print("{} puissance {} est {} : ".format(nombre,n,res))
