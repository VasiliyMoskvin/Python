__author__="Москвин Василий"
#Вопрос: где правильнее вставлять эту строку (__autor__...)?

# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
print("Задание 1")

fruits = ["яблоко", "банан", "киви", "арбуз"]
counter = 1
for one in fruits:
    print("{}.{:>10}".format(counter, one))
    counter += 1
# Подсказка: использует метод .format()

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.
print("Задание 2")

from random import randint
list_1 = [randint(1, 15) for i in range(0, randint(1, 20))]
list_2 = [randint(1, 15) for i in range(0, randint(1, 20))]


print("Было")
print(list_1)
print(list_2)

for i in list_2:
    if i in list_1:
        while i in list_1: # т.к. может быть несколько одинаковых элементов в списке, то...
            list_1.remove(i)

print("Стало")
print(list_1)
print(list_2)
# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("Задание 3")

list_1 = [randint(1, 15) for i in range(0, randint(1, 20))]
list_2 = []

for i in list_1:
    if i % 2 == 0:
        list_2.append(i / 4)
    else:
        list_2.append(i * 2)

print(list_1)
print(list_2)