"""
На вход программе подается целое положительное число N.
Необходимо написать рекурсивную функцию с именем get_rec_N,
которая отображает на экране последовательность целых чисел от 1 до N (включительно).
Каждое число выводится с новой строки.

В качестве единственного параметра функция get_rec_N должна принимать числовое значение.
Начальный вызов функции уже дан в программе и выглядит так:

get_rec_N(N)

"""
n = int(input())


def get_rec_N(n):
    if n > 0:
        get_rec_N(n - 1)
        print(n)

get_rec_N(n)
