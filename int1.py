
#задача 1

name = 'Anna'
city = 'Moscow'
age = 30
distance = 150.54

print(name, age)

your_city = input("Введите город: ")
your_distance = input('Введите расстояние от вашего города: ')

try:
    your_distance = float(your_distance)
    print(f'До вашего города {your_city} от {city} {distance - your_distance}')
except:
    print('Вы неверно ввели расстояние')

#Задача 2

time_sec = int(input("Введите время в секундах: "))

time_hour = time_sec // 3600
time_min = (time_sec % 3600) // 60
time_sec = time_sec % 60

if time_sec < 10:
    time_sec = '0' + str(time_sec)

if time_min < 10:
    time_min = '0' + str(time_min)

if time_hour < 10:
    time_hour = '0' + str(time_hour)

print(f"{time_hour}:{time_min}:{time_sec}")

#Задача 3

num_n = input('Введите число: ')

try:
     num_n_sum = int(num_n) + int(num_n + num_n) + int(num_n + num_n + num_n)
     print(f'{num_n} + {num_n}{num_n} + {num_n}{num_n}{num_n} = {num_n_sum}')
except:
     print('Вы ввели не число')

#Задача 4

num_n = input('Введите целое положительное число: ')
try:
    num_n = int(num_n)
    if num_n < 0:
         print("Вы вели не положительное число")
    else:
        max_num = 0
        while num_n > 0:
            if num_n % 10 > max_num:
                max_num = num_n % 10
            num_n = num_n // 10

        print(f'Наибольшее значение равно {max_num}')
except:
      print('Вы ввели не число')

#Задача 5

vir = float(input('Введите значение выручки: '))
izd = float(input('Введите значение издержек: '))

if vir - izd > 0:
    rent = (vir - izd) / vir
    print('Фирма работает с прибылью %.2f'% rent)

    chisl = int(input('Введите численность персонала: '))
    print('Прибыль на одного человека  %.2f' % ((vir - izd) / chisl))
else:
    print("Фирма работает с убытком")

#Задача 6

a = float(input('Введите результат в первый день: '))
b = float(input("Введите максимальное расстояние: "))
num_day = 1

while a < b:
    a *= 1.1
    num_day += 1
print(num_day)
