"""
Игра лото
"""
from random import choice
import Card
import Player
from ErrorCard import ErrorCard

__author__ = "Москвин Василий"

def initial_game(player_name):
    """
    Инициализация игры. Создание двух игроков: пользователь и компьютер.
    :param player_name: имя пользователя
    :return: запуск игры
    """
    print("Игра началась!")
    card_player = Card.Card()
    card_computer = Card.Card()
    player = Player.Player(player_name, card_player)
    computer = Player.Player("Computer", card_computer)
    get_stat(player, computer)
    start_game(player, computer)

def start_game(player, computer):
    """
    Запуск игры
    :param player: игрок пользователь
    :param computer: игрок компьютер
    :return: завершение игры
    """
    for i in gen_number():  # Из мешка достали номер
        print("Из мешка достали бочёнок под номером {}".format(i))
        check_computer(computer, i)  # Проверка карточки компьютера
        get_stat(player, computer)  # Вывод на экран карточек пользователя и компьютера
        ans = input("Хотите зачеркнуть число {} в своей карточке (n - нет)".format(i))  # Хотите зачеркнуть число?
        if ans != "n":  # Если да, то
            try:  # Пытаюсь зачеркнуть число в карточке пользователя
                player.card.remove_number(i)
            except ErrorCard:  # Если числа нет, то пользователь проиграл
                print("Такой цифры {} у вас в карте нет. Вы проиграли".format(i))
                get_stat(player, computer)
                break  # Выход из игры
            else: # Если число есть в карточке, то
                player.reduce_count_numers()  # уменьшаю счётчик незачёркнутых числе в карточке на единицу
        else:  # Если пользователь не хочет зачёркивать число, то
            if player.card.check_card(i):  # проверяю карточку пользователя на наличие числа
                print("У игрока {} есть число {} в карте. Вы проиграли".format(player.name, i)) # Если число есть, то
                get_stat(player, computer)  # пользователь проиграл
                break  # Выход из игры
        if player.count_numbers == 0 and computer.count_numbers == 0:  # Если у пользователя и компьютера одновременно
            get_stat(player, computer)
            print("Ничья!")  # закончились числа на карточке, то это ничья
            break  # Выход из игры
        if player.count_numbers == 0:  # Если у пользователя закончились числа на карточке, то пользователь победил
            get_stat(player, computer)
            print("Игрок {} победил".format(player.name))
            break  # Выход из игры
        elif computer.count_numbers == 0:  # Если у компьютера закончились числа на карточке, то компьютера победил
            get_stat(player, computer)
            print("Игрок {} победил".format(computer.name))
            break  # Выход из игры

def check_computer(computer, i):
    """
    Проверка игрока-компьютера на наличие выпавшего числа в карточке
    :param computer: объект игрок-копьютер
    :param i: выпавшее число
    :return: если выпавшее число есть в карточке, то оно зачёркивается
    """
    for j in computer.card.card:
        for k in j:
            if k == str(i):
                computer.card.remove_number(i)
                computer.reduce_count_numers()

def gen_number():
    """
    Генератор выпадающих из мешка числел
    :return: номер бочонка из мешка
    """
    lst = [i for i in range(1, 91)]
    while True:
        if len(lst) == 0:
            raise StopIteration
        element = choice(lst)
        lst.remove(element)
        yield str(element)

def get_stat(player, computer):
    """
    Возвращает статистику игры: имя игроков и их карточки
    :param player: объект игрок-пользователь
    :paraym computer: объект игрок-компьютер
    :return: имя игроков и их карточки
    """
    print(player)
    print(computer)

while True:
    ans = input("Do you want to play? (n - to exit)\n")
    if ans == "n":
        break
    else:
        ans = input("Enter your name. \n")
        initial_game(ans)

