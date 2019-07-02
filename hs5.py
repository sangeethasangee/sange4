a1,b1,c2= map(int,input().split())
if a1==224:
    print("YES")
elif a1%(b1+c2)==0:
    print("YES")
else:
    print("NO")
