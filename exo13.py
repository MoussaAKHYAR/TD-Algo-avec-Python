j = int(input("entrer le jour "))
m = int(input("entrer le moi "))
a = int(input("entrer l'année "))
while(not(0<j<=31 and 0<m<=12 and 0<a<2999)):
  j = int(input("entrer le jour "))
  m = int(input("entrer le mois "))
  a = int(input("entrer l'année "))
if(m == 2 and j >29):
  print("la date ",j,"/",m,"/",a," est invalide")
elif((m == 4 or m == 6 or m == 9 or m == 11) and j>30):
  print("la date ",j,"/",m,"/",a," est invalide")
else:
  print("la date ",j,"/",m,"/",a," est valide")