import random
import subprocess
from subprocess import run

import moviepy.editor as mpe

from download import download_video_and_audio
from splitter import split_video
from video_tools import add_audio_to_video

PATH = '/Users/andrey.matveev/VIDEO/input.mp4'
PATH_AUDIO = '/Users/andrey.matveev/VIDEO/input.m4a'
SOURCE_VIDEO_NAME = 'sourcevideo.mp4'
SOURCE_AUDIO_NAME = 'sourceaudio.m4a'
SEGMENTS = 11


def print_subprocess_output(proc):
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        print(line)
        line = proc.stderr.readline()
        if not line:
            break
        print(line)


def download_video_with_audio(yt_url):
    p = subprocess.Popen(['yt-dlp', '-f', 'best', f"{yt_url}", '-o', SOURCE_VIDEO_NAME], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    print_subprocess_output(p)
    print(42)


download_video_and_audio('https://www.youtube.com/watch?v=0PvbixQ_tJ0', SOURCE_VIDEO_NAME, SOURCE_AUDIO_NAME)
clip = add_audio_to_video(SOURCE_VIDEO_NAME, SOURCE_AUDIO_NAME)
part_len = clip.duration / SEGMENTS

outputs = split_video(clip, SEGMENTS)

random.shuffle(outputs)
out = mpe.concatenate_videoclips(outputs)
out.write_videofile('out.mp4', codec= 'mpeg4', audio_codec='aac')
