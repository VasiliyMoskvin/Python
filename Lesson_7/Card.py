from random import randint
from ErrorCard import ErrorCard


class Card:
    def __init__(self):
        self.num_in_card = self.gen_numbers()
        self.card = self.get_card()


    def get_card(self):
        lst = []
        for i in range(3):
            lst.append(self.get_string(i))
        return lst

    def get_string(self, index):
        lst = [str(i) for i in self.num_in_card[index]]
        lst_index = self.get_index_in_string()
        for i in range(10):
            if i in lst_index:
                continue
            else:
                lst.insert(i, " ")
        return lst

    def get_index_in_string(self):
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
        in_card = []
        in_string = []
        while True:
            i = randint(1, 90)
            for j in in_card:
                if i in j:
                    break
            else:
                if i not in in_string:
                    in_string.append(i)
            if len(in_string) == 5:
                in_string.sort()
                in_card.append(in_string)
                in_string = []
            if len(in_card) == 3:
                break
        return in_card

    def remove_number(self, i):
        for index, j in enumerate(self.card):
            if i in j:
                self.card[index][j.index(i)] = "#"
                break
        else:
            raise ErrorCard

    def check_card(self, i):
        for j in self.card:
            if i in j:
                return True
        return False



    def __str__(self):
        s1 = "---------------------------------------"
        return "{:<}\n{:<}\n{:<}\n{:<}\n{:<}".format(s1, " ".join(self.card[0]),
                                           " ".join(self.card[1]), " ".join(self.card[2]), s1)
