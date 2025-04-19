"""
Имеется программа (см. листинг ниже).
Необходимо в теле функции func2 дописать команду, которая бы меняла значение уже существующей переменной msg,
объявленной в функции func1.
"""


def func1():
    msg = input()

    def func2():
        nonlocal msg
        msg = input()
        print(msg)

    func2()
    print(msg)


func1()
