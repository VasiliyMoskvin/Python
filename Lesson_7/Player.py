__author__ = "Москвин Василий"

class Player:
    """
    Класс игрока
    """
    def __init__(self, name, card):
        """
        Инициализация игрока
        :param name: имя
        :param card: его карта
        """
        self.name = name
        self.card = card
        self.count_numbers = 15  # Количество незачёркнутых цифр на карте

    def reduce_count_numers(self):
        """
        Уменьшает количество незчёркнутых цифр на единицу
        :return: изменяет self.count_numbers
        """
        self.count_numbers -= 1

    def __str__(self):
        """
        Вывод информации об игроке на экран
        :return: информация об игроке (имя и его карта)
        """
        return "{}\n{}".format(self.name, self.card)