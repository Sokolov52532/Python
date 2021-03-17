import os
from shutil import copytree, copy2

root_dir = 'my_project'
result_dir = os.path.join(root_dir, 'templates')


def copyng_temp(path, destination):
    for i in os.scandir(path):
        if i.is_file():
            if os.path.split(os.path.split(path)[0])[1] == 'templates':
                os.makedirs(os.path.join(destination,
                                         os.path.split(os.path.split(os.path.split(path)[0])[0])[1]),
                            exist_ok=True)
                copy2(os.path.join(path, i.name),
                      os.path.join(destination, os.path.split(os.path.split(os.path.split(path)[0])[0])[1]))
            else:
                pass
        elif i.is_dir():
            if i.name == 'templates':
                for j in os.scandir(os.path.join(path, i.name)):
                    if j.is_dir():
                        copyng_temp(os.path.join(os.path.join(path, i.name), j.name), destination)
            else:
                copyng_temp(os.path.join(path, i.name), destination)


copyng_temp(root_dir, result_dir)
