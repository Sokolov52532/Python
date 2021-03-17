import os

path = 'D:\projects'
folders = ['settings',
           'mainapp',
           'adminapp',
           'authapp']


def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

projectname = input('Input project name: ')
createFolder(path)

full_path = os.path.join(path, projectname)
createFolder(full_path)

for f in folders:
    folder = os.path.join(full_path, f)
    createFolder(folder)
