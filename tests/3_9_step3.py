"""
В программе объявлен следующий список:

lst = [5.4, 6.7, 10.4]
На вход программе подаются целые числа, записанные через пробел.
Необходимо прочитать эти числа и сохранить в отдельном списке digs.
Добавить в конец списка lst список digs отдельным элементом (как вложенный).
Результирующий список lst вывести на экран командой:

print(lst)
"""
lst = [5.4, 6.7, 10.4]
digs = list(map(int, input().split()))
lst.append(digs)
print(lst)
