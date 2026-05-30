"""
Подвиг 3.
Используя менеджер контекста with, откройте файл 'letter.txt' на запись в текстовом режиме
с кодировкой UTF-8 в текущем рабочем каталоге.
Сохраните в файл строку:

msg = input()


P.S. На экран ничего выводить не нужно.
"""
msg = input()
try:
    with open('letter.txt', 'w', encoding='utf-8') as file:
        file.write(msg)
except:
    ...