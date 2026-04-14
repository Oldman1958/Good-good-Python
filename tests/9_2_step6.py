"""
Подвиг 4.
На вход программе подается натуральное число N, которое необходимо прочитать и сохранить через переменную.
Используя строки из латинских букв ascii_lowercase и ascii_uppercase:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase


объявите функцию-генератор с одним параметром max_size,
которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной max_size = N символов.
Например, при N=6 адрес может выглядеть так: SCrUZo@mail.ru

Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно.
Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).

Подсказка:
для формирования случайного индекса для выбора символа из строки chars, используйте функцию randint модуля random:

import random
random.seed(1)
indx = random.randint(0, len(chars)-1)
"""

from string import ascii_lowercase, ascii_uppercase
import random

# Устанавливаем seed для воспроизводимости результатов (как в подсказке)
random.seed(1)

# Формируем строку допустимых символов
chars = ascii_lowercase + ascii_uppercase

# Читаем входное число N
N = int(input())


# Объявляем функцию‑генератор для создания e-mail
def email_generator(length):
    while True:  # Бесконечный цикл — генератор будет работать бесконечно
        # Создаём email: выбираем length случайных символов из chars
        email = ''.join(
            chars[random.randint(0, len(chars) - 1)]
            for _ in range(length)
        )
        yield f'{email}@mail.ru'  # Возвращаем сгенерированный пароль и приостанавливаем выполнение


# Создаём экземпляр генератора для длины N
gen = email_generator(N)

# Генерируем и выводим первые пять email-ов, каждый с новой строки
for _ in range(5):
    print(next(gen))
