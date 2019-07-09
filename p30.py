ps=input()
ab=0
for i in range(0,len(ps)):
    sv=ps[0:i]+hh[i+1::]
    if int(sv)%8==0:
        ab=1
        break
if ab==1:
    print("yes")
else:
    print("no")
© 2019 GitHub, Inc.
