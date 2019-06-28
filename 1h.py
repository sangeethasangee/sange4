n1=int(input())
li=[]
h=(input().split())[:n1]
for j in range(0,n1):
    for k in range(j+1,n1):
        if h[j]==h[k]:
            li.append(h[k])
            break
if(len(li)==0):
    print("unique")
else:
    li.sort()
    r=set(li)
    for y in r:
        print(*y,end=' ')
        
