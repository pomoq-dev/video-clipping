import random

from moviepy import editor as mpe


def split_audio_to_parts(audio, piece_duration=3):
    sub_audios = []
    piece_cnt = round(audio.duration / piece_duration)
    for i in range(0, piece_cnt + 1):
        start = i * piece_duration
        if start >= audio.duration:
            break
        end = start + piece_duration
        if end >= audio.duration:
            break
        sub_audio = audio.subclip(start, end)
        sub_audios.append(sub_audio)
    return sub_audios


def audio_change_for_video(source_audio, piece_duration=3, video=None):
    audio = source_audio
    if video != None:
        audio = source_audio.subclip(0, video.duration)

    sub_audios = split_audio_to_parts(audio, piece_duration)
    return mpe.concatenate_audioclips(sub_audios)