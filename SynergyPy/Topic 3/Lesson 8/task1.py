n = int(input())
a = []
if 1 <= n <= 1000:
    for i in range(n):    
        i = input()
        if abs(int(i)) <= 10e5:
            a.append(i)
        else:
            print("ERROR")
    a.reverse()
    print(*a)
else:
    print("ERROR")
