"""
На вход программе подается строка. Необходимо ее прочитать и найти в ней все индексы строкового фрагмента "ра".
Выведите найденные индексы на экран в одну строчку через пробел.
Если же фрагмент "ра" отсутствует в строке, то вывести -1.
"""
s = input()
if not 'ра' in s:
    print(-1)
else:
    for i in range(len(s) - 1):
        if s[i] == 'р' and s[i + 1] == 'а':
            print(i, end=' ')
