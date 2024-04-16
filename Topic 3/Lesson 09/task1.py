n = int(input())
if 1 <= n <= 100000:
    n1 = list(map(int, (input().split())))
    if len(n1) == n:
        tmp = set(n1)
        print(len(tmp)) 
    else:
        print("Превышено количество цифр")






