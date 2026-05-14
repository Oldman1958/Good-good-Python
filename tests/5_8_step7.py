"""
Подвиг 5.
На вход программе подается натуральное число N.
Необходимо его прочитать и сгенерировать вложенный список с помощью list comprehension, размером N x N,
где первая строка содержала бы все нули, вторая - все единицы, третья - все двойки и так до N-й строки.
Результат вывести в виде таблицы чисел как показано в примере ниже.

4

0 0 0 0
1 1 1 1
2 2 2 2
3 3 3 3
"""

n = int(input())
"""
Классический вариант решения
result = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(i)
    result.append(row)
"""

#  вариант с list omprehension
result = [[i for j in range(n)] for i in range(n)]


for row in result:
    print(*row)
