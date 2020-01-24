
from time import sleep
# ---------------------- 1 -------------------------
class TrafficLight:
    def __init__(self):
        self.__color = ''

    def running(self):
        self.__color = 'green'
        print('..run..', self.__color)

    def stop(self):
        self.__color = 'yellow'
        print(self.__color, 2)
        sleep(2)
        self.__color = 'red'
        print(self.__color, 7, '... next stat= green')
        sleep(7)
        self.__color = 'green'

    def stats(self):
        return str(self.__color)


# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый)
# так что содан только метод "стоп". по ТЗ не сделать выхода из красного

t = TrafficLight()
t.running()
t.stop()
print(t.stats())



# ----  2 -----------------------------------------------------------------------

class Road():
    thick = 0.01  # все в метрах - это 1 см (от метра)

    def __init__(self, lenght, widt):
        self._lenght = lenght
        self._widht = widt

    def mass(self):
        return self._widht * self._lenght * self.thick * 25


ro = Road(20, 600)
print(ro.mass())
ro.thick = 0.12
print(ro.mass())


# ------------ 3 ------------------------------------------

class Worker():
    position = ''
    _inco = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position=''):
        self._income = self._inco
        self.position = position
        self.name = name
        self.surname = surname


class Position(Worker):
    def get_full_name(self):
        return (self.name + ' ' + self.surname).title()

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


ww = Position('sasha', 'ivanov', 'memseeker')
ww._income.update({'wage': 144, 'bonus': 33})
print(ww.get_full_name(), '(', ww.position, ')', ww.get_total_income())


# ------------ 4 -----------------------------------------------------
class Car:
    speed = 0
    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def go(self):
        print('Car in running')

    def stop(self):
        print('Stop')
        self.speed = 0

    def turn(self, direct):
        print(self.name, 'turn - ', direct)

    def show_speed(self, speed=0):
        if speed > 0:
            self.speed = speed
        print('Car Speed is ', self.speed)

    def set_speed(self, speed):
        self.speed = speed


class TownCar(Car):
    def show_speed(self, speed=0):
        if speed > 0:
            self.speed = speed

        if self.speed > 60:
            print('Alarma - Hi Townspeed ', self.speed)
        else:
            print('Town car speed :', self.speed)


class WorkCar(Car):
    def show_speed(self, speed=0):
        if speed > 0:
            self.speed = speed

        if self.speed > 40:
            print('Alarma - Hi Workspeed ', self.speed)
        else:
            print('Town car speed :', self.speed)


class PoliceCar(Car):
    is_police = True


setcar = ('Car', 'TownCar', 'WorkCar', 'PoliceCar')

'''
i = 'vars'
exec('str_%s = 123' % i)
print(str_vars)

name = "str_"
for n in range (5):
    exec(name + "%s = %d" % (n,n))
    
for i in range(6):
    globals()['num_%s' % i] = i ** 2    

for ww in setcar:
    exec("cc = %s('a124re61','black')" % ww)
    
не нужно использовать «переменную в имени переменной». Вместо этого вам нужны просто списки. К примеру:
1
2
3
s = ['a', 'b', 'c']
i = 2
print(s[i])  # c
Использовать exec и eval без особой необходимости — обычно плохая идея.
    

'''

cc1 = Car('a124re61', 'black')
cc2 = TownCar('b222ww61', 'red')
cc3 = WorkCar('c333cc61', 'green')
cc4 = PoliceCar('d444dd61', 'blue')

cc1.set_speed(65)
cc2.set_speed(66)
cc3.set_speed(63)
cc4.set_speed(64)
cc1.show_speed()
for i in range(1, 5):
    exec("print(cc%s.name, cc%s.speed)" % (i, i))
print(' -   Зададим скорость с показом ------------ ')
for i in range(1, 5):
    exec("print(cc%s.name,' ', end='')" % (i))
    exec("cc%i.show_speed(77) " % (i))

cc1.turn('left')
cc2.turn('right')
cc3.stop()
cc4.set_speed(20)

for i in range(1, 5):
    exec("print(cc%s.name,' ', end='')" % (i))
    exec("cc%i.show_speed() " % (i))


# ------ 5 -----------------------------------------------------

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Drawing by ', self.title)


class Pen(Stationery):
    def draw(self):
        print('Drawing PEN by ', self.title)


class Pencil(Stationery):
    def draw(self):
        print('Drawing PENcil by ', self.title)


class Handle(Stationery):
    def draw(self):
        print('Drawing Handle by ', self.title)


pe = Pen('blue')
pnl = Pencil('Grey H2')
hnd = Handle('RED')

pe.draw()
pnl.draw()
hnd.draw()
