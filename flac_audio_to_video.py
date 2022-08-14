import os
import random

import moviepy.editor as mpe


def audio_change(audio):
    piece_duration = 3
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
    random.shuffle(sub_audios)
    return mpe.concatenate_audioclips(sub_audios)


video = mpe.VideoFileClip(os.path.join('results', 'result10_15.mp4'))
audio = mpe.AudioFileClip('beethoven.flac')
audio = audio_change(audio.subclip(0, video.duration))

result = video.set_audio(audio)
result.write_videofile('hobana.mp4', codec='mpeg4', audio_codec='aac')
