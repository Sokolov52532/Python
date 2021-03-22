class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        return f'Запуск отрисовки c помощью {self.title}'


class Pencil(Stationery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        return f'Запуск отрисовки c помощью {self.title}'


class Handle(Stationery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        return f'Запуск отрисовки c помощью {self.title}'


blank = Stationery('blank')
print(blank.draw())

pen = Pen('Ручка')
print(pen.draw())

pencil = Pencil('Карандаш')
print(pencil.draw())

handle = Handle('Маркер')
print(handle.draw())
