while True:
    try:
        a = int(input('input a > '))
        b = int(input('input b > '))
        if a >= 0 and b >= 0: break
        print('a and b must be natural or zero, try again...')
    except KeyboardInterrupt:
        print('\njust input numbers...')
    except ValueError:
        print('\nit is not an integer, try again...')
    except:
        print('\nunknown error, try again...')

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
raise_ = lambda a, b: a * raise_ (a, b - 1) if b > 0 else 1
print(f'{a} в степени {b} равно: {raise_(a, b)}')

# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
sum_ = lambda a, b: (sum_(a-1, b) + 1 if a >= b else sum_(a, b-1) + 1) if a > 0 or b > 0 else 0
print(f'{a} плюс {b} равно: {sum_(a, b)}')