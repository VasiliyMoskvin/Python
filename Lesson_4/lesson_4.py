import os # модуль взаимодействия с ОС
import shutil # модуль доступа к утилитам системы (copy)

print(os.getcwd()) # где я

os.chdir("..") # подняться на уровень выше директорию

ls = os.listdir() # список# содержимого текущей директории

#for i in ls:
#    if os.path.isdir(i):  # если директория
#        print("Dir: ", i)
#    else:
#        shutil.copy(i, i + ".copy") # копирует файлы

#if os.path.exists("test.txt"): # существует ли такой файл
#    print("file exists")
#else:
#    print("No")

#os.mkdir("test-z")
#os.makedirs("test-z\dir\dir1\dir2")
#shutil.rmtree(".\\test-z") # удаляет всё дерево
path_1 = os.path.join("test-z", "dir", "dir1", "dir2") # Обход различных ОС
os.makedirs(path_1)
