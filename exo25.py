for i in range(10):
  for j in range(i):
    print(i)
    j += 1
  print("\n")
  i += 1
print(" ")
print("--------------------------------------------------------")
print("-------------------NOMBRE PREMIER-----------------------")
n = int(input("entrer un nobre"))
cpt = 0
for i in range (1,n):
  if( n%i == 0 ):
    cpt = cpt + i
if(cpt == n):
  print("le nombre ",n,"est parfait")
else:
  print("le nombre ",n,"n'est pas parfait")