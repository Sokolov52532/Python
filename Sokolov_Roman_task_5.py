from itertools import zip_longest
from sys import argv
import json

n, source1, source2, output = argv

with open(str(source1), 'r', encoding='utf-8') as users:
    with open(str(source2), 'r', encoding='utf-8') as hobbys:
        dict1 = {user.replace('\n', ''): hobby for user, hobby in zip_longest(users, hobbys, fillvalue=None) if users}
        for i in dict1:
            if dict1[i]:
                dict1[i] = dict1[i].replace('\n', '')

with open(str(output), 'w', encoding='utf-8') as users_hobby:
    json.dump(dict1, users_hobby, ensure_ascii=False, indent=2)

print(dict1)
