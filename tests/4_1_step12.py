"""
Работа светофора для пешеходов запрограммирована следующим образом:
в начале каждого часа в течение трех минут горит зеленый сигнал,
затем в течение двух минут – красный, в течение трех минут – опять зеленый и т. д., процесс повторяется.

На вход программе подается вещественное число t, означающее время в минутах, прошедшее с начала очередного часа.
Необходимо прочитать это число и определить, сигнал какого цвета горит для пешеходов в момент времени t
(прочитанного из входного потока). На экран вывести сообщение (без кавычек):

 "green" - для зеленого;
 "red" - для красного.
"""
t = float(input())
q = t % 5
if q <= 3:
    print('green')
else:
    print('red')
