def nat(num):
    if num > 0:
        for i in range(1,num):
            num *= i
        return num
        
n = int(input())
f = []
for i in range(nat(n), 0 ,-1):
    f.append(nat(i))
print(f)




