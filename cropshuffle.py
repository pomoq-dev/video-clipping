import random
import subprocess

import video_tools
from download import download_video_and_audio
from splitter import split_video
from video_tools import add_audio_to_video

PATH = '/Users/andrey.matveev/VIDEO/input.mp4'
PATH_AUDIO = '/Users/andrey.matveev/VIDEO/input.m4a'
SOURCE_VIDEO_NAME = 'sourcevideo.mp4'
SOURCE_AUDIO_NAME = 'sourceaudio.m4a'
SEGMENTS = 11

download_video_and_audio('https://www.youtube.com/watch?v=0PvbixQ_tJ0', SOURCE_VIDEO_NAME, SOURCE_AUDIO_NAME)
clip = add_audio_to_video(SOURCE_VIDEO_NAME, SOURCE_AUDIO_NAME)
part_len = clip.duration / SEGMENTS

outputs = split_video(clip, SEGMENTS)

random.shuffle(outputs)
video_tools.join_clips_to_video(outputs, 'out.mp4')
