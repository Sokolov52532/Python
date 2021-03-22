class Worker:
    def __init__(self, n, sur, pos):
        self.name = n
        self.surname = sur
        self.position = pos
        self._income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def __init__(self, n, sur, pos):
        super().__init__(n, sur, pos)
        self._income['wage'] = 500
        self._income['bonus'] = 100500
        print(self.name, self.surname, self.position, self._income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}'


t = Position("Yasya", "Pumpkin", "Janitor")
print(t.get_full_name())
print(t.get_total_income())
