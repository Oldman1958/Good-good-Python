"""
На вход программе подается строка с названиями городов, записанных в одну строчку через пробел.
Необходимо прочитать эту строку и сформировать список из названий городов.
Затем, перебрать полученный список циклом for и заменить названия городов на длины их строк.
Результат вывести на экран в виде последовательности чисел через пробел в одну строчку.
"""
towns = list(map(str, input().split()))
out = []
for i in range(len(towns)):
    out.append(len(towns[i]))

print(*out)
