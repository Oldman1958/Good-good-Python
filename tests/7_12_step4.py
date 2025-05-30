"""
Объявите функцию, которая переводит символы строки в нижний регистр (малые буквы) и возвращает результат.
Определите декоратор для этой функции, который имеет один параметр tag,
определяющий строку с названием тега и начальным значением "h1".
Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.

Пример заключения строки "python" в тег h1:

<h1>python</h1>

Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для строки s,
прочитанной из входного потока:

s = input()
Результат работы декорированной функции отобразите на экране.
"""


def get_tag(tag='h1'):
    """Функция декоратор, принимающая и передающая далее параметр tag"""

    def func_decorator(func):
        """Функция декоратор, принимающая ссылку на вызываемую функцию"""

        def wrapper(s):
            """Функция обертка вызывающая переданную функцию и добавляющая в нужные места тэги"""
            res = f'<{tag}>{func(s)}</{tag}>'
            return res

        return wrapper

    return func_decorator


@get_tag(tag='dev')      # Передаем в декоратор параметр - тэг dev
def get_lower(s):
    res = s.lower()
    return res


s = input()
d = get_lower(s)
print(d)
