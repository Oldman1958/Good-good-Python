"""
На вход программе поступают номера телефонов с привязкой к именам в виде строк следующего формата:

номер_1 имя_1
номер_2 имя_2
...
номер_N имя_N

В программе уже реализовано считывание всех строк и сохранение их в виде списка:

lst_in = list(map(str.strip, sys.stdin.readlines()))
На основе списка lst_in необходимо создать словарь d, где ключами будут имена,
а значениями - список номеров телефонов для этого имени (ключа).
Обратите внимание, что одному имени может принадлежать несколько разных номеров.
Полученный словарь вывести командой:

print(*sorted(d.items()))
"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

a = [i.split() for i in lst_in]

d = {}

for i in range(len(a)):
    key = a[i][1]
    val = a[i][0]

    if key not in d:
        d[key] = []
        d[key].append(val)
    else:
        d[key].append(val)

print(*sorted(d.items()))

"""
Здесь более оптимальное, но не мое решение.
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}

for i in lst_in:
    value, key = i.split()
    if key in d:
        d[key] += [value]
    else:
        d[key] = [value]

print(*sorted(d.items()))
"""
