"""
Exercice 5
Ecrire un programme qui saisit 5 variables de type entier au clavier et qui affiche leur somme.
Utiliser une boucle (for ou while ou do..while).
"""
i = 1
som = 0
while(i <= 5):
  val = int(input("entrer une valeur "))
  som = som + val
  i += 1
print("la somme des valeurs est :",som)
