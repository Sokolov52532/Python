from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]


def sor_klasses():
    if len(klasses) < len(tutors):
        zipped = tuple(zip_longest(tutors, klasses, fillvalue=None))
        yield zipped
    else:
        for i in range(len(tutors)):
            yield tutors[i], klasses[i]


print(*sor_klasses())
