"""
На вход программе подается строка, содержащая названия городов, записанных через пробел.
Необходимо прочитать эту строку и на ее основе сформировать список lst из названий городов,
добавив в его конец список cities:

cities = ["Москва", "Тверь", "Вологда"]
 Выведите полученный список lst на экран командой:

print(*lst)
"""
cities = ["Москва", "Тверь", "Вологда"]
new_cities = input().split()
print(*(new_cities + cities))
