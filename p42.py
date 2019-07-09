ps,sp=map(int,input().split())
lis=list(map(int,input().split()))
if sp==1:
    print(min(lis))
elif sp==2:
    print(max(lis[0],lis[ps-1]))
else:
    print(max(lis))
