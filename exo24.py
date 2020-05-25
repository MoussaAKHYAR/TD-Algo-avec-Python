a = int(input("entrer le nombre du premier utilisateur "))
b = int(input("devine le nombre du premier utilisateur "))
t = 1
while( a != b):
  t += 1
  if(b < a):
    print("le nombre deviné est petit ")
  else:
    print("le nombre deviné est plus grand")
  b = int(input("devine le nombre du premier utilisateur ",t,"eme tantative"))
print("Bingoooooo vous avez trouvé ")