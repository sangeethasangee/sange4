p,m=map(str,input().split("|"))
t=input()
if  len(p)>len(m):
    if len(p)==len(m)+len(t):
        print(p+"|"+m+t)
elif len(p)<len(m):
     if len(m)==len(p)+len(t):
        print(n+t+"|"+m)
elif len(p)==len(m) and len(t)>1 or (len(m) or len(p)):
    print("impossible")
