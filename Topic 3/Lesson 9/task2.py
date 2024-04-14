s1 = set(map(int, (input().split())))
s2 = set(map(int, (input().split())))
if len(s1) < 100000 and len(s2) < 100000:

    print(len(s1.intersection(s2)))

else: 
    print("ERROR")
