"""
На вход программе подается строка с номером телефона. Ожидается следующий формат номера в строке:

+7(xxx)xxx-xx-xx

где x - это любая цифра.
Число введенных символов считается верным (то есть не может быть, чтобы отсутствовала какая-либо цифра или была лишняя).
Необходимо прочитать строку из входного потока и проверить, что она содержит номер телефона в соответствии с приведенным
форматом.
Вывести "ДА", если это так и "НЕТ" в противном случае.


Ниже мое решение, оно правильное, но оно без использования enumerate.

num = input()
stamp = '+7(xxx)xxx-xx-xx'
res = 'ДА'
for i in range(len(stamp)):
    if stamp[i] == 'x' and num[i].isdigit():
        continue
    elif stamp[i] != 'x' and stamp[i] == num[i]:
        continue
    else:
        res = 'НЕТ'
        break
print(res)

Далее решение с использованием enumerate.
"""

s = '+7(xxx)xxx-xx-xx'
n = input().rjust(len(s))
for i, item in enumerate(n):
    if s[i] == item or s[i] == 'x' and item.isdigit():
        continue
    print('НЕТ')
    break
else:
    print('ДА')
