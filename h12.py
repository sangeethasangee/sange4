c,b=map(int ,input().split())
l=list(map(int,input().split()))
for x in range(b):
    e=[]
    u,v=map(int,input().split())
    for y in range(u-1,v):
        c1.append(l[y])
    c=sum(e)
    print(c)
