import turtle

class Car:
    def __init__(self, s, c, n, p=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    def show_speed(self):
        return f'speed is: {self.speed}'


class TownCar(Car):
    def __init__(self, s, c, n, p=False):
        super().__init__(s, c, n, p)

    def show_speed(self):
        if self.speed > 60:
            return f'speed limit 60 is reached: {self.speed}'
        else:
            return f'speed is: {self.speed}'


class SportCar(Car):
    def __init__(self, s, c, n, p=False):
        super().__init__(s, c, n, p)


class WorkCar(Car):
    def __init__(self, s, c, n, p=False):
        super().__init__(s, c, n, p)

    def show_speed(self):
        if self.speed > 40:
            return f'speed limit 40 is reached: {self.speed}'
        else:
            return f'speed is: {self.speed}'


class PoliceCar(Car):
    def __init__(self, s, c, n, p=True):
        super().__init__(s, c, n, p)


p_car = PoliceCar(80, 'silver', 'DeLorean')
print(f'created obj {p_car.__class__}, {p_car.speed}, {p_car.color}, {p_car.name}, is police = {p_car.is_police}')
print(p_car.show_speed())

t_car = TownCar(50, 'yellow', 'Bumblebee')
print(f'created obj {t_car.__class__}, {t_car.speed}, {t_car.color}, {t_car.name}, is police = {t_car.is_police}')
print(t_car.show_speed())

t_car2 = TownCar(200, 'green', 'GreenHornet')
print(f'created obj {t_car2.__class__}, {t_car2.speed}, {t_car2.color}, {t_car2.name}, is police = {t_car2.is_police}')
print(t_car2.show_speed())

s_car = SportCar(300, 'black', 'Batmobile')
print(f'created obj {s_car.__class__}, {s_car.speed}, {s_car.color}, {s_car.name}, is police = {s_car.is_police}')
print(s_car.show_speed())

w_car = WorkCar(40, 'white', 'ECTO-1')
print(f'created obj {w_car.__class__}, {w_car.speed}, {w_car.color}, {w_car.name}, is police = {w_car.is_police}')
print(w_car.show_speed())

w_car2 = WorkCar(45, 'blue', 'ECTO-1')
print(f'created obj {w_car2.__class__}, {w_car2.speed}, {w_car2.color}, {w_car2.name}, is police = {w_car2.is_police}')
print(w_car2.show_speed())
