__author__ = "Москвин Василий"
# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers"). Рассчитайте зарплату всех работников,
# зная что они получат полный оклад, если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают удвоенную ЗП,
# пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора каждый работник получал строку из файла

from decimal import Decimal


class Employees:
    """
    Класс работников
    """

    def __init__(self, name, surname, std_salary, profession, norma_hours):
        """
        Инициализация работника
        :param name: имя
        :param surname: фам
        :param std_salary: стандартная зарплата, оклад
        :param profession: профессия
        :param norma_hours: норма часов
        """
        self.name = name
        self.surname = surname
        self.std_salary = std_salary
        self.profession = profession
        self.norma_hours = norma_hours
        self.hours_in_this = 0  # Отработанные часы в этом месяце

    def add_hours_in_this(self, hours_in_this):
        """
        Добавляет количество часов, отработанные в этом месяце
        :param hours_in_this: количество часов, отработанные в этом месяце
        :return: изменяет значение self.hours_in_this
        """
        self.hours_in_this = hours_in_this

    def salary_in_this_month(self):
        """
        Возвращает зарплату в этом месяце. Если недоработка - зарплата уменьшается пропорционально
        отработанному времени. Если норма - зарплата стандартная. Если переработка - зарплата увеличиваеся,
        двойная оплата переработанных часов
        :return: зарплата в этом месяце
        """
        if self.hours_in_this == self.norma_hours:
            return self.std_salary
        elif self.hours_in_this < self.norma_hours:
            return (self.std_salary / self.norma_hours) * self.hours_in_this
        else:
            return self.std_salary + \
                   2 * (self.std_salary / self.norma_hours) * (self.hours_in_this - self.norma_hours)

    def __str__(self):
        """
        Отображение класса на печати
        :return: класс на печати
        """
        return "{} {} {} {} {} {}".format(self.name, self.surname, self.std_salary,
                                          self.profession, self.norma_hours, self.hours_in_this)


list_employees = []
with open('data\\workers', 'r', encoding='utf-8') as f:  # Заполняю список данных работников
    for i, line in enumerate(f):
        if i != 0:
            person = line.split()
            obj = Employees(person[0], person[1], Decimal(person[2]), person[3], Decimal(person[4]))  # Вопрос: Как
            list_employees.append(obj)  # можно сократить запись? От person[...] в глазах рябит.:-)

with open('data\\hours_of', 'r', encoding='utf-8') as f:  # Заполняю данные о проделанной работе в этом месяце
    for i, line in enumerate(f):
        if i != 0:
            person = line.split()
            for j in list_employees:
                if j.name == person[0] and j.surname == person[1]:  # Если имя и фамилия совпадают,
                    j.add_hours_in_this(Decimal(person[2]))  # то это искомый работник
                    break
            else:
                print("Нет в списке работников этого чеовека {} {} {}".format(person[0], person[1]))

for i in list_employees:
    print("{} {} \t получит в этом месяце {} вместо {}. "
          "т.к. он отработал {} из {} часов".format(i.name, i.surname, i.salary_in_this_month(), i.std_salary,
                                                    i.hours_in_this, i.norma_hours))
