# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
#

# import math
# class Triangle:
#     def __init__(self, ax, ay, bx, by, cx, cy):
#         self.ax = ax
#         self.ay = ay
#         self.bx = bx
#         self.by = by
#         self.cx = cx
#         self.cy = cy
#
#     def dliny_storon(self):
#         ab = int(((self.bx-self.ax)**2 + (self.by - self.ay)**2)**0.5)
#         bc = int(((self.cx-self.bx)**2 + (self.cy - self.by)**2)**0.5)
#         ac = int(((self.cx-self.ax)**2 + (self.cy - self.ay)**2)**0.5)
#         return ab, bc, ac
#
#     def perimetr(self):
#         return int(sum(self.dliny_storon()))
#
#
#     def square (self):
#         p = self.perimetr() / 2
#         return int((p * (p - self.dliny_storon()[0]) * (p - self.dliny_storon()[1]) * (p - self.dliny_storon()[2]))**0.5)
#
#     def height (self):
#         hab = int(2 * self.square() / self.dliny_storon()[0])
#         hac = int(2 * self.square() / self.dliny_storon()[1])
#         hbc = int(2 * self.square() / self.dliny_storon()[2])
#         return hab, hac, hbc
#
#
#
# triangle1 = Triangle(1,2,5,10,10,3)
# print(type(triangle1.dliny_storon()))

# print("Площадь треугольника " , triangle1.square())
# print("Высота треугольника " , triangle1.height())
# print("Периметр треугольника " , triangle1.perimetr())



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze:
    def __init__(self, ax, ay, bx, by, cx, cy, dx,dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy


    def istrapeze(self):
        return (abs(self.ay - self.by) == abs(self.cy - self.dy) or abs(self.cy - self.by) == abs(self.ay - self.dy)) \
                or (abs(self.ax - self.bx) == abs(self.cx - self.dx) or abs(self.cx - self.bx) == abs(self.ax - self.dx))


    def isequilateral(self):
        if self.dliny_storon()[0] == self.dliny_storon()[2] or self.dliny_storon()[1] == self.dliny_storon()[3]:
            print("Трапеция равнобочная")
        else:
            print("Трапеция неравнобочная")


    def dliny_storon(self):
        ab = int(((self.bx - self.ax) ** 2 + (self.by - self.ay) ** 2) ** 0.5)
        bc = int(((self.cx - self.bx) ** 2 + (self.cy - self.by) ** 2) ** 0.5)
        cd = int(((self.dx - self.cx) ** 2 + (self.dy - self.cy) ** 2) ** 0.5)
        da = int(((self.ax - self.dx) ** 2 + (self.ay - self.dy) ** 2) ** 0.5)
        return ab, bc, cd, da

    def perimetr(self):
        return int(sum(self.dliny_storon()))


    def square (self):
        if abs(self.ay - self.by) == abs(self.cy - self.dy) and abs(self.ay - self.by) != 0:
            return int((self.dliny_storon()[1] + self.dliny_storon()[3]) * (self.ay - self.by) / 2)
        if abs(self.cy - self.by) == abs(self.ay - self.dy) and abs(self.cy - self.by) != 0:
            return int((self.dliny_storon()[0] + self.dliny_storon()[2]) * (self.cy - self.by) / 2)
        if abs(self.ax - self.bx) == abs(self.cx - self.dx) and abs(self.ax - self.bx) != 0:
            return int((self.dliny_storon()[1] + self.dliny_storon()[3]) * (self.ax - self.bx) / 2)
        if abs(self.cx - self.bx) == abs(self.ax - self.dx) and abs(self.cx - self.bx) != 0:
            return int((self.dliny_storon()[0] + self.dliny_storon()[2]) * (self.cx - self.bx) / 2)


trapeze1 = Trapeze(1,1,2,5,7,5,10,1)


if trapeze1.istrapeze():
    print("Похоже это трапеция, параллельные основания")
    trapeze1.isequilateral()
    print("Длины сторон трапеции",  trapeze1.dliny_storon())
    print("Площадь трапеции",  trapeze1.square())
    print("Периметр трапеции", trapeze1.perimetr())
else:
    print("Похоже это не трапеция, нет параллельных оснований")




#normal

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


#hard

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла