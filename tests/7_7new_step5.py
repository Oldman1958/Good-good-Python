"""
Подвиг 3.
Продолжите программу, в которой нужно объявить функцию с именем count_chars
и следующими параметрами (порядок следования важен):

s - строка с текстом; принимает позиционные и именованные аргументы;
chars - строка с символами; принимает позиционные и именованные аргументы;
return_type=tuple - определяет возвращаемый тип данных (по умолчанию кортеж); принимает только именованные аргументы;
ignore_case=True - флаг учета регистра букв (малые или большие) при обработке строк (по умолчанию значение True);
принимает только именованные аргументы.
Функция count_chars должна находить частоты встречаемости символов chars в строке s.
Если установлен флаг ignore_case=True, то при поиске регистр букв учитываться не должен, иначе регистр учитывается.
Функция должна возвращать коллекцию, тип данных которой указан в параметре return_type,
и с частотами встречаемости символов chars в строке s (в порядке их следования).

Например, для строки:

msg = "Python is an easy to learn, powerful programming language."

Вызов функции:

fr = count_chars(msg, "aouvei", return_type=list, ignore_case=False)

должен возвращать следующий список:

[6, 4, 2, 0, 4, 2]

Вызовите функцию count_chars со строкой text, набором символов symbols и следующими значениями параметров:

return_type должен быть равен set;
ignore_case должен быть равен False.
Результат сохраните в переменной result.

Задачу следует реализовать, используя только текущие знания, без применения каких-либо внешних библиотек.

P.S. На экран ничего выводить не нужно.
"""


# здесь объявляйте функцию

def count_chars(s, chars, *, return_type=tuple, ignore_case=True):
    if ignore_case:
        processed_s = s.lower()
        processed_chars = chars.lower()
    else:
        processed_s = s
        processed_chars = chars

    out = []
    for i in processed_chars:
        out.append(processed_s.count(i))

    # Преобразуем результат в требуемый тип данных
    if return_type == list:
        result_collection = out
    elif return_type == tuple:
        result_collection = tuple(out)
    elif return_type == set:
        # При преобразовании в set порядок теряется, но это соответствует типу данных
        result_collection = set(out)
    else:
        # Если передан неизвестный тип — возвращаем кортеж по умолчанию
        result_collection = tuple(out)

    return result_collection


# здесь продолжайте программу
text = input()
symbols = input()

result = count_chars(text, symbols, return_type=set, ignore_case=False)

print(result)

"""
Python is an easy to learn, powerful programming language.
aouvei
"""
