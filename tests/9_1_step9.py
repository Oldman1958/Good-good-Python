"""
Используя символы малых букв латинского алфавита (строка ascii_lowercase):

from string import ascii_lowercase

запишите генератор, который бы возвращал все возможные сочетания из двух букв латинского алфавита.
Выведите первые 50 сочетаний на экран в строку через пробел.

Например, первые семь начальных сочетаний имеют вид:

aa ab ac ad ae af ag
"""


from string import ascii_lowercase

# Генератор, возвращающий все возможные сочетания из двух букв латинского алфавита
combinations = (a + b for a in ascii_lowercase for b in ascii_lowercase)

# Получаем первые 50 сочетаний
first_50 = [next(combinations) for _ in range(50)]

# Выводим их в строку через пробел
print(' '.join(first_50))
