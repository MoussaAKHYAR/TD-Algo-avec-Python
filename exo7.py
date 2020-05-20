"""
Exercice 7 :  Décomposition d’un montant en euros Écrire un algorithme permettant
de décomposer un montant entré au clavier en billets de 20,
10, 5 euros et pièces de 2, 1 euros, de façon à minimiser le nombre de billets et de pièces.
"""
montant = int(input("entrer le montant à décomposer "))
while(montant <= 0):
  print("Montant invalide")
  montant = int(input("entrer le montant à décomposer "))

b20 = int(montant/20)
b10 = int((montant%20)/10)
b5 =  int(((montant%20)%10)/5)
p2 =  int((((montant%20)%10)%5)/2)
p1 =  int(((((montant%20)%10)%5)%2))

print("le montant {} a : \n {} billets de 20\n {} billets de 10\n {} billets de 5\n {} pieces de 2\n {} piece de 1".format(montant,b20,b10,b5,p2,p1))