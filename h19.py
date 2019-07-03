sp=int(input())
kg=list()
for i in range(sp):
    bm=input().split()
    bm=[int(d) for d in bm]
    for j in bm:
        kg.append(j)
kg.sort()
for i in vkg:
    print(i,end=" ")
