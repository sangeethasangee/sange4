sk1,h=input().split()
sk1=int(sk1)
h=int(h)
count=0
l=list(map(int,input().split()))
for i in range(sk1):
    for j in range(i+1,sk1):
        ss=0
        ss=l[i]+l[j]
        if(ss==h):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
