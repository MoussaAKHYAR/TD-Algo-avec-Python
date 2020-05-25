"""
Exercice 9 : Ecrire un algorithme qui donne la durée de vol en heure minute connaissant l'heure de départ et l'heure d'arrivée.
a. On considère que le départ et l'arrivé ont lieu le même jour
b. On suppose que la durée de vol est inférieure à 24 heures mais peut avoir lieu le lendemain.
"""
hd = int(input("entrer l'heure de départ "))
md = int(input("entrer minute de départ "))
while(not (0 < hd < 24) or not (0 <md < 60)):
  hd = int(input("entrer l'heure de départ "))
  md = int(input("entrer minute de départ "))

ha = int(input("entrer l'heure d'arrivée "))
ma = int(input("entrer minute d'arrivée "))
while(not (0 < hd < 24) or not (0 <md < 60)):
  ha = int(input("entrer l'heure d'arrivée "))
  ma = int(input("entrer minute d'arrivée "))

if(hd <= ha):
  hg = ((ha * 60 + ma ) - ( hd * 60 + md))
  hda =int(hg/60)
  mda = hg%60
  print("la durée du vol est {}H {}mm ".format(hda,mda))
else:
  hg = 1440 - (((hd * 60 + md ) - ( ha * 60 + ma)))
  hda =int(hg/60)
  mda = hg%60
  print("la durée du vol est {}H {}mm ".format(hda,mda))

