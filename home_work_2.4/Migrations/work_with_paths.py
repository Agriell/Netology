# Домашнее задание к лекции 2.4 «Работа с путями»
#
# Задача №1
# Нужные для работы файлы и заготовка кода находятся на GitHub.
#
# Представьте, что вам нужно отыскать файл в формате sql среди десятков других,
# при этом вы знаете некоторые части этого файла (на память или из другого источника).
#
# Программа ожидает строку, которую будет искать (input()).
# После того, как строка введена, программа ищет её во всех файлах, выводит имена
# найденных файлов построчно и выводит количество найденных файлов.
# Программа снова ожидает ввод, но теперь поиск происходит только среди отобранных
# на предыдущем этапе файлов.
# Программа снова ожидает ввод.
# ...
# Выход из программы программировать не нужно. Достаточно принудительно ее
# останавливать, для этого можно нажать Ctrl + C. Для получения списка всех
# файлов используйте стандартные функции из os и os.path.
#
# Пример на настоящих данных:
#
#       python3 find_procedure.py
#       Введите строку: INSERT
#       ... большой список файлов ...
#       Всего: 301
#       Введите строку: APPLICATION_SETUP
#       ... большой список файлов ...
#       Всего: 26
#       Введите строку: A400M
#       ... большой список файлов ...
#       Всего: 17
#       Введите строку: 0.0
#       Migrations/000_PSE_Application_setup.sql
#       Migrations/100_1-32_PSE_Application_setup.sql
#       Всего: 2
#       Введите строку: 2.0
#       Migrations/000_PSE_Application_setup.sql
#       Всего: 1
# Не забываем организовывать собственный код в функции.
#
# Задача №2. Дополнительная (не обязательная)
#
# Генерировать абсолютный путь до папки с миграциями. Скрипт при этом лежит в
# одной папке с папкой 'Migrations', но запускать мы его можем из любой
# директории - он будет работать корректно.

import os
import os.path


def full_path():
    return os.path.abspath(os.path.dirname(__file__))


def create_files_list():
    """return [list] with file names with .sql expansion"""
    lst = os.listdir(full_path())
    files = []
    for i in lst:
        j = i.split('.')
        if j[len(j)-1] == 'sql':
            files.append(os.path.join(full_path(), i))
    return files


def check_input(file_name, input_data_rez):
    """return file_names, input_data_rez in content"""
    with open(file_name, 'r') as file:
        content = file.read()
    return file_name, input_data_rez in content


def search_filter(searching_files_list, input_data_rez):
    temp_list = []
    for file in searching_files_list:
        # print(check_input(file, input_data_rez))
        search_result = check_input(file, input_data_rez)
        if search_result[1]:
            print(search_result[0])
            temp_list.append(search_result[0])
    return temp_list


def start():
    searching_files_list = create_files_list()
    while True:
        input_data_rez = input('Введите строку поика: ')
        searching_files_list = search_filter(searching_files_list, input_data_rez)
        print('Всего найдено {} файлов\n'.format(len(searching_files_list)))


start()
