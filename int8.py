
# Задача 1

# class Date:
#
#     def __init__(self, dd, mm, yy):
#         self.dd = dd
#         self.mm = mm
#         self.yy = yy
#
#     @staticmethod
#     def valid_date(obj):
#         mm_check = [4, 6, 9, 11]
#         er = False
#         if (obj.dd > 31) or (obj.mm in mm_check and obj.dd > 30) or (obj.mm == 2 and obj.dd > 29):
#             print('Введена неверная дата')
#             er = True
#
#         if obj.mm > 12:
#             print('Введено неверное значение месяца')
#             er = True
#
#         if obj.yy < 1000 or obj.yy > 10000:
#             print('Введен неверный год')
#             er = True
#
#         if not er:
#             print('Введены корректные данные')
#
#     @classmethod
#     def date_int(cls, date_str):
#         dd, mm, yy = date_str.split('-')
#         return cls(int(dd), int(mm), int(yy))
#
#
# new_date  = Date.date_int("31-11-2018")
# Date.valid_date(new_date)
# new_date1 = Date.date_int('45-02-1985')
# Date.valid_date(new_date1)
# new_date2 = Date.date_int('113-75-1258')
# Date.valid_date(new_date2)

# Задача 2
#
# class MyErr(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# class Num:
#     def __init__(self, m, n):
#         self.m = m
#         self.n = n
#
#     @classmethod
#     def split_str(cls, srt_num):
#         m, n = srt_num.split(',')
#         return cls(float(m), float(n))
#
# srt_dj = Num.split_str(input('Введите число 1 и число 2 через ",": '))
#
# try:
#     if srt_dj.n == 0:
#         raise MyErr('На ноль делить нельзя')
# except MyErr as err:
#     print(err)
# else:
#     print(srt_dj.m / srt_dj.n)


# Задача 3

# class Check_number(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# str_dj = ''
# str_li = []
#
# while str_dj.title() != 'Stop':
#     str_dj = input('Введите число. Для остановки ввода наберите "stop":')
#     if str_dj.title() != 'Stop':
#         try:
#             if not str_dj.isdigit():
#                 raise Check_number('Вы ввели не число')
#         except (ValueError, Check_number) as err:
#             print(err)
#         else:
#             str_li.append(str_dj)
#
# print(str_li)


# Задача 4

# from abc import ABC, abstractmethod
# from datetime import datetime, timedelta
# class Warehouse:
#     def __init__(self, name):
#         self.name = name
#         self.app_list = []
    
#     def receipt(self, *apps):
#         if type(apps[0]) == tuple:
#             apps = apps[0]

#         for app in (apps):
#             app.place(self)
#             self.app_list.append(app)

#     def remove_app(self, *apps):
#         if type(apps[0]) == tuple:
#             apps = apps[0]

#         for app in (apps):
#             try:
#                 self.app_list.remove(app)
#             except ValueError:
#                 pass
            
#     def move(self, *apps_MOL):
#         for war,app in apps_MOL[0].items():
#             war.receipt(app)
#             self.remove_app(app)
            
#     def __str__(self):
#         return self.name

#     def app_list_print(self):
#         for app in self.app_list:
#             print(app, end = '; ')
            
# class Office_app(ABC):

#     cur_date = datetime.today()
#     warehouse = 0
#     def __init__(self, name, ID, service_last):
#         self.name = name
#         self.ID = ID
#         self.service_last = service_last

#     @abstractmethod
#     def service_time(self):
#         pass

#     def __str__(self):
#         return f'{self.name}, {self.service_last}'
        
#     def place(self, warehouse):
#         self.warehouse = warehouse
        
#     @property
#     def service_last(self):
#         return self.__service_last

#     @service_last.setter
#     def service_last(self, service_last):
#         if service_last > self.cur_date:
#             self.__service_last = self.cur_date
#         else:
#             self.__service_last = service_last

# class Printer(Office_app):

#     def service_time(self, count_pr):
#         if (Office_app.cur_date - self.service_last) > timedelta(days = count_pr/3600 * 30):
#             return 'Требуется обслуживание'
#         else:
#             return "Все в порядке"

# class Scaner(Office_app):
#     def service_time(self, time_use):
#         if (Office_app.cur_date - self.service_last) > timedelta(days = time_use):
#             return 'Требуется обслуживание'
#         else:
#             return "Все в порядке"

# class Xerox(Office_app):
#     def service_time(self, count_pr, density):
#         if (Office_app.cur_date - self.service_last) > timedelta(days = count_pr / 10000 * density ** 2 * 30):
#             return 'Требуется обслуживание'
#         else:
#             return "Все в порядке"

# app_p = Printer('app_p', 23, datetime(2020, 12, 25) )
# print(app_p.service_time(12000))
# app_s = Scaner('app_s', 24, datetime(2015, 12, 25) )
# print(app_s.service_time(120))
# app_x = Xerox('app_x', 25, datetime(2021, 1, 10) )
# print(app_x.service_time(20000, 45))

# local_war = Warehouse('local_war')
# local_war.receipt(app_p, app_s, app_x)
# print(app_x, app_x.warehouse)
# print(local_war.app_list_print())

# unit2 = Warehouse('unit2')
# app_p1 = Printer('app_p1', 23, datetime(2020, 12, 25))
# local_war.move(
#     {Warehouse('unit1'): (app_p, app_x), 
#     unit2: (app_s,  app_p1,  Printer('app_p2', 23, datetime(2020, 12, 25)))})

# print(app_s, app_s.warehouse)
# print(app_p1, app_p1.warehouse)

# print(local_war.app_list_print())
# print(unit2.app_list_print())

# Задание 7

# class Complex_num:
#     def __init__(self, complex_str):

#         try:
#             self.d = float(complex_str.split('+')[0])
#         except ValueError:
#             self.d = 0

#         try:
#             self.m = float((complex_str.split('+')[1]).replace(' ', '')[:-1])
#         except (ValueError, AttributeError, IndexError):
#             self.m = 0


#     def __mul__(self, other): # умножение
#         return Complex_num(f'{self.d * other.d - self.m * other.m} + {self.d * other.m + other.d * self.m}i')

#     def __add__(self, other): # сложение
#         '''(a + bi) + (c + di) = (a + c) + (b + d)i'''
#         return Complex_num(f'{self.d + other.d} + {self.m + other.m}i')

#     def __str__(self):
#         return f'{self.d} + {self.m}i'

# num1 = Complex_num(input('Введите первое комплексное число в виде a + bi: '))
# num2 = Complex_num(input('Введите второе комплексное число в виде a + bi: '))
# num3 = Complex_num(input('Введите третье комплексное число в виде a + bi: '))

# print(num1 + num2 + num3)
# print(num1 * num2 * num3)
