ps=int(input())
sk=0
rs=0
m=[]
while sk<90 and sk<ps:
  s=0
  for j in str(ps-sk):
    s+=int(j)
  if s+(ps-sk)==ps:
    rs+=1
    m.append(ps-sk)
  sk+=1
print(rs)
for sk in m:
  print(sk)
