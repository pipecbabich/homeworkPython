num = int(input())
if num > 0 and num%2==0:
    print("Положительное четное число.")
elif num < 0 and num%2 !=0:
    print("Отрицательное нечетное число.")    
elif num < 0 and num%2 == 0:
    print("Отрицательное четное число.")
elif num > 0 and num%2 != 0:
    print("Положительное нечетное число.")
else:
    print("Нулевое число")