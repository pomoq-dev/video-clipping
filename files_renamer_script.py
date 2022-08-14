import os
import random

PATH = 'rename_example_directory'

files = os.listdir(PATH)
paths = []
for file_name in files:
    path = os.path.join(PATH, file_name)
    if not path.endswith('.mp4'):
        continue
    paths.append(path)

new_paths = [os.path.join(PATH, f'file_temp{x}.mp4') for x in range(0, len(paths))]
random.shuffle(new_paths)
print(new_paths)

for path, new_path in zip(paths, new_paths):
    os.rename(path, new_path)

paths = new_paths
new_paths = [os.path.join(PATH, f'file{x}.mp4') for x in range(0, len(paths))]
random.shuffle(new_paths)
print(new_paths)

for path, new_path in zip(paths, new_paths):
    os.rename(path, new_path)
