"""
Подвиг 5.
Объявите функцию-генератор, которая бы возвращала простые числа.
(Простое число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.
"""
import sympy
from sympy import isprime


def simple_number():
    for i in range(1000):
        if isprime(i):
            yield i

gen = simple_number()
for _ in range(20):
    print(next(gen), end=' ')
