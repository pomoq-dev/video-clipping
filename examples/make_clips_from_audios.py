import os
import random

from moviepy import editor as mpe

import src.audio_tools
import src.clear_directories

RES_AUDIOS = '../res_audios'
RES_LONG_AUDIOS = '../res_long_audios'
SOURCE_AUDIOS = '../source_audios'


def split_songs_to_clips():
    src.clear_directories.clear_directory(RES_AUDIOS)

    audio_names = os.listdir(SOURCE_AUDIOS)
    for name_i, name in enumerate(audio_names):
        if not name.endswith('.mp3'):
            continue
        path = os.path.join(SOURCE_AUDIOS, name)
        audio = mpe.AudioFileClip(path)
        sub_audios = src.audio_tools.split_audio_to_parts(audio)

        for sub_audio_i, sub_audio in enumerate(sub_audios):
            res_name = f'song{name_i}sub{sub_audio_i}.mp3'
            res_path = os.path.join(RES_AUDIOS, res_name)
            sub_audio.write_audiofile(res_path, codec='aac')


def join_random_clips(clips_in_one):
    names = list(filter(lambda x: x.endswith('.mp4'), os.listdir(RES_AUDIOS)))
    paths = [os.path.join(RES_AUDIOS, name) for name in names]
    random.shuffle(paths)

    src.clear_directories.clear_directory(RES_LONG_AUDIOS)
    num_long_audios = len(paths) // clips_in_one
    for long_audio_i in range(0, num_long_audios):
        res_path = os.path.join(RES_LONG_AUDIOS, f'long_audio{long_audio_i}.mp4')
        sub_audios = []
        for i in range(0, clips_in_one):
            path_i = long_audio_i * clips_in_one + i
            sub_audio = mpe.AudioFileClip(paths[path_i])
            sub_audios.append(sub_audio)
        res_audio = mpe.concatenate_audioclips(sub_audios)
        res_audio.write_audiofile(res_path, codec='aac')


join_random_clips(30)
