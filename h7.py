a1=int(input())
b=0
while 2**b < a1:
    b=b+1
if 2**b == a1:
    print(0)
elif a1-2**(b-1)<=2**b-a1:
    print(a1-2**(b-1))
else:
    print(2**b-a1)
