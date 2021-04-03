class Date:
    def __init__(self, date):
        self.date = date.split('-')

    @classmethod
    def splits(cls, date):
        list1 = []
        for i in date.split("-"):
            list1.append(int(i))
        return list1

    @staticmethod
    def checkdate(lis):
        lis = lis.split('-')
        if 0 < int(lis[0]) < 31 and lis[0].isdigit():
            print('Дата введена верно')
        else:
            print('Дата введена неверно')
        if 0 < int(lis[1]) < 12 and lis[1].isdigit():
            print('месяц введен верно')
        else:
            print('месяц введен неверно')
        if 0 < int(lis[2]) < 9999 and lis[2].isdigit():
            print('год введен верно')
        else:
            print('год введен неверно')


a = Date("12-05-1224")
print(a.splits("12-05-1224"))
Date.checkdate("12-05-1224")
Date.checkdate("35-13-0")

