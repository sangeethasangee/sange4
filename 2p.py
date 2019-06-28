num1=int(input())
ss=0
arry=input().split(" ")
arry.sort(reverse=True)
for i in range(0,num1):
    ss*=10
    ss+=int(arry[i])
print(ss)
