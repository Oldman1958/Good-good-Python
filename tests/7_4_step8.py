"""
В функцию из предыдущего подвига 5 добавьте в конец еще один третий формальный параметр up
с начальным булевым значением True.
Если параметр up равен True, то тег, указанный в формальном параметре tag, следует записывать заглавными буквами,
а иначе малыми.

После объявления функции далее в программе прочитайте из входного потока строку
и дважды вызовите функцию (с выводом результата ее работы на экран):
первый раз со строкой и именованным аргументом tag со значением 'div';
второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up со значением False.
"""


def is_tag(s, tag='h1', up=True):
    if up:
        tag = tag.upper()
    return f"<{tag}>{s}</{tag}>"


tag = 'div'

s = input()
print(is_tag(s, tag))
print(is_tag(s, tag, up=False))
