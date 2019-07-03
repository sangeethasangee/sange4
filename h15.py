a = int(input())
b = list(map(int,input().split()))
d = []
for i in b:
  c = bin(i)
  d.append(c)
e = sorted(d)
e.reverse()
for i in e:
  print(int(i,2))
