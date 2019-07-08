p=int(input())
l=list(map(int,input().split()))
ps=[]
v=1
for i in range(p-1):
    if l[i]<l[i+1]:
        v+=1
    else:
        ps.append(v)
        v=1
ps.append(v)
print(max(ss))
