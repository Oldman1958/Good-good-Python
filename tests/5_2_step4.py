"""
Объявите в программе следующий одномерный список длиной 10 элементов, состоящий из нулей:

p = [0] * 10
На каждой итерации цикла запрашивайте у пользователя ввод целого числа - индекс элемента списка p,
по которому записывается значение 1, если ее там еще нет.
Если же 1 уже проставлена по текущему индексу, то список не менять.
Необходимо расставить так пять единиц в списке p. После этого цикл прерывается.

Программу реализовать с помощью цикла while и с использованием оператора continue,
когда 1 уже проставлена в списке по текущему индексу, чтобы запросить другой индекс.
Результат вывести на экран в виде последовательности чисел, записанных через пробел.
"""

p = [0] * 10
count = 0
while count < 5:
    i = int(input())
    if p[i] == 0:
        p[i] = 1
        count += 1
    else:
        continue
print(*p)
