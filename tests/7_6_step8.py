"""
На вход программе подаются вещественные числа и следующей строкой названия городов, записанные через пробел.
Необходимо прочитать числа, сохранить их в виде списка.
Затем, прочитать строку с названиями городов и сформировать на ее основе еще один список.
После этого сформировать единый список lst, в котором сначала идут числа, а затем, названия городов.

Объединение списков реализовать с использованием оператора распаковки *. Вывести полученный список lst на экран командой:

print(*lst)
"""

lst1 = list(map(float, input().split()))
lst2 = list(map(str, input().split()))
lst = (*lst1, *lst2)
print(*lst)
