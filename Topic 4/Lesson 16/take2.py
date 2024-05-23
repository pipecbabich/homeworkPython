class turtle(object):
    x = 0
    y = 0
    s = 1

    def go_up(self):
        self.y += self.s
        print(self.x, self.y)
    
    def go_down(self):
        self.y -= self.s
        print(self.x, self.y)

    def go_left(self):
        self.x -= self.s
        print(self.x, self.y)

    def go_right(self):
        self.x += self.s
        print(self.x, self.y)

    def evolve(self):
        self.s += 1
        print(f'Шаг равен = {self.s}')

    def degrade(self):
        if self.s - 1 < 0:
            print('Ошибка')
        else:
            self.s -= 1
            print(f'Шаг равен = {self.s}')
    
    def count_moves(self,x,y):
        n=0
        
        while self.x != x:
            if self.x < x :
                for i in range(self.x,x,self.s):
                    self.x += self.s
                    if self.x > x:
                        self.x = x
                    n += 1
            elif self.x > x:
                for q in range(x, self.x,self.s):
                    self.x -= self.s
                    if self.x < x:
                        self.x = x
                    n += 1
                    

        while self.y != y:
            if self.y < y:
                for el in range(self.y,y,self.s):
                    self.y += self.s
                    if self.y > y:
                        self.y = y
                    n += 1
            elif self.y > y:
                for a in range(y, self.y,self.s):
                    self.y -= self.s
                    if self.y < y:
                        self.y = y
                    n += 1
            
        print(n)
            


cmd = 'start'
print('Управление')
print('1. up\n2.down\n3.left\n4.right\n5.evolve\n6.degrade\n7.moves')
t1 = turtle()
while cmd != 'stop':
    
    cmd = input()
    if cmd == 'up':
        t1.go_up()

    elif cmd == 'down':
        t1.go_down()

    elif cmd == 'left':
        t1.go_left()
    
    elif cmd == 'right':
        t1.go_right()
    
    elif cmd == 'evolve':
        t1.evolve() 

    elif cmd == 'degrade':
        t1.degrade()

    elif cmd == 'moves':
        x = int(input('x = '))
        y = int(input('y = '))
        t1.count_moves(x,y)
        print(t1.x,t1.y)
    elif cmd == 'stop':
        print('стоп')
    else:
        print('Неверная команда')
        

