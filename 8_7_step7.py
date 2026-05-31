"""
Подвиг 6.
Используя менеджер контекста with, откройте два файла 'text_1' и 'text_2' на чтение в кодировке UTF-8,
расположенные в подкаталоге lib.
С помощью конструкции try/except выполните обработку ошибки FileNotFoundError
на случай отсутствия любого из открываемых файлов.

Если файлы успешно открыты на чтение, прочитайте из них все данные с пропуском первой строки.
После этого запишите в файл 'text_all.txt' в кодировке Windows-1251
сначала прочитанные данные из файла 'text_1', а затем, с новой строки,
данные из файла 'text_2'.
Итоговый файл 'text_all.txt' должен располагаться в текущем рабочем каталоге.

P.S. На экран ничего выводить не нужно.
"""

try:
    with open('lib/text_1', encoding='utf-8') as file1, open('lib/text_2', encoding='utf-8') as file2, open('text_all.txt', 'w',encoding='Windows-1251' ) as file3:
        f1, f2 = file1.readlines()[1:] ,file2.readlines()[1:]
        file3.writelines(f1)
        file3.write('\n')
        file3.writelines(f2)
except FileNotFoundError:
    pass