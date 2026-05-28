"""
Подвиг 6.
Используя менеджер контекста with,
откройте файл с именем 'course_text.txt' на чтение в кодировке 'windows-1251',
расположенный в подкаталоге python текущего рабочего каталога.
С помощью конструкции try/except выполните обработку ошибки FileNotFoundError
на случай отсутствия открываемого файла.

Необходимо выполнять чтение данных из файла 'course_text.txt',
пока не встретится первое слово 'python' (в любом регистре).
Файловая позиция при этом должна останавливаться на букве 'p'.
То есть, само слово 'python' должно оставаться непрочитанным.

P.S. На экран ничего выводить не нужно.
"""

try:
    with open('python/course_text.txt', encoding='windows-1251') as file:
        text_file = file.read()
        position = text_file.lower().find("python")
        file.seek(position)

except FileNotFoundError:
    ...