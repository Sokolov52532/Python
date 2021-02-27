num_dict = dict(one='один', two='два', three='три', four='четыре', five='пять',
                six='шесть', seven='семь', eight='восемь', nine='девять', ten='десять')


def num_translate_adv(word):
    """
    translates numbers from English into Russian

    :param word: str
    :return: str
    """

    if word.istitle():
        word = word.lower()
        if word in num_dict:
            return word.title()
    elif word in num_dict:
        return word


print(num_translate_adv(input()))