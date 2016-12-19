from random import randint
from ErrorCard import ErrorCard

__author__ = "Москвин Василий"

class Card:
    """
    Класс карты
    """
    def __init__(self):
        """
        Инициализация карты
        """
        self.num_in_card = self.gen_numbers()  # Все чисел на карте
        self.card = self.get_card()  # Числа и пробелы на карте


    def get_card(self):
        """
        Возвращает карту
        :return: карта
        """
        lst = []
        for i in range(3):  # Заполняю строки карты
            lst.append(self.get_string(i))  # Получить и добавить строку на карту
        return lst

    def get_string(self, index):
        """
        Формирует строку с соответствующим порядковым номером
        :param index: порядковый номер строки в карте
        :return: сформированная строка
        """
        lst = [str(i) for i in self.num_in_card[index]]
        lst_index = self.get_index_in_string()
        for i in range(10):
            if i in lst_index:
                continue
            else:  # Если индекс i должен быть пустым,
                lst.insert(i, " ")  #  то записываю пробел
        return lst

    def get_index_in_string(self):
        """
        Возвращает индексы в строке, которые должны быть заполнены цифрами
        :return: индексы в строке, которые должны быть заполнены числами
        """
        lst = []
        while True:
            i = randint(1, 9)
            if i not in lst:
                lst.append(i)
            if len(lst) == 5:
                break
        lst.sort()
        return lst

    def gen_numbers(self):
        """
        Получение всех числел на карте
        :return: все числа на карте, сгруппированные по строкам
        """
        in_card = []  # Все числа на карте
        in_string = []  # Все числа в строке
        while True:
            i = randint(1, 90)
            for j in in_card:
                if i in j:
                    break
            else:  # Если i нет в строках,
                if i not in in_string:
                    in_string.append(i)  # то добавляем его к строке
            if len(in_string) == 5:  # Если длина строки равна 5,
                in_string.sort()  # сортируем строку
                in_card.append(in_string)  # добавляем её ко всем числам на карточке
                in_string = []
            if len(in_card) == 3:  # Если сформировано 3 строки,
                break  # выхожу из цикла
        return in_card

    def remove_number(self, i):
        """
        Удаляет номер из карточки
        :param i: номер, который необходимо удалить
        :return: изменённую карточка, на месте i стоит #
        """
        for index, j in enumerate(self.card):
            if i in j:
                self.card[index][j.index(i)] = "#"
                break
        else:  # Если i нет на карте, то
            raise ErrorCard # бросаю ошибку ErrorCard

    def check_card(self, i):
        """
        Проверка карты на наличие i
        :param i: номер, который нужно проверить
        :return: если i есть на карте - True, иначе - False
        """
        for j in self.card:
            if i in j:
                return True
        return False



    def __str__(self):
        """
        Вывод данных карты на печать
        :return: данные карты на печать
        """
        s1 = "---------------------------------------"  # Вопрос: Как корректно вывести карточку на экран, без табуляции
        return "{}\n{}\n{}\n{}\n{}".format(s1, "\t".join(self.card[0]),
                                           "\t".join(self.card[1]), "\t".join(self.card[2]), s1)
