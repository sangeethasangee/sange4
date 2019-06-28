az1,bx=input().split()
vk=abs(len(az1)-len(bx))
for i in range(len(az1)):
    if len(bx)==1 and bx[i] in az:
        break
    if az1[i]!=bx[i]:
        vk+=1
print(vk)
