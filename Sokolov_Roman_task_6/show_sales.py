from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if len(argv) > 2:
            if int(argv[1]) - 1 <= i <= int(argv[2]) - 1:
                print(line.replace('\n', ''))
        elif len(argv) > 1:
            if int(argv[1]) - 1 <= i:
                print(line.replace('\n', ''))
        elif len(argv) == 1:
            print(line.replace('\n', ''))
