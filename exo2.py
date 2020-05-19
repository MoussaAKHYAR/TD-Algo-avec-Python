import math
"""
Exercice 2
Ecrire un programme qui demande à l’utilisateur de donner le rayon d’un cercle et lui retourne sa surface et son périmètre.
PI =  4 * arc tangeante de 1. la fonction arc tangeante est atan ex : atan(2).
"""
rayon = float(input("entrer le rayon du cercle"))
s = rayon*rayon*4*math.atan(1)
p = 2*rayon*4*math.atan(1)
print("la surface du cercle est ",s)
print("le perimetre du cercle est ",p)
