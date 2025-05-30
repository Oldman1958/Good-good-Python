"""
На вход программе подается строка, в которой записано арифметическое выражение. Например:

"10 + 25 - 12"

или

"10 + 25 - 12 + 20 - 1 + 3"

и т. д. То есть, количество действий может быть произвольным.

Необходимо прочитать эту строку из входного потока и выполнить вычисление, записанного в ней арифметического выражения. Результат вычисления отобразить на экране.

Полагается, что в качестве арифметических операций используется только сложение (+) и вычитание (-), а в качестве операндов только целые неотрицательные числа. Следует учесть, что математические операции могут быть записаны как с пробелами (до и после), так и без них.

P.S. В целях обучения программу следует делать без использования функции eval.
"""
exp = input().replace(' ', '')
summ = 0

for val in exp.split('+'):
    for i, v in enumerate(val.split('-')):
        if i == 0:
            summ += int(v)
        else:
            summ -= int(v)

print(summ)

# Я решил с использованием eval
# print(eval(input()))
#
#
# Это другой вариант решения
#
# n = input().replace(' ', '')
# s = ''
# for i in n:
# 	if i.isdigit():
# 		s += i
# 	else:
# 		s += ' ' + i + ' '
# s = s.split()
#
# total = int(s[0])
# for i in range(1, len(s) , 2 ):
# 	if s[i] == '+':
# 		total += int(s[i + 1])
# 	else:
# 		total -= int(s[i+1])