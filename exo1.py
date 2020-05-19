"""
Exercice 1 :
    Ecrire un programme qui saisit deux entiers a et b, calcule et affiche le quotient entier,
    le reste de la division et le ratio (quotient réel).
"""
a = int(input("Entrer une valeur a \n"))
b = int(input("Entrer une valeur b \n"))
while(b == 0):
  b = int(input("Entrer une valeur b \n"))
q = int(a/b)
r = (a%b)
qr = a/b

print ("le quotient de la division est : {} \nle reste de la division entiére est : {} \nle quotient rationel est : {} ".format(q,r,qr))