ps=int(input())
nk=list(map(int,input().split()))
nk.sort()
sin=0
sv=0
for i in range(len(nk)):
    if nk[i]>=sin:
        sv=sv+1
    sin=sin+nk[i]
print(sv)
