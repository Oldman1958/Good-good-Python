"""
Объявите функцию, которая имеет один параметр, принимающий строку.
Функция должна возвращать два значения в виде кортежа: переданную строку и ее длину.

После объявления функции далее в программе прочитайте из входного потока строку с названиями городов,
записанных через пробел.
Сформируйте на основе прочитанной строки список cities из названий городов.
Затем, используя генератор словарей и ранее объявленную функцию, сформируйте на основе списка cities словарь d в формате:

d = {<город 1>: <число символов>, ..., <город N>: <число символов>}

Выведите этот словарь в порядке возрастания длин строк с помощью команд:

a = sorted(d, key=d.get)
print(*a)
"""


def get_str(s):
    return s, len(s)


cities = input().split()
d = dict(get_str(i) for i in cities)

a = sorted(d, key=d.get)
print(*a)
