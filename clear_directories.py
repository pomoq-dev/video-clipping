import os
import shutil


def remove_directory(name):
    print(f'Removing {name}...')
    shutil.rmtree(name)


remove_directory('clips')
remove_directory('results')
remove_directory('source')

os.mkdir('clips')
os.mkdir('results')
os.mkdir('source')
