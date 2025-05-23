"""
На вход программе подается целое число: текущее время (секунды) в диапазоне [0; 59].
Необходимо его прочитать и вычислить следующее за ним значение в секундах с учетом границ диапазона [0; 59].
То есть, если прочитанное значение равно 59, то следующее должно быть равно 0. И так по кругу.

Реализуйте программу с помощью тернарного условного оператора. Результат (следующее значение) отобразите на экране.

P.S. Попробуйте также реализовать эту же задачу с использованием только арифметических операций.
"""
n = int(input())
print(n + 1 if n < 59 else 0)
