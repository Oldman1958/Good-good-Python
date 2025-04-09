"""
Объявите в программе функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
На вход этой функции передаются N длин сторон через ее аргументы. Дополнительно могут быть указаны именованные аргументы:

tp - булево значение True/False;
color - целое числовое значение;
closed - булево значение True/False;
width - вещественное значение.

Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров
в порядке их перечисления в тексте задания (если они были переданы).
Если какой-либо параметр отсутствует, его возвращать не нужно (пропустить).

P.S. Функцию выполнять не нужно, только объявить.
"""


def get_data_fig(*N, **kwargs):
    """
    get_data_fig(*N)
    N - длины сторон многоугольника
    **kwargs
        type - булево значение True/False
        color - целое числовое значение
        closed - булево значение True/False
        width - целое значение
    """
    perimetr = sum(N)
    t = (perimetr,)
    if "tp" in kwargs:
        typ_e = kwargs["tp"]
        t += (typ_e,)
    if "color" in kwargs:
        color = kwargs["color"]
        t += (color,)
    if "closed" in kwargs:
        closet = kwargs["closed"]
        t += (closet,)
    if "width" in kwargs:
        width = kwargs["width"]
        t += (width,)
    return t


"""
Строки ниже это тест на работоспособность функции, их отправлять не надо.
print(get_data_fig(1, 2, 3, 4, 3, 2, 4))                         # [19]
print(get_data_fig(1, 2, 3, 4, 3, 2, 4, color='green'))          # [19, 'green']
print(get_data_fig(1, 2, 3, 4, 3, 2, 4, color='green', tp=True)) # [19, True, 'green']
"""

