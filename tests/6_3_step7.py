"""
 На вход программе подается строка с названиями городов, записанных через пробел.
 Необходимо прочитать эту строку и на ее основе сформировать кортеж из названий городов.
 Затем, выполните проверку: если в полученном кортеже присутствует город "Ульяновск",
 то этот элемент следует удалить (создав новый кортеж).
 Выведите на экран названия городов из итогового кортежа (по порядку) в одну строчку через пробел.
"""


towns = tuple(map(str, input().split()))

if 'Ульяновск' in towns:
    res = list(towns)
    res.remove('Ульяновск')
    print(*res)
else:
    print(*towns)
