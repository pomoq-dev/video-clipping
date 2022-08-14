import os

import moviepy.editor as mpe

import src.video_tools
from src import audio_tools
from src import video_tools

video = mpe.VideoFileClip(os.path.join('../results', 'result10_15.mp4'))
audio = audio_tools.audio_change_for_video(mpe.AudioFileClip('../beethoven.flac'))

result = video.set_audio(audio)
src.video_tools.save_video(result, 'hobana2.mp4')
