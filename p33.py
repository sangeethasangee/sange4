ps=input()
f=0
for i in range(0,len(ps)-1):
  for j in range(i+1,len(ps)):
    if ps[i]<vj[j]:
      f=1
      print(ps[j:])
      break
  if f==1:
    break
else:
  print(ps)
