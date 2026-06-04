"""
Подвиг 3.
Используя менеджер контекста with, откройте файл с именем 'targets.dat' на чтение в кодировке UTF-8,
расположенный в подкаталоге images относительно текущего рабочего каталога.

С помощью конструкции try/except выполните обработку ошибки FileNotFoundError
на случай отсутствия открываемого файла.
Также пропишите еще один except для обработки всех остальных возникающих ошибок.

При возникновении ошибки FileNotFoundError установите значение переменной success_open_file в False.
При возникновении других ошибок установите значение переменной success_file_operations в False.
Начальные значения переменных success_open_file и success_file_operations должны быть равны True.

Прочитайте из файла последнюю строку и результат сохраните в переменной last_row.

P.S. На экран ничего выводить не нужно.
"""


success_open_file = True
success_file_operations = True

try:
    with open('images/targets.dat', encoding='utf-8') as file:
        # file.read()
        last_row = file.readlines()[-1]

except FileNotFoundError:
    success_open_file = False
except:
    success_file_operations = False

