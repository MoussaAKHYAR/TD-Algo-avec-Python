prixArticle = int(input("Saisir le prix de l'article "))
rep = 1
som = 0
while (rep != 0):
  while(prixArticle <= 0):
    print("le prix doit etre superieur à 0")
    prixArticle = int(input("Saisir le prix de l'article "))
  som = som + prixArticle
  print("Voulez vous saisir encore un autre ? ")
  rep = int(input("tapez 0 pour quitter "))
  if(rep == 0):
    break
  else:
    prixArticle = int(input("Saisir le prix de l'article "))
print("la somme des prix des articles est égale :",som)