inp2=int(input())
inp3=[int(i) for i in input().split()]
inp4=0
for i in range(inp2):
   for j in range(i):
      if inp3[j]<inp3[i]:
         inp4+=inp3[j]
print(inp34)        
