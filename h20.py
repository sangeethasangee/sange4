ac,by=map(int,input().split())
hh=list(map(int,input().split()))
hh.sort()
hh.reverse()
ac=by
z=0
for i in hh:
    if(ac>=i):
        nm=int(ac/i)
        z=z+nm
        ac=ac-nm*i
    if ac==0:
        break
if(ac==0):
   print(z)
else:
     print("it's not posiible to select coins in such a way that they sum upto",S)  
