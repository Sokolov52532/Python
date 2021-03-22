class Road:
    def __init__(self, l, w):
        self._lenght = l
        self._width = w

    def summass(self):
        summa = (self._lenght*self._width*(25*5)) / 1000
        return summa


road1 = Road(20, 5000)
print(road1.summass())
