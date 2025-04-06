"""
Объявите в программе функцию с именем check_password, которая первым параметром принимает строку (пароль)
и имеет второй формальный параметр chars с начальным значением в виде строки "$%!?@#".
Функция должна проверять, есть ли в пароле хотя бы один символ из chars и что длина пароля не менее 8 символов.
Если проверка проходит, то функция возвращает булево True, иначе False.

P. S. Вызывать функцию не нужно, только объявить.
"""


def check_password(psw, chars="$%!?@#"):
    return all([any([i in psw for i in chars]), len(psw) > 7])

print(check_password('12345678!'))