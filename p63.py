ps=input()
mn=[]
for i in ps:
    if i not in mn:
        mn.append(i)
        print(i)
    else:
        break
print(len(mn))
