"""
На вход программе поступают данные в виде набора строк в формате:

ключ1=значение1
ключ2=значение2
...
ключN=значениеN

Ключами здесь выступают целые числа (см. пример ниже).
В программе уже реализовано считывание всех строк и сохранение их в виде списка:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Необходимо преобразовать список lst_in в словарь d (без использования функции dict())
и вывести полученный словарь на экран командой:

print(*sorted(d.items()))
"""

import sys


# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)


lst_out = []

for i in lst_in:
    lst_out.append(i.split('='))

lst_dict = {}

for i in range(len(lst_out)):
    lst_dict[int(lst_out[i][0])] = lst_out[i][1]

print(*sorted(lst_dict.items()))
