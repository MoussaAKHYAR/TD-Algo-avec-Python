import math
"""
Exercice 8 :
Ecrire un algorithme permettant de résoudre une équation du second degré.
Ax2 + bx + c = 0
"""
print("Résouudre une équation du second degré Ax2 + bx + c = 0 ")
a = float(input("entrer la valeur de A "))
b = float(input("entrer la valeur de b "))
c = float(input("entrer la valeur de c "))
while(a==0):
  print("la valeur de A doit etre different de 0")
  a = float(input("entrer la valeur de A"))

d = b*b-(4*a*c)
if(d > 0):
  x1 = float((-b-(math.sqrt(d)))/2*a)
  x2 = float((-b+(math.sqrt(d)))/2*a)
  print("les solutions de l'equation est : X1 = {} et X2 = {} ".format(x1,x2))
if(d == 0):
  x1 = float(-b/2*a)
  print("la solution est : x1 = ",x1)
if(d < 0):
  print("il n'y a pas de solution !!!!!!!!!")



