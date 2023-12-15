# Минимальная версия python 3.11

from datetime import date
import os, json

tasks_dict = list()
fields=['id', 'date', 'task']

def show_menu():
    #print('\033c', end='') # Очистка экрана
    print('1. Добавить заметку',
          '2. Показать все заметки',
          '3. Показать за определенную дату',
          '4. Изменить запись',
          '5. Удалить запись',
          '6. Закончить работу',"",sep = '\n')

def show_ask_menu():
        print('Внести изменения?',
              '1. Да',
              '2. Нет',"",sep = '\n')

def work_with_tasks():
    global tasks_dict
    tasks_dict = read_txt('tasks.txt')
    while (1):
        show_menu()
        match input():
            case '1': add_new_task()
            case '2': show_all_tasks()
            case '3': show_date_tasks()
            case '4': change_task()
            case '5': delete_task()
            case '6': break

#------------------------------------
#      БЛОК 1 Добавление данных     #
#------------------------------------
def add_new_task():
    global tasks_dict
    data = []
    if (len(tasks_dict) == 0):
        data.append(1) 
    else:
        data.append(tasks_dict[-1]['id'] + 1) 
    data.append(str(date.today())) 
    data.append(input('Введите заметку: ')) 
    tasks_dict.append(dict(zip(fields, data)))
    write_txt('tasks.txt', tasks_dict)

#------------------------------------
#      БЛОК 2 Вывода на экран       #
#------------------------------------
def show_all_tasks():
    if (len(tasks_dict) == 0): 
        print ("Не найдено!")
    else:
        for line in tasks_dict:
            print_one_line(line)

def show_date_tasks():
    data = input('Введите дату: ') 
    for line in tasks_dict:
        if (line["date"] == data):
            print_one_line(line)

def print_one_line(line):
    print(json.dumps(line))

#------------------------------------
#       БЛОК 4 Редактирование       #
#------------------------------------
def change_task():
    show_all_tasks()
    change_one_task(input("Введите номер записи которую хотите изменить: "))

def change_one_task(index):
    line = try_to_find(index)
    if (line):
        line["task"] = input("Введите новую запись: ")
        write_txt('tasks.txt', tasks_dict)
    else: print ('Такой записи нет.')

def try_to_find(index):
    for line in tasks_dict:
        if line["id"] == int(index): return line
    return {}


#------------------------------------
#       БЛОК 5 Удалить запись       #
#------------------------------------
def delete_task():
    show_all_tasks()
    delete_one_line(input("Какую запись будем удалять?: "))

def delete_one_line(index):
    line = try_to_find(index)
    if (line):
        print_one_line(line)
        show_ask_menu()
        match input():
            case '1': tasks_dict.remove(line)
            case '2': return 
        write_txt('tasks.txt', tasks_dict)
    else: print('Такой записи нет.')

#------------------------------------
#       БЛОК Работы с файлом        #
#------------------------------------
def read_txt(filename):
    with open(filename) as d:
        return json.load(d)

def write_txt(filename , tasks_dict):
    with open(filename,'w',encoding='utf-8') as tsk:
        tsk.write(json.dumps(tasks_dict))

#------------------------------------
#       СТАРТ ОСНОВНОЙ ПРОГРАММЫ    #
#------------------------------------
work_with_tasks()