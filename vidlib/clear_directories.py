import os
import shutil


def clear_directory(name):
    print(f'Removing {name}...')
    if os.path.isdir(name):
        shutil.rmtree(name)
    os.makedirs(name)


def clear_all():
    clear_directory('clips')
    clear_directory('results')
    clear_directory('source')
