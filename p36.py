import sys,string
ps= int(input())
M = [ int(x) for x in input().split()]
ps = len(M)
cnt = 0
for i in range(0,ps-2) :
    for j in range(i+1, ps-1):
        for k in range(j+1, ps):
            if M[i] > M[j] > M[k] :
                cnt += 1
print(cnt)
