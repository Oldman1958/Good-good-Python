"""
Гражданин 1 января открыл счет в банке, вложив 1000 руб.
Каждый год размер вклада увеличивается на 5% от имеющейся суммы.
Определить сумму вклада через n лет (n - целое положительное число, читаемое из входного потока).
Результат (сумму вклада) округлить до сотых и вывести на экран. Программу реализовать при помощи цикла while.
"""
c = 1000
n = int(input())
i = 0
while i < n:
    c *= 1.05
    i += 1
print(round(c, 2))
