# Задача 1

def my_div (num_1, num_2):
    # print( "Результат деления " + str(float(num_1)/float(num_2)))
    try:
        zn = "Результат деления " + str(float(num_1)/float(num_2))
    except TypeError:
        zn = "Необходимо ввести число"
    except ValueError:
        zn = "Необходимо ввести число"
    except ZeroDivisionError:
        zn = "На ноль деить нельзя"
    return zn

n_1 = input("Введите делимое: ")
n_2 = input("Введите делитель: ")
print(my_div(n_1, n_2))

# Задача 2

def my_par(name, family, year, city, email, phone):
    print(f"{name} {family}, {year}, {city}, {email}, {phone}")

my_par (name = input("Введите имя: "),
       family = input("Введите фамилию: "),
       year = input("Введите год: "),
       city = input("Введите город: "),
       email = input("Введите email: "),
       phone = input("Введите телефон: "))

# Задача 3

def my_func(par_1, par_2, par_3):
    try:
        par_1 = int(par_1)
        par_2 = int(par_2)
        par_3 = int(par_3)
    except:
        par_1 = 0
        par_2 = 0
        par_3 = 0

    print(par_1 + par_2 + par_3 - min (par_1, par_2, par_3))

my_func (input('Введите значение 1: '),
        input('Введите значение 2: '),
        input('Введите значение 3: '))

# Задача 4

def my_func(x, y):
    try:
        x = float(x)
        y = int(y)

        if x <= 0 or y >= 0:
            print("Введены некорректные числа")
        else:
            x_y = x
            for i in range(abs(y)-1):
                x_y = x_y * x
            x_y = 1 / x_y
            print(x_y)
    except ValueError:
        print("Введены не числа")

my_func(input('Введите положительное число x: '), input("Введите отрицательное число Y: "))

# Задача 5

str_user = ""
str_user_s = 0
while str_user != "!":
    str_user = input("Введите строку чисел, разделенных пробелом. Ввод останавливается при наборе '!': ")
    str_user_sp = str_user.split()

    for i in range(len(str_user_sp)):
        try:
            if str_user != "!":
                str_user_s += float(str_user_sp[i])
        except ValueError:
            if str_user_sp[i] != "!":
                print(str_user_sp[i] + ' не является числом')
            else:
                str_user = str_user_sp[i]
    print (str_user_s)

# Задача 6

def int_func(sl):
    return sl.title()

sl = input('Введите несколько слов из маленьких латинских букв: ')
sl_sp = sl.split()
for i in range(len(sl_sp)):
    print (int_func(sl_sp[i]) + ' ', end = "")
