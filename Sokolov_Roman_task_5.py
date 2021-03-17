import os
import django
from collections import defaultdict

root_dir = django.__path__[0]
django_files = defaultdict(list)
count = [0, 0, 0, 0]


def count_file(file, size):
        global count
        count[len(str(size)) - 3] += 1
        ext = file.name.rsplit('.', maxsplit=1)[-1].lower()
        if ext not in django_files[size]:
            django_files[size].append(ext)


def scan(dir):
    for i in os.scandir(dir):
        if i.is_file():
            if i.stat().st_size < 100:
                count_file(i, 100)
            elif 100 < i.stat().st_size < 1000:
                count_file(i, 1000)
            elif 1000 < i.stat().st_size < 10000:
                count_file(i, 10000)
            elif 10000 < i.stat().st_size < 100000:
                count_file(i, 100000)
        elif i.is_dir:
            scan(os.path.join(dir, i.name))


scan(root_dir)

idx = 0
for i in sorted(django_files):
    django_files[i] = (count[idx], django_files[i])
    idx += 1

print(dict(django_files))
