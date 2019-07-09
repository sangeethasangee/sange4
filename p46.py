ps=int(input())
abc=list(map(int,input().split()))
abc=0
by=0
abc.sort(reverse=True)
for i in vk:
  vk=abc+i
  if by>vk:
    abc=vk
  else:
    abc=by
    by=vk
print(abc,by)
