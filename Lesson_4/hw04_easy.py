__author__ = "Москвин Василий"
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
print("Задание 1")

from random import randint

start_list = [randint(-100, 100) for _ in range(0, 10)]
finish_list = [i ** 2 for i in start_list]

print(start_list)
print(finish_list)
# Задание-2:
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
print("Задание 2")

list_first = ["apple", "cherry", "banana", "kiwi"]
list_second = ["cherry", "plum", "mango", "banana", "papaya"]
list_result = [i for i in list_first if i in list_second]

print(list_first)
print(list_second)
print(list_result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих след. условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print("Задание 3")

start_list = [randint(-100, 100) for _ in range(0, 10)]
list_result = [i for i in start_list if i % 3 == 0 and i > 0 and i != 4]

print(start_list)
print(list_result)