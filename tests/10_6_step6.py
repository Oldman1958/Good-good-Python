"""
Подвиг 4.
Имеется следующий фрагмент программы с функцией parse_json и словарем json_data:

def parse_json(data):
    match data:
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}


С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон для выделения значения ключа access
с проверкой на тип bool и для выделения даты (первое значение списка) из поля data с проверкой,
что data является списком.
Возвратите выделенные два значения в виде кортежа в формате (access, date).

P. S. В программе нужно только дописать шаблон. Вызывать функцию не нужно.
"""
from os import access


def parse_json(data):
    match data:
        # здесь прописывайте шаблон
        case {'access': access, 'data': [date, *_]} if isinstance(access, bool) and isinstance(data['data'], list):
            return access, date

        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
                return ids, login

    return None

"""
Подробное объяснение добавленного шаблона:
{'access': access, 'data': [date, *_]} — шаблон для сопоставления структуры словаря:
{'access': access} — ищем ключ 'access' и сохраняем его значение в переменную access;
'data': [date, *_] — ищем ключ 'data', значение которого должно быть списком. 
Извлекаем первый элемент списка (date), остальные элементы игнорируем с помощью *_.
if isinstance(access, bool) — дополнительная проверка типа: убеждаемся, что значение по ключу 'access' 
имеет тип bool (True/False).
isinstance(data['data'], list) — проверяем, что значение поля 'data' действительно является списком.
return access, date — возвращаем найденные значения в виде кортежа (access, date).
"""

json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
