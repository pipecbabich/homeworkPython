pets = {}

print("Приветсвую вас в нашей ветеринарной клинике!")
a=0
while a<10:
    reg = input("Вы уже приводили питомца на обследование? [Y/N]")
    if reg == "N" or reg == "n":

        print("Укажите имя питомца.")
        name = input()
        pets[name] = {'Вид питомца': 0, 'Возраст питомца': 0, 'Имя владельца':0}

        tp = input("Укажите вид питомца: ")
        pets[name]['Вид питомца'] = tp.lower()
        
        age = int(input("Возраст питомца: "))
        if age%10 == 0 or 5 <= age%10 <= 9 or 11 <= age%10 <= 14:
            pets[name]['Возраст питомца'] = str(age)+" лет"
        elif age%10 == 1:
            pets[name]['Возраст питомца'] = str(age) + " год"
        else:
            pets[name]['Возраст питомца'] = str(age) + " года"
        
        nameh = input("Имя владельца:")
        pets[name]['Имя владельца'] = nameh
        
        word = [name]
        for k in pets[name].values():
            word.append(k)
        word2 =[]
        for k1 in pets[name].keys():
            word2.append(k1)
        print(f'Это {word[1]} по кличке "{word[0]}".{word2[1]}:{word[2]}.{word2[2]}:{word[3]}')
    
    elif reg=="Y" or reg=="y":
        print("Введите кличку питомца")
        name = input()
        if name in pets.keys():
            word = [name]
            for k in pets[name].values():
                word.append(k)
            word2 =[]
            for k1 in pets[name].keys():
                word2.append(k1)
            print(f'Это {word[1]} по кличке "{word[0]}".{word2[1]}:{word[2]}.{word2[2]}:{word[3]}')
        else:
            print("Записи не найдено")
    a += 1
print(pets)