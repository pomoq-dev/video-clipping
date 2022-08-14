import moviepy.editor as mpe
import os
import random
import fnmatch
from pydub import AudioSegment

PATH = '/Users/andrey.matveev/VIDEO/input.mp4'
PATH_AUDIO = '/Users/andrey.matveev/VIDEO/input.m4a'
PATH_VIDEO_AUDIO = '/Users/andrey.matveev/VIDEO/input.mp4'
SEGMENTS = 10


def add_audio_to_video():
    init_clip = mpe.VideoFileClip(PATH)
    audio_background = mpe.AudioFileClip(PATH_AUDIO)
    # final_audio = mpe.CompositeAudioClip([clip.audio, audio_background])
    final_clip = init_clip.set_audio(audio_background)
    return final_clip


clip = add_audio_to_video()
part_len = clip.duration / SEGMENTS

outputs = []
for i in range(0, SEGMENTS):
    start = round(i * part_len, 2)
    end = round(start + part_len, 2)
    out_clip = clip.subclip(start, end)
    outputs.append(out_clip)

random.shuffle(outputs)
out = mpe.concatenate_videoclips(outputs)
out.write_videofile('out.mp4', codec= 'mpeg4', audio_codec='aac')

