"""
Объявите в программе функцию, которая имеет один параметр - вес предмета, и выводит на экран сообщение (без кавычек):

"Предмет имеет вес: x кг."

где x - переданное значение (аргумент) функции. После объявления функции прочитайте (с помощью функции input)
вещественное число и вызовите функцию с этим числовым значением.
"""


def weight_message(w):
    print(f"Предмет имеет вес: {w} кг.")


x = float(input())
weight_message(x)
