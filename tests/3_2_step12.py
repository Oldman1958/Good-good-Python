"""
На вход программе подается строка, состоящая из двух слов, записанных через пробел. Длина первого слова меньше второго.
Необходимо прочитать строку, выделить из нее слова и обрезать второе слово до длины первого.
Полученное (обрезанное) слово выведите в консоль (на экран).
"""
s = input().split()
print(s[1][len(s[0])])
