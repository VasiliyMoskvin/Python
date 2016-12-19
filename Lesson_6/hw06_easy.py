__author__ = "Москвин Василий"
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    """
   Класс построения треугольника
   """

    def __init__(self, points):
        """
       Инициализация треугольника по трём точкам
       :param points: словарь точек {a:[x, y], ...}
       """
        self.a = points["a"]
        self.b = points["b"]
        self.c = points["c"]
        self.points = dict(a=self.a, b=self.b, c=self.c)
        self.length_side = dict(c=self.get_length(self.a, self.b),  # Словарь значений длин сторон
                                b=self.get_length(self.a, self.c),  # a - сторона, лежащая против точки a
                                a=self.get_length(self.b, self.c))
        self.angles = dict(a=self.get_angle("a"),  # Словарь значений углов в треугольнике
                           b=self.get_angle("b"),  # a - угол, ледащий при вершине a
                           c=self.get_angle("c"))

    def get_length(self, a, b):
        """
       Возвращает длину стороны межту точками a и b
       :param a: первая точка
       :param b: вторая точка
       :return: длина стороны ab
       """
        ab = list(map(lambda x, y: (x - y) ** 2, a, b))
        return math.sqrt(ab[0] + ab[1])

    def get_angle(self, x):
        """
       Возвращает угол при вершине x. Формула расчёта: acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
       :param x:  вершина треугольника
       :return: угол при вершине треугольника
       """
        if x == "a":
            a = self.length_side["a"]
            b = self.length_side["b"]
            c = self.length_side["c"]
        elif x == "b":
            a = self.length_side["b"]
            b = self.length_side["c"]
            c = self.length_side["a"]
        elif x == "c":
            a = self.length_side["c"]
            b = self.length_side["a"]
            c = self.length_side["b"]
        return (180 / math.pi) * math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))

    def perimeter(self):
        """
       Возвращает величину периметра треугольника
       :return: перметр треугольника
       """
        per = 0
        for key in self.length_side.keys():  # Вопрос: ломал голову, как реализовать эту функцию через встроенные функции
            per += self.length_side[key]  # map, zip, итд. Но ничего не пришлов голову. Как можно это сделать?
        return per  # Мне кажется, что это возможно

    def height(self, x):
        """
       Возвращает высоту треугольника, исходящую из вершины x
       :param x: вершина, откуда исходит высота
       :return: высота треугольника, исходящия из вершины x
       """
        if x == "a":
            return self.length_side["b"] * math.sin((math.pi / 180) * self.angles["c"])
        elif x == "b":
            return self.length_side["c"] * math.sin((math.pi / 180) * self.angles["a"])
        elif x == "c":
            return self.length_side["a"] * math.sin((math.pi / 180) * self.angles["b"])
        else:
            print("Нет такого ключа {}".format(x))

    def square(self):
        """
       Возвращает величину площади треугольника по формуле s = sqrt(p(p - a)(p - b)(p - c)) p = (a + b + c) / 2
       :return: величина площади треугольника
       """
        per = self.perimeter() / 2
        return math.sqrt(per * (per - self.length_side["a"])
                         * (per - self.length_side["b"]) * (per - self.length_side["c"]))

    def square_h(self, x):
        """
       Возвращает величину площди треугольника по формуле s = 0.5 * a * h, где основание треугольника
       :param x: вершина, из которой исходит высота
       :return: площадь треугольника
       """
        return 0.5 * self.length_side[x] * self.height(x)


my_points = {"a": [-1, 0], "b": [0, 3], "c": [2, 0]}
tr = Triangle(my_points)
print("Задание 1")
print("Площадь треугольника s = {}".format(tr.square()))
print("Высоты треугольника из вершин: a = {}, b = {}, c = {}".format(tr.height("a"), tr.height("b"), tr.height("c")))
print("Периметр треугольника p = {}".format(tr.perimeter()))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.

class TrapezoidIso:
    def __init__(self, points):
        """
        Инициализация трапеции по 4-м точкам, формата {'a':[x, y], ...}
        Здесь же вычисляются углы и диагонали трапеции
        :param points: словарь точек, по которым строется трапеция. Формат: {'a':[x, y], ...}
        """
        self.points = dict(a=points["a"], b=points["b"], c=points["c"], d=points["d"])
        self.length_side = dict(a=self.get_length(self.points["a"], self.points["b"]),  # Словарь значений длин сторон
                                b=self.get_length(self.points["b"], self.points["c"]),  # a - сторона, исходящая из a
                                c=self.get_length(self.points["c"], self.points["d"]),
                                d=self.get_length(self.points["d"], self.points["a"]))
        self.angels = dict()
        self.get_angels()
        self.diagonal = self.get_diagonal()

    def get_length(self, a, b):
        """
        Возвращает длину стороны межту точками a и b
        :param a: первая точка
        :param b: вторая точка
        :return: длина стороны ab
        """
        ab = list(map(lambda x, y: (x - y) ** 2, a, b))
        return round(math.sqrt(ab[0] + ab[1]), 5)

    def get_angels(self):
        """
        Заполняет словарь значений углов трапеции
        """
        self.angels["a"] = round(self.get_angel(self.points["a"], self.points["b"]), 5)
        self.angels["b"] = round(180 - self.angels["a"] + self.get_angel(self.points["c"], self.points["b"]), 5)
        self.angels["d"] = round(math.fabs(self.get_angel(self.points["d"], self.points["c"])), 5)
        self.angels["c"] = round(360 - self.angels["a"] - self.angels["b"] - self.angels["d"], 5)

    def get_angel(self, a, b):
        """
        Вычисляет угол наклона прямой ab
        :param a: первая точка прямой ab
        :param b: вторая точка прямой ab
        :return: угол наклона прямой ab
        """
        try:
            tang = (b[1] - a[1]) / (b[0] - a[0])
        except ZeroDivisionError:
            tang = math.inf
        res = math.atan(tang) * (180 / math.pi)
        return res

    def get_diagonal(self):
        """
        Возвращает кортеж величин диагоналей трапеции. Необходима для проверки равнобедренности трапеции
        :return: кортеж величин диагоналей трапеции
        """
        d1 = round(math.sqrt(self.length_side['c'] ** 2 + self.length_side['d'] ** self.length_side['b'] - (
            (self.length_side['d'] * (self.length_side['c'] ** 2 - self.length_side['a'] ** 2)) / (
                self.length_side['d'] - self.length_side['b']))), 5)
        d2 = round(math.sqrt(self.length_side['a'] ** 2 + self.length_side['d'] ** self.length_side['b'] - (
            (self.length_side['d'] * (self.length_side['c'] ** 2 - self.length_side['a'] ** 2)) / (
                self.length_side['d'] - self.length_side['b']))), 5)

        return d1, d2

    def get_height(self):
        """
        Возвращает величину высоты трапеции. Необходима для вычисления площади трапеции
        :return: выста трапеции
        """
        return round(self.length_side["c"] * math.sin((math.pi / 180) * self.angels["a"]), 5)

    def is_isosceles(self):
        """
        Возвращает True, если трапеция равнобедренная. И False в противном случае
        :return: истинность равнобедренности трапеции
        """
        if self.angels['a'] == self.angels['d']:  # В одну строчку условие показалось очень громоздким, но так тоже не
            if self.angels['b'] == self.angels['c']:  # очень
                if self.diagonal[0] == self.diagonal[1]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def perimeter(self):
        """
        Возвращает значение величины периметра трапеции
        :return: периметр трапеции
        """
        per = 0
        for key in self.length_side.keys():
            per += self.length_side[key]
        return round(per, 5)

    def square(self):
        """
        Возвращает значение величины площади трапеции
        :return: площадь трапеции
        """
        return round(((self.length_side['b'] + self.length_side['d']) / 2) * self.get_height(), 5)


my_points = {"a": [-5, 0], "b": [-3, 3], "c": [3, 3], "d": [5, 0]}
tr = TrapezoidIso(my_points)

print("Задание 2")
if tr.is_isosceles():
    print("Трапеция равнобочная")
else:
    print("Трапеция не равнобочная")

for key in tr.length_side.keys():
    print("Сторона {} длиной {}".format(key, tr.length_side[key]))

print("Периметр трапеции равен {}".format(tr.perimeter()))
print("Площадь трапеции {}".format(tr.square()))
