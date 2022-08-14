import os

import moviepy.editor as mpe

from src import audio_tools

video = mpe.VideoFileClip(os.path.join('../results', 'result10_15.mp4'))
audio = audio_tools.audio_change_for_video(mpe.AudioFileClip('../beethoven.flac'))

result = video.set_audio(audio)
result.write_videofile('hobana2.mp4', codec='mpeg4', audio_codec='aac')
