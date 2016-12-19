__author__ = "Москвин Василий"
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Learner:
    """
    Класс ученика
    """

    def __init__(self, name, surname, otchestvo, father, mather, classroom):
        """
        Инициализация ученика
        :param name: имя
        :param surname: фамилия
        :param otchestvo: отчество
        :param father: ФИО отца
        :param mather: ФИО матери
        :param classroom: учебный класс
        """
        self.name = name
        self.surname = surname
        self.otchestvo = otchestvo
        self.father = father
        self.mather = mather
        self.classroom = classroom

    def get_classroom(self):
        """
        Возвращает учебный класс ученика
        :return: учебный класс ученика
        """
        return self.classroom.classrooms

    def get_all_subjects(self):
        """
        Возвращает список всех предметов ученика в формате: Ученик --> Класс --> Учителя --> Предметы
        :return: список всех предметов ученика в формате: Ученик --> Класс --> Учителя --> Предметы
        """
        list_all_subjcts = []
        list_all_teachers = []
        for i in self.classroom.get_all_teachers():  # Получаю список всех учителей
            list_all_teachers.append(i)

        for i in self.classroom.get_all_subjects():  # Получаю список всех предметов
            list_all_subjcts.append(i)

        return "Ученик {}\t Класс {}\t Учителя {}\t Предметы {}" \
            .format(self.name, self.classroom.classrooms, " ".join(list_all_teachers), " ".join(list_all_subjcts))
        # Вопрос: Здесь не понял формат вывода. Нужно было попарно выводить: Учитель-Предмет?

    def get_parent_names(self):
        """
        Возвращает ФИО родителей ученика
        :return: ФИО родителей ученика
        """
        return "Мама {} Папа {}".format(self.mather, self.father)


class Teacher:
    """
    Класс учителей
    """

    def __init__(self, name, subject):
        """
        Инициализация нового учителя
        :param name: ФИО учителя
        :param subject: предмет, который ведёт учитель
        """
        self.name = name
        self.teach_classes = set()
        self.subject = subject

    def add_classes(self, class_name):
        """
        Добавляет новый учебный класс этому учителю
        :param class_name: новый учебный класс
        :return: изменяет множество self.teach_classes
        """
        self.teach_classes.add(class_name)


class Classroom:
    """
    Класс учебного класса
    """
    all_classrooms = set()  # Множесто всех учебных классов

    def __init__(self, class_name):
        """
        Инициализация учебного класса
        :param class_name: имя класса
        """
        Classroom.all_classrooms.add(class_name)  # Добавляю новый класс во множество всех учебныйх классов
        self.list_classroom = []  # Список учеников
        self.teacher_subject = []  # Список кортежей (учитель, предмет)
        self.classrooms = class_name

    def get_all_classrooms(self):
        """
        Возвращает множество всех учебных классов
        :return: множество всех учебных классов
        """
        return Classroom.all_classrooms

    def get_list_classroom(self):
        """
        Возвращает список учеников учебного класса в формате: 'Иванов И.И.'
        :return: список учеников учебного класса в формате: 'Иванов И.И.'
        """
        list_classrom = []
        for i in self.list_classroom:
            list_classrom.append("{} {}.{}.".format(i.surname, i.name[0], i.otchestvo[0]))
        return list_classrom

    def get_all_teachers(self):
        """
        Возвращает список всех учетелей учебного класса
        :return: список всех учетелей учебного класса
        """
        list_teachers = []
        for i in self.teacher_subject:
            list_teachers.append(i[0].name)
        return list_teachers

    def get_all_subjects(self):
        """
        Возвращает список всех предметов учебного класса
        :return: список всех предметов учебного класса
        """
        list_subjects = []
        for i in self.teacher_subject:
            list_subjects.append(i[1])
        return list_subjects

    def get_all_teacher_subject(self):
        """
        Возвращает список кортежей (учитель, предмет) учебного класса
        :return: список кортежей (учитель, предмет) учебного класса
        """
        teacher_subject = []
        for i in self.teacher_subject:
            teacher_subject.append((self.teacher_subject[0].name, self.teacher_subject[1]))
        return teacher_subject

    def add_list_classroom(self, list_classroom):
        """
        Добавляет список учеников класса
        :param list_classroom: Список учеников класса
        :return: изменение self.list_classroom
        """
        self.list_classroom.extend(list_classroom)

    def add_teacher_subject(self, teacher, subject):
        """
        Добавляет кортеж (учитель, предмет), если этот предемет уже не препадаётся в этом классе
        и если учитель препадаёт этот предмет. Также происходит запись в класс учителя о преподавании в
        этом учебном классе
        :param teacher: ссылка на класс учителя
        :param subject: предмет
        :return: изменяет self.teacher_subject, иначе - ошибка. В случае истиности, происходит запись в класс учителя
        о преподавании в этом учебном классе: teacher.add_classes(self.get_classrooms())
        """
        if subject != teacher.subject:
            return "Учитель {} не преподаёт предмет {}".format(teacher.name, subject)
        else:
            for i in self.teacher_subject:
                if i[1] == subject:
                    return "Предмет {} уже препадаётся в этом классе".format(subject)
            teacher.add_classes(self.classrooms)
            self.teacher_subject.append((teacher, subject))
