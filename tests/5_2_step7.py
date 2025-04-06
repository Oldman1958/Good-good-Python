"""
На вход программе подается строка с именами студентов, записанных в одну строчку через пробел.
Прочитайте эту строку и сформируйте на ее основе список из имен студентов.
Необходимо определить, что в этом списке хотя бы одно имя начинается и заканчивается на ту же самую букву
(без учета регистра). Если это так, то на экран вывести строку "ДА", иначе строку "НЕТ".
Программу реализовать с использованием цикла while и оператора break.
"""
names = list(map(str, input().split()))
i = 0
count = 0
while i < len(names):
    if names[i][0].lower() == names[i][-1]:
        count += 1
        break
    else:
        i += 1
        continue


print("ДА" if count != 0 else "НЕТ")
