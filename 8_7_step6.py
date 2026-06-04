"""
Подвиг 4.
Используя менеджер контекста with,
откройте файл 'log_stats.txt' в подкаталоге work_data на чтение и дозапись в текстовом режиме
с кодировкой UTF-8.
Добавьте в файл строку:

msg = input()

и прочитайте самую первую строчку из файла в переменную header.

P.S. На экран ничего выводить не нужно.
"""

msg = input()
try:
    with open('work_data/log_stats.txt', 'a+', encoding='utf-8') as file:
        file.write(msg)
        file.seek(0)
        file.readline()
except:
    ...