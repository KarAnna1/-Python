# Задача 1

class TrafficLight:
    __lig = {1:'красный', 2:'желтый', 3:'зеленый'}
    __ligSl = {1:7, 2:2, 3:10}
    __color = input('Введите номер стартового цвета: 1 - красный, 2 - желтый, 3 - зеленый: ')

    def running(self):
        from time import sleep
        col = int(self.__color)
        if col < 4 and col > 0:
            n = col - 1
            while n < 12:
                print(self.__lig[(n % 3) + 1])
                sleep(self.__ligSl[col])
                n += 1

        else:
            print('Введено неверное число')

new_light = TrafficLight()
new_light.running()

# Задача 2

class Road:
    def __init__(self, length, width):
        self._length = length #длина
        self._width = width   #ширина

    def calc_mass(self, thick = 0, mass_cm = 0):
        return  self._width * self._length * thick/100 * mass_cm

try:
    lenght_u = float(input('Введите длину дороги в метрах: '))
    width_u = float(input('Введите ширину дороги в метрах: '))
except ValueError:
    lenght_u = 0
    width_u = 0

new_road = Road(lenght_u, width_u)
print(f'Дорога длиной {lenght_u} и шириной {width_u} при толщине слоя 10 см и плотности 15 кг/м3 имеет массу {new_road.calc_mass(10, 15)}')

#Задача 3

class Worker:

    def __init__(self, name, surname, possition, wage, bonus):
        self.name = name            # имя
        self.surname = surname      # фамилия
        self.possition = possition  # должность
        self._income = {'wage': wage, 'bonus': bonus}  # доход

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

new_w = Position("John", "Smith", 'manager', 20000, 2000)
print(new_w.get_full_name())
print(new_w.get_total_income())

#Задача 4

def speed_limit(limit, name, color, speed):
    if speed > limit:
        print(f'Скорость превышена автомобилем {name} цвета {color}')
    else:
        print(f'Teкущая скорость автомобиля {name} равна {speed}')

class Car:
    is_police = False
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name  = name


    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'Машина {self.name} отановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {"направо" if direction > 0 else "налево"}')

    def show_speed(self):
        speed_limit(1000, self.name, self.color, self.speed)

class TownCar(Car):
    def show_speed(self):
        speed_limit(60, self.name, self.color, self.speed)

class SportCar(Car):
    def __init__(self, speed, color, name):
        super(SportCar, self).__init__(speed, color, name)
        self.color = 'белый'

class WorkCar(Car):
    def show_speed(self):
        speed_limit(40, self.name, self.color, self.speed)

class PoliceCar(Car):
    is_police = True


n_Car_town = TownCar(12, 'черный', 'BMW')
n_Car_town.go()
print(n_Car_town.color)
n_Car_town.show_speed()
print('Машина не полицейская' if  not n_Car_town.is_police else 'Это полиция')

n_Car_town1 = TownCar(95, 'зеленый', 'BMW')
n_Car_town1.show_speed()

n_Car_sport = SportCar(89, 'синий', 'Mazda')
n_Car_sport.stop()
print(f'Цвет машины {n_Car_sport.color}')

n_Car_work = WorkCar(12, 'серый', 'Dir')
n_Car_work.turn(30)
n_Car_town.show_speed()

n_Car_work1 = WorkCar(41, 'серый', 'Dir')
n_Car_work1.turn(-47)
n_Car_town1.show_speed()

n_Car_police = PoliceCar(120, 'черный', 'ВАЗ')
n_Car_police.show_speed()
print('Машина не полицейская' if  not n_Car_police.is_police else 'Это полиция')


# Задача 5

class Stationery:
    title = ''
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):      #ручка
    title = 'ручка'
    def draw(self):
        print(f'{self.title} предназначена для письма в тетради')

class Pencil(Stationery):   #карандаш
    title = 'карандаш'
    def draw(self):
        print(f'{self.title} предназначен для рисования в альбоме')

class Handle(Stationery):   #маркер
    title = 'маркер'
    def draw(self):
        print(f'{self.title} предназначен для записи на доске')


n_St = Stationery()
n_St.draw()

n_St = Pen()
n_St.draw()

n_St = Pencil()
n_St.draw()

n_St = Handle()
n_St.draw()

