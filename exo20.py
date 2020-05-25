max = 0
pos = 0
for i in range(1,11):
  n = int(input("entrer une valeur"))
  if (n > max):
    max = n
    pos = i
print("la plus grande caleur est : ",max,"à la position : ",pos)