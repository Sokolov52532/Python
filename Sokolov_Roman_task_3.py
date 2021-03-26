class Cell:
    def __init__(self, n):
        self.num = n

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num > other.num:
            return self.num - other.num
        elif self.num < other.num:
            return other.num - self.num
        else:
            return 'разность ячеек клеток равна нулю'

    def __mul__(self, other):
        return self.num * other.num

    def __floordiv__(self, other):
        if self.num > other.num:
            return self.num // other.num
        elif self.num < other.num:
            return other.num // self.num
        else:
            return 'разность ячеек клеток равна нулю'

    def make_order(self, ncells):
        print(f'{"*" * ncells}\n' * (self.num // ncells), "*" * (self.num % ncells), sep='')


cell1 = Cell(23)
cell2 = Cell(3)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 // cell2)
print(cell1 * cell2)

cell1.make_order(5)
