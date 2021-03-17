import os
import yaml

with open('config.yaml') as f:
    content = yaml.safe_load(f)


def createTree(values, prefix=""):
    for directory, paths in values.items():
        dir_path = os.path.join(prefix, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            createTree(paths, dir_path)
        else:
            for i in paths:
                if isinstance(i, dict):
                    createTree(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'), 'w') as f:
                        f.write('')


createTree(content)

print(content)
