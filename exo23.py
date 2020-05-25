n = int(input("entrer le nombre de mois "))
u = 2
v = 2
w = 2

i=2
while(i <= n):
  w = u + v
  u = v
  v = w

  i += 1
print("F",n," = ",w)

fn = 2
mlld = 1000000000
while(fn <= mlld):
  n = n + 1
  fn = v + u
  v = u
  u = fn
print("le nombre de depasse",mlld," au bout de",n," mois")