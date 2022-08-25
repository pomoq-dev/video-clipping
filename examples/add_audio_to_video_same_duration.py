import os.path

from vidlib import files_tools
from vidlib import video_tools
from vidlib import audio_tools
from moviepy import editor as mpe

VIDEO_DIR = '../drive-download-20220825T115431Z-001'
AUDIO_DIR = 'audios_wav'

videos = files_tools.list_full_paths(VIDEO_DIR, 'mp4')
videos.sort()
audios = files_tools.list_full_paths(AUDIO_DIR, 'wav')
audios.sort()

for src_audio_path, video_path in zip(audios, videos):
    audio = mpe.AudioFileClip(src_audio_path)
    video = mpe.VideoFileClip(video_path)
    ratio = audio.duration / video.duration
    audio_tools.change_sound_speed(src_audio_path, 'tmp.wav', ratio)
    res_video = video_tools.add_audio_to_video(video_path, 'tmp.wav')

    video_basename = os.path.basename(video_path)
    video_tools.save_video(res_video, video_basename)



