"""
На вход программе подается строка из двух слов, записанных через пробел. Необходимо прочитать эту строку и вычислить
следующие булевы значения:

для оператора in (проверки вхождения первого слова во второе);
для оператора == (сравнения двух слов);
для оператора > (сравнение на больше первого слова со вторым);
для оператора < (сравнение на меньше первого слова со вторым).

Все булевы значения объединить в одну строку через пробел и вывести на экран в порядке их перечисления в задании
подвига.
"""
w1, w2 = map(str, input().split())
print(w1 in w2, w1 == w2, w1 > w2, w1 < w2)
