price = [38.75, 14, 65.02, 75.98, 76, 25.2, 55, 37,
         78.01, 21.4, 77.14, 21.92, 92, 19.02, 24.5]

for i, val in enumerate(price):
    rub = int(val)
    kop = int(round(val % int(val), 2) * 100)
    if i != len(price) - 1:
        print(f'{rub} руб {kop:02d} коп', end=', ')
    else:
        print(f'{rub} руб {kop:02d} коп')

for i, val in enumerate(sorted(price)):
    rub = int(val)
    kop = int(round(val % int(val), 2) * 100)
    if i != len(price) - 1:
        print(f'{rub} руб {kop:02d} коп', end=', ')
    else:
        print(f'{rub} руб {kop:02d} коп')

print(f'исходный список: {price}')

down_price = reversed(sorted(price))

for i, val in enumerate(sorted(price)):
    rub = int(val)
    kop = int(round(val % int(val), 2) * 100)
    if len(price) - 6 < i != len(price) - 1:
        print(f'{rub} руб {kop:02d} коп', end=', ')
    elif i == len(price) - 1:
        print(f'{rub} руб {kop:02d} коп')

