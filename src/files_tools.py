import os
import random


def get_all_paths_files_ext_in_dir(dir_path, ext):
    names = list(filter(lambda x: x.endswith(ext), os.listdir(dir_path)))
    return [os.path.join(dir_path, name) for name in names]


def rename_files_random(dir_with_files):
    files = os.listdir(dir_with_files)
    paths = []
    for file_name in files:
        path = os.path.join(dir_with_files, file_name)
        if not path.endswith('.mp4'):
            continue
        paths.append(path)

    new_paths = [os.path.join(dir_with_files, f'file_temp{x}.mp4') for x in range(0, len(paths))]
    random.shuffle(new_paths)
    print(new_paths)

    for path, new_path in zip(paths, new_paths):
        os.rename(path, new_path)

    paths = new_paths
    new_paths = [os.path.join(dir_with_files, f'file{x}.mp4') for x in range(0, len(paths))]
    random.shuffle(new_paths)
    print(new_paths)

    for path, new_path in zip(paths, new_paths):
        os.rename(path, new_path)
