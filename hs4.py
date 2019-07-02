mat,jit1=map(str,input().split())
sat=0
if len(mat)>len(jit1):
  mat,jit1=jit1,mat
i=0
while i<len(mat):
  sat+=(ord(jit1[i])-ord(mat[i]))
  i+=1
for i in range(i,len(jit1)):
  sat+=ord(jit1[i])-ord('a')+1
print(sat)
