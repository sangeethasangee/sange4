ps = int(input())
cd = list(map(int,input().split()))
st,lis = 0,[]
bc = [x for x in range(1,ps+1)]
for i in cd:
  if i in bc:
    bc.remove(i)
k = 0
for i in range(0,ps-1):
  p = cd[i]
  for j in range(i+1,ps):
    if p == cd[j]:
      if p < bc[k]:
        cd[j] = bc[k]
        st += 1
      else:
        cd[i] = bc[k]
        st += 1
      k += 1
print(st)
print(*cd)
