n = int(input())
n1 =list(map(int, input().split()))
n1.insert(0,n1.pop())
print(n1)
