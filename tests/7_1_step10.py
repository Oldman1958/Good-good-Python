"""
Объявите в программе функцию с одним параметром,
которая проверяет корректность переданного ей email-адреса в виде строки.
Полагается, что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы могут принимать
значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит "ДА", иначе "НЕТ".

После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.
"""
import string


def check_email(email):
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '_@.'
    if '@' not in email or '.' not in email:
        return 'НЕТ'
    else:
        for i in email:
            if i not in all_chars:
                return 'НЕТ'
        return 'ДА'



print(check_email(input()))
