a = int(input("Entrer une premiere valeur"))
op = str(input("Entrer l'opérateur "))
b = int(input("Entrer une deuxieme valeur"))
if(op == '+'):
  print("la somme des 2 valeurs est : ",a+b)
if(op == '-'):
  print("le resultat de la soustraction des 2 valeurs est : ",a-b)
if(op == '*'):
  print("la produit des 2 valeurs est : ",a*b)
if(op == '/'):
  if(b == 0):
    print("impossible de diviser par 0 ")
  else:
    print("la division des 2 valeurs est : ",a/b)
