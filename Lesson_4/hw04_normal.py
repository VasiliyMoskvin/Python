__author__ = "Москвин Василий"
# Задание-1:
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
print("Задание 1")

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
line_test = "mtMmEZUOmcq"
pattern = '[A-Z]*([a-z]+)[A-Z]*'
print(re.findall(pattern, line))

list_temp = []
list_res = []
for i, s in enumerate(line):
    if s.isupper() and list_temp != []:
        list_res.append("".join(list_temp[:]))
        list_temp = []
    elif s.islower():
        list_temp.append(s)
    if i == len(line) - 1 and list_temp != []:
        list_res.append("".join(list_temp[:]))
        list_temp = []
print(list_res)


# Задание-2:
# Вывести символы в верхнем регистре, которые окружают ровно два символа в нижнем регистре слева
# и два символа в верхнем регистре справа. Решить задачу двумя способами: с помощью re и без.
# Т.е. из строки "sGAMkgAYEOmHBSQs" нужно получить ['GAM', 'EO']
print("Задание 2")

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
         'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
         'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
         'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
         'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
         'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
         'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
         'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
         'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
         'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
         'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
         'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

line_test = "vAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsn"
# Вопрос: решение через re и без него дают разные ответы. Считаю, что решение без re более корректно даёт ответ.
# Отличием можно увидеть, если проходить по line_test (это часть line_2). Для того, чтобы заменить line_2 на line_test нужно заменить
# Проблема возникает, когда большие буквые являются границами, для длвух шаблонов. т.е. AAbbBBCCbbBBDD. Здесь
# re не обрабатывает CC и соответственно DD (граница второго шаблона) тоже не записывается
pattern = "([A-Z]+)[a-z]{2}[A-Z]{2}([A-Z]+)"
list_res = []
for i in re.findall(pattern, line_2): # здесь line_2 на line_test
    list_res.extend(list(i))  # избавляюсь от кортежей
print(list_res)

list_temp = []
list_res = []
temp = ""
for i, s in enumerate(line_2): # здесь line_2 на line_test
    if s.isupper():
        if len(list_temp) == 0:
            list_temp.append(s)
        elif len(list_temp) == 1:
            list_temp[0] = "{}{}".format(list_temp[0], s)
        elif len(list_temp) == 2:
            if len(list_temp[1]) == 1:
                list_temp = []
                list_temp.append(s)
            elif len(list_temp[1]) == 2 or len(list_temp[1]) == 3:
                list_temp[1] = "{}{}".format(list_temp[1], s)
            else:
                list_temp.append(s)
        elif len(list_temp) == 3:
            list_temp[2] = "{}{}".format(list_temp[2], s)
    elif s.islower():
        if len(list_temp) == 0:
            continue
        elif len(list_temp) == 1:
            list_temp.append(s)
        elif len(list_temp) == 2:
            if len(list_temp[1]) == 1:
                list_temp[1] = "{}{}".format(list_temp[1], s)
            elif len(list_temp[1]) == 3:
                temp = list_temp[1][-1]
                list_temp = []
                list_temp.append(temp)
                list_temp.append(s)
            elif len(list_temp[1]) == 4:
                temp = list_temp[1][2:4]
                list_temp = []
                list_temp.append(temp)
                list_temp.append(s)
            else:
                list_temp = []
        else:
            list_res.append(list_temp[0])
            list_res.append(list_temp[2])
            temp = list_temp[2]
            list_temp = []
            list_temp.append(temp)
            list_temp.append(s)


print(list_res)
# Вопрос: нужно было избавиться от кортежей или правильный результат получен?

# Задача-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла) произвольными целыми
# числами, в результате в файле должно быть 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле.
print("Задание 4")

from random import randint

with open("hw04_normal.txt", "w") as f:  # записываю цифры в файл
    for _ in range(0, 2500):  # Вопрос: почему записывается 2733 числа?
        f.write(str(randint(0, 10)))

file_content = ""
with open("hw04_normal.txt", "r") as f:  # читаю из файла
    file_content = f.read()

print(file_content)
content = re.split(r'(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)', file_content)  # разделяю
# Вопрос: как убрать пробелы через re?
for i in content:  # удалить пустые элементы
    if i == "":
        content.remove("")

index_max = 0
max_length = 0

for i, line in enumerate(content):  # прохожу по списку ищу максимальну длину и индекс этого элемента
    if len(line) > max_length:
        max_length = len(line)
        index_max = i

print(content)
print("max_length={}, index_max={} volume={}".format(max_length, index_max, content[index_max]))
