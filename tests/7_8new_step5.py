"""
Подвиг 3.
Продолжите программу, в которой нужно объявить функцию с именем verify_password
и следующими параметрами (порядок следования важен):

psw - строка с паролем; только позиционные аргументы;
chars="@#!*" - один из обязательных символов в пароле; принимает позиционные и именованные аргументы;
min_length=8 - минимальная длина пароля; принимает позиционные и именованные аргументы.
Функция verify_password должна проверять корректность записи пароля psw по следующим критериям:

длина пароля не менее min_length символов;
пароль должен содержать хотя бы один из символов chars="@#!*";
пароль не должен содержать русские буквы (как большие, так и малые) "абвгдеёжзийклмнопрстуфхцчшщьыъэюя".
Если пароль корректен, то функция должна возвращать булево значение True, иначе False.

Например:

res1 = verify_password("fА12fgfhsf") # False
res2 = verify_password("VBNFGfdg!") # True
res3 = verify_password("VBNFGfdg!", min_length=15) # False
res4 = verify_password("VBNFGfdg!9", min_length=7, chars="@#$%^") # False

Вызовите функцию verify_password для проверки пароля:

password = input()

и со значениями параметров:

chars="0123456789"
min_length=10
Результат сохраните в переменной result.
"""


# здесь объявляйте функцию
def verify_password(psw, /, chars="@#!*", min_length=8):
    # Проверка длины пароля
    if len(psw) < min_length:
        return False

    # Проверка наличия хотя бы одного символа из chars
    has_required_char = any(char in psw for char in chars)
    if not has_required_char:
        return False

    # Определение набора русских букв (строчные и прописные)
    russian_letters = "абвгдеёжзийклмнопрстуфхцчшщьыъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"


    # Проверка отсутствия русских букв в пароле
    has_russian_letters = any(char in russian_letters for char in psw)
    if has_russian_letters:
        return False

    # Если все проверки пройдены, возвращаем True
    return True

# Получение пароля от пользователя
password = input()

# Вызов функции verify_password с заданными параметрами и сохранение результата в переменной result
result = verify_password(password, chars="0123456789", min_length=10)

print(result)

