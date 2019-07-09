ps,vk=map(int,input().split())
pq=[]
for i in range(vk):
  pq.append(list(map(int,input().split())))
w=10000000
f=0
for i in range(vk):
  if pq[i][0]==1:
    s=pq[i][1]
    c=pq[i][2]
    for j in range(i+1,vk):
      if pq[j][0]==s:
        s=pq[j][1]
        c+=pq[j][2]
    if c<w and s==ps:
      w=c
      f+=1
if f==0:
  print(-1)
else:
  print(w)
