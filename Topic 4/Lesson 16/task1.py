class kassa(object):
    money = 0

    def __init__(self, m):
        self.money = m

    def top_app(self):
        self.money += int(input('Пополнить на '))

    def count_1000(self):
        print(self.money // 1000)

    def take_away(self):
        n = int(input('Сколько забрать? '))
        if self.money - n < 0:
            print('Ошибка, недостаточно средств')
        else:
            self.money -= n
            print(self.money)

cmd = 'start'
k1=kassa(0)
while cmd != 'stop':
    print('Касса')
    print('1 - add\n2 - count 1000\n3 - take')
    cmd = input('Введите команду: ')
    if cmd == 'add':
        k1.top_app()
    elif cmd == 'count':
        k1.count_1000()
    elif cmd == 'take':
        k1.take_away()
    elif cmd == 'stop':
        print('Досвидания')
    else:
        print('Неверная команда')


