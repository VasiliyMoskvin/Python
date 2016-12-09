__author__ = "Москвин Василий"
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# print("Задание 1")

import os
import shutil
import sys

__author__ = "Москвин Василий"


def cr_dir(dir_name):
    try:
        os.mkdir(dir_name)
        if os.path.exists(dir_name):
            print("Каталог {} создан".format(dir_name))
    except OSError:
        print("Каталог с именем \'{}\' уже существует".format(dir_name))


def create_dir():
    for i in range(1, 10):
        cr_dir("dir_{}".format(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_this_dir():
    for i in os.listdir():
        if __name__ == '__main__': # В этом задании функция выводит список каталогов
            if os.path.isdir(i):
                print(i)
        else: # В задании normal выводит и каталоги и файлы
            print(i)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_this_file():
    shutil.copy(sys.argv[0], "copy_{}".format(sys.argv[0].split("/")[-1])) # создаю файл 'copy_название-файла'

if __name__ == '__main__':
    create_dir()
    list_this_dir()
    copy_this_file()
