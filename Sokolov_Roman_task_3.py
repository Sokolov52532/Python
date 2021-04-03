class NotInt(Exception):
    def __init__(self, txt):
        self.txt = txt


list1 = []

while True:
    try:
        inp_data = (input("Введите число: "))
        if inp_data == 'stop':
            break
        elif not inp_data.isdigit():
            raise NotInt('Вы ввели не число')
    except NotInt as err:
        print(err)
    else:
        list1.append(int(inp_data))
        print(f'{list1}, для завершения программы введите "stop"')
