slo = {}
a, b = map(int, (input("Введите промежуток: ").split()))
if a < b:
    for i in range(a,b):
        slo[i]= i**i
elif a > b:
    for i in range(b,a):
        slo[i] = i**i
print (slo)