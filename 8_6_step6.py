"""
Подвиг 4.
Используя менеджер контекста with, откройте файл с именем 'bank.csv' на чтение в кодировке UTF-8,
расположенный в текущем рабочем каталоге.
С помощью конструкции try/except выполните обработку ошибки FileNotFoundError
на случай отсутствия открываемого файла.

Файл 'bank.csv' содержит первую строку с названием полей и последующие строки с данными.
Разделителем между данными выступает запятая.
Например:

education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,deposit
secondary,no,2343,yes,no,unknown,5,may,1042,1,-1,0,unknown,yes
secondary,no,45,no,no,unknown,5,may,1467,1,-1,0,unknown,yes
secondary,no,1270,yes,no,unknown,5,may,1389,1,-1,0,unknown,yes
...


Необходимо прочитать из файла 'bank.csv' первые две строки и на их основе сформировать словарь row_data вида:

row_data = {'поле_1': 'значение_1', 'поле_2': 'значение_2', ...}

Для приведенного выше примера словарь row_data будет иметь вид:

row_data = {'education': 'secondary', 'default': 'no', 'balance': '2343', ...}


Обратите внимание, что в ключах и значениях словаря не должно быть символов переноса строки '\n'.
Все прочие символы должны оставаться без изменений.

P.S. На экран ничего выводить не нужно.
"""

import csv

row_data = {}

try:
    with open('bank.csv', encoding='utf-8') as file:
        # Создаём объект для чтения CSV‑файла
        csv_reader = csv.reader(file, delimiter=',')

        # Читаем первую строку — заголовки полей
        headers = next(csv_reader)

        # Читаем вторую строку — данные первой записи
        first_data_row = next(csv_reader)

        # Формируем словарь: сопоставляем заголовки с соответствующими значениями
        row_data = dict(zip(headers, first_data_row))

except FileNotFoundError:
    success_open_file = False

