"""
Подвиг 2.
Продолжите программу, в которой нужно объявить функцию с именем most_popular
и следующими параметрами (порядок следования важен):

people - список строк из имен людей; должен принимать позиционные и именованные аргументы;
case_sens=False - флаг учета регистра букв (малые или большие) при обработке строк (по умолчанию значение False);
должен принимать только именованные аргументы.

Функция most_popular должна находить наиболее часто встречающееся имя в списке people.
Если установлен флаг case_sens=True, то при поиске должен учитываться регистр букв, иначе регистр не учитывается.
Функция должна возвращать кортеж вида:

(<найденное имя>, <частота встречаемости>)

Например, для списка:

celebrities = ['Толстой', 'Балакирев', 'Пушкин', 'Бердяев', 'Балакирев', 'Пушкин', 'Толстой', 'пушкин']

Вызов функции:

result = most_popular(celebrities)

должен возвращать кортеж:

('пушкин', 3)

Вызовите функцию most_popular со списком writers и значением параметра case_sens равным True.
Результат сохраните в переменной result.

Задачу следует реализовать, используя только текущие знания, без применения каких-либо внешних библиотек.

P.S. На экран ничего выводить не нужно.
"""


# здесь объявляйте функцию
def most_popular(people, *, case_sens=False):
    # Создаём рабочий список: если case_sens=False, приводим все имена к нижнему регистру
    if not case_sens:
        processed_people = [name.lower() for name in people]
    else:
        processed_people = people

    # Словарь для подсчёта частоты встречаемости имён
    name_counts = {}
    for name in processed_people:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

    # Находим имя с максимальной частотой
    most_popular_name = None
    max_count = 0
    for name, count in name_counts.items():
        if count > max_count:
            max_count = count
            most_popular_name = name

    return most_popular_name, max_count


# здесь продолжайте программу

# Вызов функции со списком writers и case_sens=True, сохранение результата в переменной result
writers = input().split()

result = most_popular(writers, case_sens=True)
# result = most_popular(writers)

# print(result)
