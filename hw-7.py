# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. # Фразы отделяются друг от друга пробелами.  

vowels = 'аяуюоеёэиы' + 'аяуюоеёэиы'.upper()
inp = 'пара-ра-рам рам-пам-папам па-ра-па-да'

# --- solution one ---
count = set()
for phrases in inp.split():
    count.add(sum(phrases.count(ch) for ch in vowels))
rithm = len(count) == 1
print('Парам пам-пам' if rithm else 'Пам парам')

# --- solution two ---
rithm = len(set(map(lambda ph:sum(ph.count(ch) for ch in vowels), inp.split()))) == 1
print('Парам пам-пам' if rithm else 'Пам парам')

# --- solution three ---
out = ''.join([ch for ch in inp if ch in vowels + ' '])
rithm = len(set(map(len, out.split()))) == 1
print('Парам пам-пам' if rithm else 'Пам парам')


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        print(*list(operation(row, col) for col in range(1, num_columns + 1)))

print_operation_table(lambda x, y: x * y)
