import math
"""
Exercice 6 :
Faire un programme qui saisit  les coordonnées de 2 points A (x1, y1) et b(x2, y2) et qui affiche la distance entre les 2 points.
Formule : distante = racine carrée de ((x1 – x2)2  + (y1 – y2)2)
Racine carrée : sqrt. Ex : sqrt(7) ; <math.h>

"""
print("entrer les coordonées du point A (x1,y1)")
x1 = int(input())
y1 = int(input())

print("entrer les coordonées du point B (x2,y2)")
x2 = int(input())
y2 = int(input())

d = math.fabs(((x1 - x2)*2 + (y1 - y2)*2))
print("la distance entre le point A et B est : {} ".format(math.sqrt(d)))


