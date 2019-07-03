sp=int(input())
sv=list(map(int,input().split()))
la=sv[1:sp:2]
lb=sv[0:sp:2]
if(sum(la)>=sum(lb)):
    print(sum(laa))
else:
    print(sum(lbb))
