
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os.path


def create_file_list():  # return [list] with file names

    fullpath = os.path.abspath(os.path.dirname(__file__))
    # print(fullpath)
    migrations = 'Migrations'
    files = glob.glob(os.path.join(fullpath, migrations, "*.sql"))
    return files


def check_input(file_name, input_data_rez):
    with open(file_name, 'r') as file:
        content = file.read()
        if input_data_rez in content:
            marker = True
        else:
            marker = False
    return file_name, marker


def search_filter(searching_files_list, input_data_rez):
    temp_list = []
    for file in searching_files_list:
        # print(check_input(file, input_data_rez))
        search_result = check_input(file, input_data_rez)
        if search_result[1] == True:
            print(search_result[0])
            temp_list.append(search_result[0])
    return temp_list


def start():
    searching_files_list = create_file_list()
    while True:
        input_data_rez = input('Введите строку поика: ')
        searching_files_list = search_filter(searching_files_list, input_data_rez)
        print('Всего найдено {} файлов'.format(len(searching_files_list)))
        print(' ')

start()
