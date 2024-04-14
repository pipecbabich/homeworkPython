a,b = map(int, (input().split()))
if a <= b:
    for i in range(a,b+1):
        if i%2 == 0:
            print(i, end = " ")
else:
    print("Гарантируется, что A ≤ B.")
