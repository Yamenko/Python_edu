# «адача 32: ќпределить индексы элементов массива (списка), 
# значени€ которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

inp_min = int(input('Min: '))
inp_max = int(input('Max: '))

# —оздание списка всех элементов которые нужно проверить
# ѕроверка если пользователь не знает какое число меньше и больше ))
if inp_min > inp_max:
    inp_min, inp_max = inp_max, inp_min

# ѕроверка границ (обрезаем ненужное)
if inp_min < min(lst): inp_min = min(lst)
if inp_max > max(lst): inp_max = max(lst)

# —оздаем список дл€ проверки
lst_enter = [*range(inp_min, inp_max)]

# ќсновной цикл программы
lst_indx = []
for i in range(len(lst)):
    if lst[i] in lst_enter:
        lst_indx.append(i)

print(lst_indx)

