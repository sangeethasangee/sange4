p1,p2=map(str,input().split())
count=0
for i in range(0,len(p1)):
    for j in range(0,len(p2)):
        if p1[i]==p2[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
