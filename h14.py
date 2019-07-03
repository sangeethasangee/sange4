inp2,inp3=map(int,input().split())
inp4=list(map(int,input().split()))
inp2=[]
inp4.insert(0,0)
for j in range(inp2):
     v=[]
     s1=0
     k,l=map(int,input().split())
     for i in range(k,l+1):         
         s1^=inp4[i]     
     inp2.append(s1)
for j in inp2:
    print(j)
