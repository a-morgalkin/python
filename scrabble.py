"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение  `k`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `k` для проверки
"""
k = 'ноутбук'

# Введите ваше решение ниже

value = {k:1 for k in 'A, E, I, O, U, L, N, S, T, R'.split(', ')}
value.update({(k,1) for k in 'А, В, Е, И, Н, О, Р, С, Т'.split(', ')})
value.update({(k,2) for k in 'D, G'.split(', ')})
value.update({(k,2) for k in 'Д, К, Л, М, П, У'.split(', ')})
value.update({(k,3) for k in 'B, C, M, P'.split(', ')})
value.update({(k,3) for k in 'Б, Г, Ё, Ь, Я'.split(', ')})
value.update({(k,4) for k in 'F, H, V, W, Y'.split(', ')})
value.update({(k,4) for k in 'Й, Ы'.split(', ')})
value.update({(k,5) for k in 'K'.split(', ')})
value.update({(k,5) for k in 'Ж, З, Х, Ц, Ч'.split(', ')})
value.update({(k,8) for k in 'J, X'.split(', ')})
value.update({(k,8) for k in 'Ш, Э, Ю'.split(', ')})
value.update({(k,10) for k in 'Q, Z'.split(', ')})
value.update({(k,10) for k in 'Ф, Щ, Ъ'.split(', ')})

count = 0
for letter in k:
    count += value.get(letter.upper())

print(count)