class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = int(input('что делим?: '))
inp_data_2 = int(input('на что делим?: '))

try:
    if inp_data or inp_data_2 == 0:
        raise ZeroError('На ноль делить нельзя')
    result = inp_data / inp_data_2
except ValueError:
    print('Вы ввели не число')
except ZeroError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {result}")

