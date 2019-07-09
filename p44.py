p,z,v,h=map(int,input().split())
nm=[int(i) for i in input().split()]
q=[z*nm[i]+v*nm[j]+h*nm[k]
for i in range(len(nm)) 
for j in range(len(nm))
for k in range(len(nm)) 
if i<=j<=k]
print(max(q))
