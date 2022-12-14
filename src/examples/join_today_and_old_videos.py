import os
import random
import shutil

from tqdm import tqdm

from src.vidliboba.video_tools import get_video_duration_by_path

TODAY_DIR = 'C:\\Users\\am779\\Videos\\Reels\\19_noused'
ALL_RANDOM_DIR = 'C:\\Users\\am779\\Videos\\Reels\\R'
RESULT_WITH_NEW_DIRS = ['C:\\Users\\am779\\Videos\\Reels\\M1', 'C:\\Users\\am779\\Videos\\Reels\\M2',
                        'C:\\Users\\am779\\Videos\\Reels\\M3', 'C:\\Users\\am779\\Videos\\Reels\\M4']
RESULT_WITH_OLD_DIRS = ['C:\\Users\\am779\\Videos\\Reels\\M11', 'C:\\Users\\am779\\Videos\\Reels\\M21',
                        'C:\\Users\\am779\\Videos\\Reels\\M31', 'C:\\Users\\am779\\Videos\\Reels\\M41']
WANT_DURATION = 8 * 60 + 30


def get_videos_paths_shuffled(dir_path):
    videos_names = os.listdir(dir_path)
    videos = []
    for video_name in videos_names:
        if video_name.endswith('.mp4'):
            videos.append(os.path.join(dir_path, video_name))
    random.shuffle(videos)
    return videos


def get_total_duration(videos_paths):
    res = 0
    for path in videos_paths:
        res += get_video_duration_by_path(path)
    return res


def add_old_videos_to(init_videos_paths, all_videos_paths, want_duration):
    # print("add_old_videos_to")
    random.shuffle(all_videos_paths)
    total_duration = get_total_duration(init_videos_paths)
    result_videos_paths = init_videos_paths.copy()

    ind = 0
    while total_duration < want_duration and ind < len(all_videos_paths):
        print(ind)
        video_path = all_videos_paths[ind]
        ind += 1
        total_duration += get_video_duration_by_path(video_path)
        result_videos_paths.append(video_path)

    random.shuffle(result_videos_paths)
    return result_videos_paths


def save_videos_to_dir(videos_paths, dir_path):
    for ind, path in tqdm(enumerate(videos_paths)):
        new_file_name = f'fileM_{ind}.mp4'
        # new_file_name = os.path.basename(path)
        new_file_path = os.path.join(dir_path, new_file_name)
        shutil.copy2(path, new_file_path)


today_videos_paths = get_videos_paths_shuffled(TODAY_DIR)
all_videos_paths = get_videos_paths_shuffled(ALL_RANDOM_DIR)

for res_dir_name in RESULT_WITH_NEW_DIRS:
    videos_paths = add_old_videos_to(today_videos_paths, all_videos_paths, WANT_DURATION)
    save_videos_to_dir(videos_paths, res_dir_name)

for res_dir_name in RESULT_WITH_OLD_DIRS:
    videos_paths = add_old_videos_to([], all_videos_paths, WANT_DURATION)
    save_videos_to_dir(videos_paths, res_dir_name)
