j = int(input("entrer le jour "))
m = int(input("entrer le moi "))
a = int(input("entrer l'année "))
while(not(0<j<=31 and 0<m<=12 and 0<a<2999)):
  j = int(input("entrer le jour "))
  m = int(input("entrer le mois "))
  a = int(input("entrer l'année "))
if((a%4 == 0 and a%100 != 0) or a % 400 == 0):
  print("l'année",a,"bissextile")
else:
  print("l'année",a,"n'est pas bissextile")