# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# 
# Помогите Кате отгадать задуманные Петей числа.

nun_1 = int(input('Enter First num: '))
nun_2 = int(input('Enter Second num: '))

Summ = nun_1 + nun_2
Multi = nun_1 * nun_2

print(f'{Summ = }, {Multi = }')

kate_num_1 = 1
kate_num_2 = Summ - kate_num_1

while (kate_num_1 * kate_num_2) != Multi:
    kate_num_1 += 1
    kate_num_2 = Summ - kate_num_1
    
print(f'{kate_num_1 = },{kate_num_2 = }')