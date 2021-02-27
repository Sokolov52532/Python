from random import choice, sample

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def jokes(num):
    """
    randomly generate jokes

    :param num: int(0-5)
    :return: list[*str]
    """

    n = 0
    list1 = []

    while n != num:
        list1.append(str(f'{choice(nouns)}, {choice(adverbs)}, {choice(adjectives)}'))
        n += 1
    return list1


print(jokes(5))

#----------------Без повторов, но без флагов------------------------------


def jokes(num):
    list1 = (sample(nouns, 5))
    list2 = (sample(adverbs, 5))
    list3 = (sample(adjectives, 5))
    list4 = []
    n = 0
    while n != num:
        list4.append(str(f'{list1[n]}, {list2[n]}, {list3[n]}'))
        n += 1
    return list4


print(jokes(5))
