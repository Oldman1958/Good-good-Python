"""
На автомойку в течение квартала заезжали машины. Их гос. номера фиксировались в журнале, следующим образом (пример):

Е220СК
А120МВ
В101АА
Е220СК
А120МВ

В программе уже реализовано чтение этих строк и сохранение в списке:

lst_in = list(map(str.strip, sys.stdin.readlines()))

На основе этого списка через генератор множеств сформировать еще один список уникальных машин.
На экран вывести число уникальных машин.
"""

import sys

lst_in = set(list(map(str.strip, sys.stdin.readlines())))

print(len(lst_in))