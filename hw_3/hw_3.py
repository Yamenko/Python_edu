﻿#Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
#Найдите количество и выведите его.

#list_1 = [1, 2, 3, 4, 5]
#k = 3
#i = 0
#for elem in list_1:
#    if elem == k: i += 1

#print (i)




#Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

#list_1 = [1, 2, 3, 4, 7]
#k = 6

#list_1.append(k)        # Добавили элемент в это список
#list_1.sort()           # Отсортировали
#index = list_1.index(k) # Нашли индекс нашего элемента в списке

#if index == (len(list_1) - 1) or (k - list_1[index - 1]) <= (list_1[index + 1] - k):
#    print(list_1[index - 1])
#else:
#    print(list_1[index + 1])


### SCRABLE ###

symbol_cost = {
    'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 'Р':1, 'С':1, 'Т':1,
    'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2,
    'Б':3, 'Г':3, 'Ё':3, 'Ь':3, 'Я':3,
    'Й':4, 'Ы':4,
    'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5,
    'Ш':8, 'Э':8, 'Ю':8,
    'Ф':10, 'Щ':10, 'Ъ':10,
    'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 
    'D':2, 'G':2, 
    'B':3, 'C':3, 'M':3, 'P':3, 
    'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 
    'K':5,
    'J':8, 'X':8,
    'Q':10, 'Z':10
    }

def count_mass(my_str) -> int:
    if len(my_str) <= 0: return 0
    
    my_str = my_str.upper()
    count = 0
    for sym in my_str:
        count += symbol_cost[sym]
    return count

print(count_mass(k))







