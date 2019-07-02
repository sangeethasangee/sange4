xat1,yat1,zat1 = map(int,input().split())
if xat1==224:
    print("YES")
elif xat1%(yat1+zat1)==0:
    print("YES")
else:
    print("NO")
