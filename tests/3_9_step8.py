"""
В программе объявлен следующий вложенный список из трех строк:

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
На вход программе подается строка, содержащее одно слово.
Необходимо прочитать это слово и реализовать проверку на наличие его в списке t.
Результат (булево True или False) вывести на экран.
Решить задачу необходимо без применения условного оператора.
"""
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]
word = input()
out = []
for i in t:
    out += i


print(word in out)
