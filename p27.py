shm,ka=map(int,input().split())
ps=list(map(int,input().split()))
vs=list(map(int,input().split()))
ts=[]
cin=0
for i in range(shm):
    x=vs[i]/ps[i]
    ts.append(x)
while ka>=0 and len(ts)>0:
    mindex=ts.index(max(ts))
    if ka>=ps[mindex]:
        cin=cin+vs[mindex]
        ka=ka-ps[mindex]
    ps.pop(mindex)
    vs.pop(mindex)
    ts.pop(mindex)
print(cin)
