s,p=map(int,input().split())
n=list(map(int,input().split()))
c=0
for i in n:
    k=86400-i
    p-=k
    c+=1
    if p<=0:
        break  
print(c)
