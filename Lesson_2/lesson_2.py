# использовать pep-8

s = 'sdhjfk'
if s.isalpha(): # s.isdigit()
    print("Строка символов")

if isinstance(s, str): # Строка относится к типу str
    print("Строка")    # не type(s)==str

#.__doc__ """ """" Описание функции

# типы данных
# изменяемые: словарь, список, множество
# неизменяемы: строка, булево, None, int, кортеж, frozenset

#print("arguments: {0:>10}, {1:<10}, {2:^20}".format(s1,s2,s3)) #<смещение
#print("arguments: %d, %d, %d"%(s1,s2,s3)) # % нужен кортеж

# строки склевивать не очень хорошо, лучше использовать формат
# "{} {}".format(s1,s2) или " ".join((s1, s2)) не s1+s2
s4 = "12345, "
print(s4.isdigit())
s4 = s4.strip(" ,;")
print(s4)

s = u"апорлд" # строка юникодов

#from __future__ import unicode_literals # для второго питона
# вывести данные в строку

for c in s:
    print(c, end=" ")

lst = list(s4) # преобразование строки в список
lst[3:3] = "x" # вставка элемента
lst[3] = 'x' # замена элемента
lst.remove(2) # удаляет, но не возвращает элемент удаляет не по индексу, а по значению
del lst[1]

tup = ([], 1, 2, 3, 4)
tup[0].append(7)

hash(False) == hash(0)

lst = [12,3,2,3,4,23,23,0,1,2,32]
lst = list(set(lst)) # список неповторяющихся элементов