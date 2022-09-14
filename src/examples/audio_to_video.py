import random

import moviepy.editor as mpe

import src.vidliboba.video_tools
from src.vidliboba import audio_tools, video_tools
from src.vidliboba.files_tools import get_all_paths_files_ext_in_dir

SHORT_CLIPS = '../short_clips'


def join_short_clips_to_video_audio_duration(audio, clips_dir):
    video_paths = get_all_paths_files_ext_in_dir(clips_dir, '.mp4')
    total_clips_duration = 0
    clips = []
    while total_clips_duration < audio.duration:
        path = random.choice(video_paths)
        clip = mpe.VideoFileClip(path)
        total_clips_duration += clip.duration
        clips.append(clip)

    video = video_tools.concatenate_videos(clips)
    video = video.set_audio(audio)

    return video


audio = audio_tools.audio_change_for_video(mpe.AudioFileClip('/Users/andrey.matveev/Documents/x6beatReduce.mp3'))
video = join_short_clips_to_video_audio_duration(audio, SHORT_CLIPS)
src.vidlib.video_tools.save_video(video, 'hobana4.mp4')
