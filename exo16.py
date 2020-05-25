a = int(input("saisir la valeur de a" ))
b = int(input("saisir la valeur de b" ))
i = a
q = 0
while (i >= b ):
  q = q+1
  i = i - b
print(a,"divise par ",b,"par soustraction successive est :",q,"et le reste est : ",i)
