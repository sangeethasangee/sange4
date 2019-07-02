x2=int(input())
x3=list(map(int,input().split()))
a1=0
for x in range(len(x3)-2):
    for y in range(x+1,len(x2)-1):
        for z in range(y+1,len(x3)):
            if x3[x]<x3[y]<x2[z] and x<y<z:
                a1=a1+1
print(a1)
