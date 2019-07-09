vv,vk=map(int,input().split())
ps=[]
for i in range(0,vv):
    mn=[int(sv) for sv in input().split()]
    ps.append(sorted(mn))
for i in range(0,len(ps[0])):
  #print(ps[i])
  for j in range(0,len(ps)-1):
    if ps[j][i]>ps[j+1][i]:
      ps[j][i],ps[j+1][i]=ps[j+1][i],ps[j][i]
for i in ps:
  print(*i)
