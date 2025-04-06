"""
На вход программе подается строка из русских букв и символов пробела.
Необходимо ее прочитать и закодировать азбукой Морзе, где каждой букве ставится в соответствие код из точки и тире.
После каждой закодированной буквы должен стоять пробел (символ окончания кода буквы).
После последнего кода пробела быть не должно (в конце строки).
"""
st = input().upper()
d = {' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-',
     'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
     'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----',
     'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}

for i in st:
    for k, v in d.items():
        if i in k:
            print(v, end=' ')
