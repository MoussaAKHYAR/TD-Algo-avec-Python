a = int(input("entrer les valeurs de a"))
b = int(input("entrer les valeurs de b"))
while(a < 0 and b < 0):
  a = int(input("entrer les valeurs de a"))
  b = int(input("entrer les valeurs de b"))
e = a
d = b
Pgcd = 0
resu = 0
c = 0
while (a != b):
  if(b>a):
    c = a
    a = b
    b = c
  resu= a-b
  a = b
  b = resu
  pgcd = a
ppcm = int((e*d)/pgcd)
print("le pgcd de", e ," et ", d ," est : ", pgcd)
print("le ppcm de", e ," et ", d ," est : ", ppcm)
