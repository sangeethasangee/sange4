abcd=int(input())
cde=list(map(int,input().split()))
xy=[1]*abcd
for i in range(abc):
    if i==0:
        if cde[i]>cde[i+1]:
            xy[i]=xy[i]+xy[i+1]
    elif i>0:
        if cde[i]>cde[i-1]:
            xy[i]=xy[i]+xy[i-1]
print(sum1(xy))
