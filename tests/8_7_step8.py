"""
Подвиг 7.


P.S. На экран ничего выводить не нужно.
"""

try:
    # Открываем оба файла для чтения
    with open('lang_doc/python_base.dat', 'r', encoding='UTF-8') as f1, \
            open('lang_doc/java_base.dat', 'r', encoding='UTF-8') as f2:

        # Читаем содержимое обоих файлов
        content_python = f1.read()
        content_java = f2.read()
    # Открываем эти два файла для записи и меняем их содержимое местами
    with open('lang_doc/python_base.dat', 'w', encoding='utf-8') as f1, \
            open('lang_doc/java_base.dat', 'w', encoding='utf-8') as f2:
        f1.write(content_java)
        f2.write(content_python)
except FileNotFoundError:
    pass