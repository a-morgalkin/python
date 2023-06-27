# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def find_sum_digits(number):
    ''' (int) -> int
    
    Return sum of digits of number. 

    Precondition: number >= 0
    >>> find_sum_digits(123)
    6
    '''
    return 0 if number == 0 else number % 10 + find_sum_digits (number//10) 

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no
def is_happy_number(number):
    ''' (int) -> bool

    Return True if sum of first 3 digits equals sum of second 3 digits.
    Else return False.

    Precondition: number consists 6 digits
    >>> is_happy_number(385916)
    True
    >>> is_happy_number(123456)
    False
    '''
    return find_sum_digits(number // 1000) == find_sum_digits(number % 1000)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

def zhuravliki(count):
    ''' (int) -> list of int
    
    Return list of integer, where list[0] - quantity made by Petya, 
    list[1] - Katya, list[2] - Seryozha. Return an empty list 
    if the has no solutions in integers.
    >>> zhuravliki(6)
    [1, 4, 1]
    >>> zhuravliki(24)
    [4, 16, 4]
    '''
    return [] if count % 6 != 0 else [count // 6, count // 6 * 4, count // 6]

# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
def is_choco_bar_devided(n, m, k):
    ''' (int, int, int) -> bool

    Return True if a chocolate bar is divided for k pieces by on motion.
    Else return False.

    Precondition: 0 < k < m * n
    >>> is_choco_bar_devided(3, 2, 4)
    True
    >>> is_choco_bar_devided(3, 2, 1)
    False
    '''
    return (k % n == 0 or k % m == 0) and (k < m * n)

# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным.
def is_big_year(year):
    ''' (int) -> bool

    >>> is_big_year(2016)
    True
    >>> is_big_year(2000)
    True
    >>> is_big_year(1900)
    False
    '''
    return year % 4 == 0 and not (year % 100 == 0 and year % 400 !=0)
