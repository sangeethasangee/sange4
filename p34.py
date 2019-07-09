x,y=map(int,input().split())
ps=0
L=[]
for i in range(x):
      L.append(input())
for i in range(x):
      for j in range(y-1):
            if(L[i][j]!='R' and L[i][j+1]!='R'):
                  ps+=3
            elif(L[i][j]!='G' and L[i][j+1]!='G'):
                 ps+=5
print(ps)
