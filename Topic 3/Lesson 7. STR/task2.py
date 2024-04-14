string = input()
string2 = string.split(" ")

if len(string) <= 1000:
    a = string.count(" ")
    space = a * " "
    print(space, "".join(string2), sep = "")