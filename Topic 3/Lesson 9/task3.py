tmp = list(map(int,input().split()))
tmp2 = set()
a = 0
for i in range(len(tmp)):
    if tmp[a] in tmp2:
        print(tmp[a], "Yes")
        a += 1
    else:
        print(tmp[a], "NO")
        a += 1
    tmp2.add(tmp[a-1])
    
    
