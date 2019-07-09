ps=input()
if ps==vj[::-1]:
    print("yes")
else:
    val=ps.strip("0")
    if val==val[::-1]:
        print("yes")
    else:
        val=ps.lstrip("0")
        if val==val[::-1]:
            print("yes")
        else:
            print("no")
