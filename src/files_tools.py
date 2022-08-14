import os


def get_all_paths_files_ext_in_dir(dir_path, ext):
    names = list(filter(lambda x: x.endswith(ext), os.listdir(dir_path)))
    return [os.path.join(dir_path, name) for name in names]
