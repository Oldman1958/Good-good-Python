"""
На вход программе подается список целых чисел, записанных в одну строчку через пробел.
Необходимо их прочитать и сохранить в виде списка.
Затем, с помощью словаря выделите только уникальные (не повторяющиеся) числа.
Сформируйте из них еще один список (уникальных чисел). Числа в этом списке должны идти в том же порядке,
что и при чтении (из входного потока). Выведите уникальные числа на экран в одну строчку через пробел.

P. S. Такая задача, обычно решается через множества, но мы их еще не проходили, поэтому воспользуемся словарем.
"""

lst_in = input().split()                            # Пользовательский ввод
unic_number = {}                                    # Создаю словарь
for value in lst_in:
    if value not in unic_number:                    # Если значения нет в словаре
        unic_number[value] = value                  # Добавляю в словарь ключи и значение
print(*[value for value in unic_number.values()])   # Перебираем список и выводим значение
