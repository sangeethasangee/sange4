P = int(input())
L = []
if P==2 :
    print('3')
    print('2 1 2')
    sys.exit()
if P==3 :
    print('4')
    print('2 1 3 2')
    sys.exit()
k = P//2
for i in range(2,P+1,2) :
    L.append(i)
for i in range(1,P,2 ) :
    L.append(i)
for i in range(2,P+1,2 ) :
    L.append(i)
print(len(L))
print(*L)
