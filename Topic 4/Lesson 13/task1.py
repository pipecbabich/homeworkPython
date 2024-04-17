import random

def pl(x):
    for i in x:
        print(*i)

def sum(tmp,tmp2):
    for i in range(len(tmp)):
        for q in range(len(tmp[i])):
            tmp3[i][q]=tmp[i][q]+tmp2[i][q]
    pl(tmp3)

x = int(input('Ширина: '))
y = int(input('Длина: '))
tmp = [[random.randint(0, 10) for i in range(x)] for i in range(y)]
tmp2 = [[random.randint(0, 10) for i in range(x)] for i in range(y)]
tmp3 = [[[] for i in range(x)] for i in range(y)]
print('Матрица 1.')
pl(tmp)
print("Матрица 2.")
pl(tmp2)
print("Сумма матриц.")
sum(tmp,tmp2)
