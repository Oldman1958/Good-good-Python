"""
Объявите в программе функцию без параметров, которая читает из входного потока (с клавиатуры) имя и фамилию,
записанные в одну строку через пробел, и выводит на экран сообщение (без кавычек):

"Уважаемый, <имя> <фамилия>! Вы верно выполнили это задание!"

После объявления вызовите эту функцию.
"""


def print_message():
    name, fam = input().split()
    print(f"Уважаемый, {name} {fam}! Вы верно выполнили это задание!")


print_message()
