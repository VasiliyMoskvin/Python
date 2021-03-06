__author__="Москвин Василий"
# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True
# Вопрос: Чему была равна переменная a, если точно известно, что её значение не изменялось?

import math             # Подключение библиотеки math, чтобы использовать inf
a = math.inf            # Присвоение бесконечности переменной a

print(a == a ** 2)      # Вывод результата на экран
print(a == a * 2)       # Вывод результата на экран
print(a > 999999)       # Вывод результата на экран