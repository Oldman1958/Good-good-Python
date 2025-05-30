"""
Объявите функцию, которая принимает строку с кириллицей (и другими символами) и преобразовывает русские буквы в латиницу,
используя следующий словарь для замены русских букв на соответствующее латинское написание:

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
Функция должна возвращать преобразованную строку.
Замены делать без учета регистра (переданную строку перевести в нижний регистр - малые буквы).

Определите декоратор с параметром chars и начальным значением " !?",
который данные символы преобразует в символ "-" и, кроме того,
все подряд идущие дефисы (например, "--" или "---") приводит к одному дефису.
Полученный результат должен возвращаться в виде строки.

Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите декорированную функцию для строки s:

s = input()
Результат работы декорированной функции отобразите на экране.
"""
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def send_param_decorator(chars=" !?"):
    def decorator(func):
        def wrapper(s):
            out = func(s)
            # Заменяем указанные символы на дефисы
            for c in chars:
                out = out.replace(c, '-')
            # Сводим подряд идущие дефисы к одному
            while '--' in out:
                out = out.replace('--', '-')

            return out

        return wrapper

    return decorator


@send_param_decorator(chars="?!:;,. ")
def cyr_2_latin(s):
    res = ''
    s = s.lower()
    for i in s:
        if i in t:
            res += t[i]
        else:
            res += i
    return res


str_in = input()

print(cyr_2_latin(str_in))
