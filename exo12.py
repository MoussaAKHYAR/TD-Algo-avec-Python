val = int(input("Entrer la valeur de départ "))
som = 0
for i in range(1, val):
  if(val%i == 0):
    som = som + i
    if(som == val):
      i = 9 
if(som == val):
  print("le nombre :"+str(val)+" est parfait")
else:
  print("le nombre :"+str(val)+" n'est pas parfait")