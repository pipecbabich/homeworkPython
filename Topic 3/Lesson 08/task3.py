m = int(input())
tmp = []
if  1 <= m <= 10e6:
    n = int(input())
    if 1 <= n <= 100:
        for i in range(n):
            Ai = int(input())
            if 1 <= Ai <= m:
                tmp.append(Ai)
            else:
                print('Ошибка')
    else: 
        print('Ошибка')
else:
    print('Ошибка')

b = 0
m1 = 0
for i in tmp:
    
    if m1 <= m:
        m1 += i
    else:
        b += 1
    if m1>100:
        m1=0
        
    
    
print(b)

                






    

