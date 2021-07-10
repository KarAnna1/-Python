# Задача 1

class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        for i in self.matr:
            for j in i:
                print("{:4}".format(j), end='')
            print()
        return ''

    def __add__(self, other):
        __n_mnatr = []
        for i in range(0, len(self.matr)):
            __n_mnatr_i = []

            for j in range(0, len(self.matr[i])):

                __n_mnatr_i.append(self.matr[i][j] + other.matr[i][j])
            __n_mnatr.append(__n_mnatr_i)

        return Matrix(__n_mnatr)


new_m_A = Matrix([[1, 3, 2], [5, 9, 32], [4, 9, 45]])
print(new_m_A)

new_m_B = Matrix([[12, 3, 8], [5, 7, 18], [5, 9, 2]])
print(new_m_B)

new_m_C = Matrix.__add__(new_m_A, new_m_B)
print(new_m_C)


# Задача 2

from abc import abstractmethod, ABC
class Clothes(ABC):

    def __init__(self, title):
        self.title = title

    def __add__(self, other):
        return VCl('VCl',(float(self.formula()) + float(other.formula())))

    def __str__(self):
        return self.formula()

    @abstractmethod
    def formula(self, s):
        pass

class VCl(Clothes):
    def __init__(self, title,vs):
        self.vs = vs

    def formula(self):
        return (self.vs).__format__('.2f')


class Coat(Clothes):
    def __init__(self, title, V):
        super(Coat, self).__init__(title)
        self.V = V

    def formula(self):
        return (self.V / 6.5 + 0.5).__format__('.2f')

class Suit(Clothes):
    def __init__(self, title, Heigh):
        super(Suit, self).__init__(title)
        self.Heigh = Heigh

    @property
    def Heigh(self):
        return self.__Heigh

    @Heigh.setter
    def Heigh(self, Heigh):
        if Heigh > 5:
            self.__Heigh = 5
        elif Heigh < 0.5:
            self.__Heigh = 0.5
        else:
            self.__Heigh = Heigh

    def formula(self):
        return (2 * self.Heigh + 0.3).__format__('.2f')

coat = Coat('coat', 12)
print(f'Для {coat.title} потрачено {coat.formula()}')

suit = Suit('suit', 3)
print(f'Для {suit.title} потрачено {suit.formula()}')

suit1 = Suit('suit', 50)
print(f'Для {suit1.title} потрачено {suit1.formula()}')

print(f'Всего потрачено {coat + suit + suit1 + coat1}')


# Задача 3.

class Cell:
    def __init__(self, count_cell):
        self.count_cell = (count_cell)

    @property
    def count_cell(self):
        return self.__count_cell

    @count_cell.setter
    def count_cell(self, count_cell):
        try:
            if int(count_cell) > 0:
                self.__count_cell = int(count_cell)
            else:
                self.__count_cell = 0
        except ValueError:
            self.__count_cell = 0

    def __add__(self, other):
         return Cell(self.count_cell + other.count_cell)

    def __sub__(self, other):
        return Cell(self.count_cell - other.count_cell)

    def __mul__(self, other):
        return Cell(self.count_cell * other.count_cell)

    def __floordiv__(self, other):
        try:
            return Cell(self.count_cell // other.count_cell)
        except ZeroDivisionError:
            return Cell(0)

    def __str__(self):
        if self.count_cell > 0:
            return f'Новая клетка размер {self.count_cell}'
        else:
            return f'неверный размер'

    def make_order(self, cell_row):

        try:
            for i in range(0, self.count_cell // cell_row):
                for i in range(0, cell_row):
                    print('*', end='')
                print()
            if self.count_cell % cell_row != 0:
                for i in range(0, self.count_cell % cell_row):
                    print('*', end='')
                print()
        except ZeroDivisionError:
            pass


cell1 = Cell(3)
cell2 = Cell(7)
cell3 = Cell(1)
cell4 = Cell(12)
cell4.make_order(5)  # 12 по 5 = 3 ряда 2 в последнем

cell5 = cell1 + cell4 # 3 + 12 = 15
print(cell5)
cell5.make_order(4) # 15 по 4 = 4 ряда и 3 в последнем

cell6 = cell3 - cell2 # 1 - 7 = -6
print(cell6)

cell7 = cell2 - cell1 # 7 - 3 = 4
print(cell7)

cell8 = cell6 * cell1 # ошибка
print(cell8)
cell8.make_order(4)

cell9 = cell1 * cell7 # 3 * 4 = 12
print(cell9)

cell10 = cell5 // cell7 # 15 // 4 = 3
print(cell10)

cell11 = cell8 // cell1 # 0 // 3
print(cell11)
cell12 = cell1 // cell8 # 3//0
print(cell12)