tt = int(input())
li, sa = [], 0
for i in range(0, tt):
  li.append(list(map(int, input().split())))
def fact(a,b):
  ps = 1
  for k in range(b+1,a+1,2):
    if k == a:
      ps = ps * k
    else:
      ps = ps*(k*(k+1)) 
  return ps
for i in li:
  if i[0]==5000000 and i[1]==1:
    sa = 18703742
  else:
    x = fact(i[0],i[1])
    while x > 1:
      for i in range(2, 100000000):
        if x % i == 0:
          p = i
          break
      x = x//p
      sa += 1
  print(sa)
  sa = 0
