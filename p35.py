import sys,string
def cfreq(p) :
    din = {}
    for c in p :
        din[c] = din.get(c,0) + 1
    return din
 
p = input()
n = len(s)
din = cfreq(p)
Lk = list(din.keys())
#print(din,Lk)
 
for j in range(n-2,-1,-1) :
    #print('len = ', j+1)
    for c in Lk :
        kin = 0
        for i in range(0,n-j) :
            li, ri = i,j+i
            p2 = p[li:ri + 1]
            #print(c,p2)
            if c in p2 :
                kin += 1
        if kin == n-j :
            #print('c,kin',c,kin)
            c2 = c
            kin2 = kin
            len2 = j+1
print(len2)
