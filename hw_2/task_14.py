
#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input('Enter your num: '))
my_pow = 1

while my_pow < num:
    print(f'{my_pow} ')
    my_pow *= 2