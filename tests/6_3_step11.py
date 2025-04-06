"""
Объявите в программе следующий двумерный кортеж, размером 5 x 5 элементов:

t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
На вход программе подается натуральное число N (N < 5).
Необходимо на основе кортежа t сформировать новый аналогичный кортеж t2 размером N x N элементов
путем отбрасывания последних строк и столбцов.
Результат выведите на экран в виде таблицы чисел.

P.S. Обратите внимание, что в при выводе таблицы в конце строк не должно быть пробелов.
"""

t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

n = int(input())

t2 = tuple()

for i in range(n):
    t2 += (t[i][:n],)

for i in t2:
    print(*i)
