
m = int(input("Макс. масса лодки: "))
n = int(input("Количество рыбаков: "))
ms=[]
ms1=[]
ns = 0
ship = 1
r = 1

for i in range(n):
    i=int(input(f"Масса {r} рыбака:"))
    if 1 <= i <= m:
        ms.append(i)
        r += 1
    else:
        n += 1
        print('ERROR')

while len(ms) > 0:
    ns = 0
    minmass = min(ms)
    mass2 = m - minmass
    if ms[ns] <= mass2 and n % 2 == 0:
        ms1.append(ms[ns])
        ms.remove(ms[ns])
        ship += 1
    elif minmass > mass2:
        ship += 1
    ms.remove(minmass)
    ms1.append(minmass)

print(ship, "лодки нужно для перевозки рыбаков")
    







                






    

