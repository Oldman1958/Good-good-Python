"""
На вход программе подаются следующие данные (каждое с новой строки):

курс доллара (вещественное значение);
число рублей (целое число) для обмена рублей на доллары.
Необходимо прочитать эти данные и вычислить целое количество получаемых долларов (с отбрасыванием дробной части) и сформировать строку, по шаблону:

"Вы можете получить <долларов>$ за <число рублей> рублей по курсу <курс доллара>"

Вывести полученную строку на экран (без кавычек).
"""
current = float(input())
n = int(input())
print(f'Вы можете получить {int(n // current)}$ за {n} рублей по курсу {current}')
