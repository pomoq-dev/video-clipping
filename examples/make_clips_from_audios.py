import os
import random

from moviepy import editor as mpe

import src.audio_tools
import src.clear_directories
import src.download_and_split_video
from src.files_tools import get_all_paths_files_ext_in_dir
from src import video_tools

SOURCE_VIDEO_FOR_SPLIT = '../source_video_to_split'
SHORT_CLIPS = '../short_clips'
RES_AUDIOS = '../res_audios'
RES_LONG_AUDIOS = '../res_long_audios'
SOURCE_AUDIOS = '../source_audios'


def download_split_videos():
    video_urls = ['https://www.youtube.com/watch?v=wGSstiUNSKE',
                  'https://www.youtube.com/watch?v=cjyz2PkR5eI',
                  'https://www.youtube.com/watch?v=Poth11ZXQC0',
                  'https://youtu.be/iIG_vDraMUQ',
                  'https://youtu.be/S9Nwwvyjkqg']
    # video_urls = ['https://www.youtube.com/watch?v=wGSstiUNSKE',
    #               'https://www.youtube.com/watch?v=cjyz2PkR5eI']
    src.download_and_split_video.download_and_split_by_clips(video_urls, SOURCE_VIDEO_FOR_SPLIT, SHORT_CLIPS, 3)


def split_songs_to_clips():
    src.clear_directories.clear_directory(RES_AUDIOS)

    audio_names = os.listdir(SOURCE_AUDIOS)
    audio_names = audio_names[0:10]
    for name_i, name in enumerate(audio_names):
        if not name.endswith('.mp3'):
            continue
        path = os.path.join(SOURCE_AUDIOS, name)
        audio = mpe.AudioFileClip(path)
        sub_audios = src.audio_tools.split_audio_to_parts(audio)

        for sub_audio_i, sub_audio in enumerate(sub_audios):
            res_name = f'song{name_i}sub{sub_audio_i}.mp4'
            res_path = os.path.join(RES_AUDIOS, res_name)
            try:
                sub_audio.write_audiofile(res_path, codec='aac')
            except Exception as ex:
                pass


def join_random_clips(clips_in_one):
    audio_paths = get_all_paths_files_ext_in_dir(RES_AUDIOS, '.mp4')
    video_paths = get_all_paths_files_ext_in_dir(SHORT_CLIPS, '.mp4')
    random.shuffle(audio_paths)
    random.shuffle(video_paths)

    src.clear_directories.clear_directory(RES_LONG_AUDIOS)
    num_long_audios = len(audio_paths) // clips_in_one
    for long_audio_i in range(0, num_long_audios):
        res_path = os.path.join(RES_LONG_AUDIOS, f'long_audio{long_audio_i}.mp4')
        sub_videos = []
        for i in range(0, clips_in_one):
            path_i = long_audio_i * clips_in_one + i
            sub_audio = mpe.AudioFileClip(audio_paths[path_i])
            sub_video = mpe.VideoFileClip(video_paths[random.randint(0, len(video_paths) - 1)])
            sub_video = sub_video.set_audio(sub_audio)
            sub_videos.append(sub_video)
        res_video = video_tools.concatenate_videos(sub_videos)
        video_tools.save_video(res_video, res_path)


download_split_videos()
split_songs_to_clips()
join_random_clips(10)
