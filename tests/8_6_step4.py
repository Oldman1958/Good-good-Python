"""
Подвиг 2.
Используя менеджер контекста with, откройте файл с именем 'diagnostics.csv' на чтение в кодировке UTF-8,
расположенный в текущем рабочем каталоге.

С помощью конструкции try/except выполните обработку ошибки FileNotFoundError
на случай отсутствия открываемого файла.
При возникновении ошибки установите значение переменной success_open_file в False.
В противном случае значение этой переменной должно быть равно True.

Прочитайте из файла первые две строки и сохраните прочитанные строки в переменных header и row соответственно.

P.S. На экран ничего выводить не нужно.
"""

try:
    with open('diagnostics.csv', encoding='utf-8') as file:
        header = file.readline()
        row = file.readline()
except FileNotFoundError:
    success_open_file = False
