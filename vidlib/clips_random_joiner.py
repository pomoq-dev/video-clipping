import os
import random

import moviepy.editor as mpe
from moviepy.audio.AudioClip import CompositeAudioClip

import vidlib.files_tools
from vidlib import audio_tools, clear_directories
from vidlib import video_tools

CLIPS_DIR = '../clips'
ads_clip = mpe.VideoFileClip('../ExtensionAds.mp4')


def resize_all_clips(clips, w, h):
    res = []
    for clip in clips:
        if clip.size[0] != w or clip.size[1] != h:
            res.append(clip.resize(w, h))
        else:
            res.append(clip)
    return res


def make_video_from_clips(clips, res_dir_name, minw, minh, num_clips_in_video, res_name, big_audio_path=None,
                          replace_audio=False):
    clips = resize_all_clips(clips, minw, minh)

    where_to_ads_i = random.randint(min(2, num_clips_in_video - 1), min(8, num_clips_in_video))
    clips.insert(where_to_ads_i, ads_clip)

    video = video_tools.concatenate_videos(clips)
    big_audio = mpe.AudioFileClip(big_audio_path)
    audio = audio_tools.audio_change_for_video(big_audio, 3, video)

    if replace_audio:
        video = video.set_audio(audio)
    else:
        video = video.set_audio(CompositeAudioClip([video.audio, audio]))

    video_tools.save_video(video, os.path.join(res_dir_name, res_name))


def join_clips(num_clips_in_video=20, res_dir_name='results', big_audio=None, replace_audio=False):
    vidlib.files_tools.clear_directory(res_dir_name)

    clips_paths = list(filter(lambda f: f.startswith('video'), os.listdir(CLIPS_DIR)))

    random.shuffle(clips_paths)
    clips = []
    video_i = 0
    minw = ads_clip.size[0]
    minh = ads_clip.size[1]
    for clip_path in clips_paths:
        clip = mpe.VideoFileClip(os.path.join(CLIPS_DIR, clip_path))
        sz = clip.size
        minw = min(minw, sz[0])
        minh = min(minh, sz[1])
        clips.append(clip)

        if len(clips) == num_clips_in_video:
            res_name = f'result{video_i}.mp4'
            video_i += 1
            make_video_from_clips(clips, res_dir_name, minw, minh, num_clips_in_video, res_name, big_audio,
                                  replace_audio)
            minw = 1000000
            minh = 1000000
            clips.clear()
