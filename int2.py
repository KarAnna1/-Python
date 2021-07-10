#Задача 1

li = [10, 13.34, 'for all', True, 7j, [2,3], {'a':1, 'b':2}, (True, False)]

for li_i in li:
     print(type(li_i))

#Задача 2

li_u = ''
li = []
num = 0
while li_u.title() != 'Stop' and num < 8:
    li_u = input('Введите значение. Для остановки ввода введите "stop": ')
    if li_u.title() != 'Stop':
        li.append(li_u)
        num += 1

print(li)

li_l = len(li) - len(li) % 2
for n in range(0, li_l , 2):
    li[n], li[n + 1] = li[n + 1], li[n]

print(li)

#Задача 3

month_n = input("Введите номер месяца в году: ")

di = {'зима' : [1,2,12], 'весна' : [3,4,5], 'лето' : [6,7,8], 'осень' : [9,10,11] }
try:
    if int(month_n) < 13 and int(month_n) > 0:
        for di_k, di_v in di.items():
            if int(month_n) in di_v:
                print(f'Вы выбрали сезон {di_k}')
    else:
        print('Такого месяца в году нет')
except ValueError:
    print('Вы ввели не число')

li = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
try:
    int_m = int(month_n)
    if int(month_n) < 13 and int(month_n) > 0:
        print(f'Вы выбрали сезон {li[int(month_n)-1]}')
    else:
        print('Такого месяца в году нет')
except ValueError:
    print('Вы ввели не число')

#Задача 4

srt_user = input("Введите несколько слов, разделенных пробелом: ")
srt_user_sp = srt_user.split(' ')

for sl in enumerate(srt_user_sp):
      print(sl[:10])

#Задача 5

li_nat = [13, 11, 11, 7, 5, 2]
new_n = input('Введите число: ')
try:
    new_n = int(new_n)
except ValueError:
    new_n = 0

i_ind = len(li_nat)
for i in li_nat:
    if i <= new_n:
        i_ind = li_nat.index(i)
        break

li_nat.insert(i_ind, new_n)
print(li_nat)

#Задача 6
str_u = ' '
i = 1
tov = []
while str_u.title() != 'N':
    str_tov = input('Введите через запятую следующие данные: название, цена, количество, единица измерения: ')
    str_u = input('Ввести еще одну строку товара? (Y/N): ')

    str_split = str_tov.split(',')

    while len(str_split) < 4:
        str_split.append('')

    t = (i, {'название': str_split[0].strip(),
             'цена': str_split[1].strip(),
             'количество': str_split[2].strip(),
             'единица': str_split[3].strip()})
    i += 1
    tov.append(t)

print(tov)

tov_an = {'название': [],
          'цена': [],
          'количество': [],
          'единица': []}

for tov_el in tov:
    tov_dic = (tov_el[1])
    for tov_key, tov_zn in tov_dic.items():

        if not (tov_zn in tov_an[tov_key]):
             tov_an[tov_key].append(tov_zn)

print(tov_an)
