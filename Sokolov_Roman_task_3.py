def sort(*args):
    """
    generate dict where keys is first symbols from *args and
    value is list of strings starts with key

    :param args: *str
    :return: dict{*key: [*str]}
    """

    list_1 = dict()

    for i, val in enumerate(args):
        if val[:1] not in list_1:
            list_1[val[:1]] = [val]
        else:
            list_1[val[:1]].append(val)

    return list_1


print(sort("Иван", "Мария", "Петр", "Илья"))
