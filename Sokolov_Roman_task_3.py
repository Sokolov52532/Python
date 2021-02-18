pers = int(input('Введите колличество процентов: '))

if pers % 10 == 1 and pers != 11:
    print(pers, 'процент')
if 5 <= pers % 10 <= 9 or pers % 10 == 0 or pers == 11:
    print(pers, 'процентов')
if 2 <= pers % 10 <= 4:
    print(pers, 'процента')
