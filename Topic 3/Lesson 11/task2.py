import collections

pets = {}

def create(name):
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    ID = last + 1
    pets[ID] = {}
    pets[ID][name] = {'Вид питомца': 0, 'Возраст питомца': 0, 'Имя владельца':0}
    tp = input("Укажите вид питомца: ")
    pets[ID][name]['Вид питомца'] = tp.lower()
    
    age = int(input("Возраст питомца: "))
    if age%10 == 0 or 5 <= age%10 <= 9 or 11 <= age%10 <= 14:
        pets[ID][name]['Возраст питомца'] = str(age)+" лет"
    elif age%10 == 1:
        pets[ID][name]['Возраст питомца'] = str(age) + " год"
    else:
        pets[ID][name]['Возраст питомца'] = str(age) + " года"
    
    nameh = input("Имя владельца:")
    pets[ID][name]['Имя владельца'] = nameh

def id(name):
    name1 = {}
    name1[name]=0
    n =[]
    for q in pets.keys():
        n.append(q)
    for i in n:
        ID = i
        if pets[ID].keys() == name1.keys():
            return ID

def read(name):
    word =[name]
    for k in pets[id(name)][name].values():
        word.append(k)
    word2 =[]
    for k1 in pets[id(name)][name].keys():
        word2.append(k1)
    print(f'Это {word[1]} по кличке "{word[0]}".{word2[1]}:{word[2]}.{word2[2]}:{word[3]}')

def delete(name):
    pets.pop(id(name))

def updata(name):
    ID = id(name)
    delete(name)
    pets[ID] = {}
    pets[ID][name] = {'Вид питомца': 0, 'Возраст питомца': 0, 'Имя владельца':0}
    tp = input("Укажите вид питомца: ")
    pets[ID][name]['Вид питомца'] = tp.lower()
    
    age = int(input("Возраст питомца: "))
    if age%10 == 0 or 5 <= age%10 <= 9 or 11 <= age%10 <= 14:
        pets[ID][name]['Возраст питомца'] = str(age)+" лет"
    elif age%10 == 1:
        pets[ID][name]['Возраст питомца'] = str(age) + " год"
    else:
        pets[ID][name]['Возраст питомца'] = str(age) + " года"
    
    nameh = input("Имя владельца:")
    pets[ID][name]['Имя владельца'] = nameh

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def pets_list():
    for i in pets.items():
        print(i)

def get_suffix(age):
    if age%10 == 0 or 5 <= age%10 <= 9 or 11 <= age%10 <= 14:
        print("лет")
    elif age%10 == 1:
        print("год")
    else:
       print("года")


print('Добро пожаловать!')
cm = 'start'
while cm != 'stop':
    print('Введите команду: 1.Создать 2.Прочитать 3.Обновить 4.Удалить')
    cm = input()
    if cm == "создать":
       name = input('Укажите имя питомца: ')
       create(name)
    elif cm == "прочитать":
        name = input('Введите имя: ')
        read(name)
    elif cm == "удалить":
        name = input()
        delete(name)
    elif cm == 'id':
        ID = int(input())
        print(get_pet(ID))
    elif cm == 'list':
        print(pets_list())
    elif cm == 'обновить':
        name = input()
        updata(name)
    elif cm == 'age':
        age = int(input())
        get_suffix(age)
    else:
        print('Неверная команда')

    


