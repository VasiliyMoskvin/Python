__author__ = "Москвин Василий"
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) - в Linux начинается с /, в Windows с имени диска
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь. Исходной директорией считать ту,
# в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp():
    if not dir_name:
        print("Необходимо указать имя копируемого файла")
        return
    if os.path.exists(dir_name):
        shutil.copy(dir_name, "copy_{}".format(dir_name))
        if os.path.exists("copy_{}".format(dir_name)):
            print("Копия файла {} успешно создана".format(dir_name))
    else:
        print("Файла {} не существует".format(dir_name))


def rm():
    if not dir_name:
        print("Необходимо указать имя удаляемого файла")
        return
    if os.path.exists(dir_name):
        agry = input("Вы точно хотите удалить файл {}? (y - удалить)".format(dir_name))
        if agry == "y":
            if os.path.isdir(dir_name):
                shutil.rmtree(dir_name)
                if not os.path.exists(dir_name):
                    print("Директория {} удалена".format(dir_name))
            elif os.path.isfile(dir_name):
                os.remove(dir_name)
                if not os.path.exists(dir_name):
                    print("Файл {} удалён".format(dir_name))
        else:
            print("Файл {} не удалён".format(dir_name))
    else:
        print("Файла {} не существует".format(dir_name))


def cd():
    if not dir_name:
        print("Необходимо указать имя директрории, куда необходимо перейти")
        return
    dir_name_abs = dir_name
    if dir_name_abs[1:2] != ":\\": # Вопрос: как узнать версиюо ОС, чтобы сделать программу кросплатформенной?
        dir_name_abs = os.path.abspath(dir_name_abs) # os.uname() не работает
    if os.path.exists(dir_name_abs):
        os.chdir(dir_name_abs)
    else:
        print("Такого пути не существует {}".format(dir_name_abs))



def ls():
    print(os.path.abspath("."))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
