import os

import moviepy.editor as mpe


video = mpe.VideoFileClip(os.path.join('results', 'result0.mp4'))
audio = mpe.AudioFileClip('beethoven.flac')
audio = audio.subclip(0, video.duration)

result = video.set_audio(audio)
result.write_videofile('hobana.mp4', codec='mpeg4', audio_codec='aac')
