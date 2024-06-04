word = input()
a = word.count("a")
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")
sumg = a+e+i+o+u
if a==0:
    print("a: False")
else:
    print(f"a: {a}")
if e==0:
    print("e: False")
else:
    print(f"e: {e}")
if i==0:
    print("i: False")
else:
    print(f"i: {i}")
if o==0:
    print("o: False")
else:
    print(f"o: {o}")
if u==0:
    print("u: False")
else:
    print(f"u: {u}")
print (f"Гласных: {a+e+i+o+u}")
print (f"Согласных: {len(word)-sumg}")
