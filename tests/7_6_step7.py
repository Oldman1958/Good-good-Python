"""
На вход программе подаются два целых числа a и b (a < b), записанные в одну строчку через пробел.
Необходимо их прочитать и сформировать список lst из целых чисел в диапазоне от a до b (включительно) с шагом 1,
используя функцию range, оператор [] и оператор распаковки *. Вывести полученный список на экран командой:

print(*lst)
"""

a, b = (map(int, input().split()))
d = [*range(a, b+1)]
print(*d)
