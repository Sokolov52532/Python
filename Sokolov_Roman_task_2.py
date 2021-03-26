from abc import ABC


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    def calc(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        print(f'maked coat {self.name} {self.size}')

    @property
    def calc(self):
        return (self.size / 6.5) + 0.5


class Costume(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.height = h
        print(f'maked costume {self.name} {self.height}')

    @property
    def calc(self):
        return (self.height * 2) + 0.3


a = Coat('first', 33)
b = Costume('second', 5)

print(a.calc)
print(b.calc)
