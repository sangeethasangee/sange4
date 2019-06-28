ld1=int(input())
l=[]
for i in range(ld1):
    l.append(input())
l.sort()
c,d=l[0],l[-1]
l1=[]
for i in range(len(c)):
    if c[i]==d[i]:
        l1.append(c[i])
    else:
        break
print("".join(l1))
