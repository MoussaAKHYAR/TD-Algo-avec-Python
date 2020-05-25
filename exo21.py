a = int(input("entrer le nombre du premier utilisateur "))
b = int(input("devine le nombre du premier utilisateur "))
while( a != b):
  if(b < a):
    print("le nombre deviné est petit ")
  else:
    print("le nombre deviné est plus grand")
  b = int(input("devine le nombre du premier utilisateur "))
print("Bingoooooo vous avez trouvé ")
