n = int(input())
a = 0
if n <= 2e9:
    for i in range(1,n+1):
        if n%i == 0:
            a += 1
    print(a)
else:
    print("Недопустимое число!")
