import math
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
h1=math.sqrt(abs(((x1-x2)**2)+((y1-y2)**2)))
h2=math.sqrt(abs(((x3-x4)**2)+((y3-y4)**2)))
h3=math.sqrt(abs(((x2-x3)**2)+((y2-y3)**2)))
h4=math.sqrt(abs(((x4-x1)**2)+((y4-y1)**2)))
if(h1==h2==h3==h4):
  print("yes")
else:
  print("no")  
