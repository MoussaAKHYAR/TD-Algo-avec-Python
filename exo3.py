"""
Exercice 3 :
    Version 1 :
    Faire un programme qui saisit 3 résistances : R1, R2 et R3.
    Calculer et afficher la résistance en série : R1 + R2 +R3
    Calculer et afficher la résistance en parallèle : (R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)
    Version 2 :
    Demander a l’utilisateur d’indiquer son choix.
    S’il entre la valeur  1, calculer et afficher la fréquence en série.
    S’il entre la valeur 2, calculer et afficher la fréquence en parallèle.
"""
#Premiere methode
"""
r1 = float(input("saisir la résistence R1"))
r2 = float(input("saisir la résistence R2"))
r3 = float(input("saisir la résistence R3"))
while (r3 == 0):
  r3 = float(input("saisir la résistence R3"))
rs = (r1+r2+r3)
rp = (r1*r2*r3)/(r1*r2 + r2*r3 + r1*r3)
print("la résistence en série est {}".format(rs))
print("la résistence en paralléle est {}".format(rp))
"""

#Deuxieme methode
r1 = float(input("saisir la résistence R1"))
r2 = float(input("saisir la résistence R2"))
r3 = float(input("saisir la résistence R3"))
while (r3 == 0):
  r3 = float(input("saisir la résistence R3"))
print("tapez 1 si vous voulez calculer la résistence en série")
print("tapez 2 si vous voulez calculer la résistence en paralléle")
choix = int(input())
if(choix == 1):
  rs = (r1+r2+r3)
  print("la résistence en série est {}".format(rs))
elif(choix == 2):
  rp = (r1*r2*r3)/(r1*r2 + r2*r3 + r1*r3)
  print("la résistence en paralléle est {}".format(rp))
else:
  print("Choix invalide")









