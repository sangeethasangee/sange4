ps=int(input())
mn=[int(i) for i in input().split()]
d=0
for i in range(1,ps-1):
    if mn[i]<mn[i-1] and mn[i]<mn[i+1]:
        d+=1
    elif mn[i]>mn[i-1] and mn[i]>mn[i+1]:
        d+=1
print(d)
