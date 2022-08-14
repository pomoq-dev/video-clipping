import os
import random

import moviepy.editor as mpe

import video_tools

CLIPS_DIR = 'clips'
ads_clip = mpe.VideoFileClip('ExtensionAds.mp4')


def resize_all_clips(clips, w, h):
    res = []
    for clip in clips:
        if clip.size[0] != w or clip.size[1] != h:
            res.append(clip.resize(w, h))
        else:
            res.append(clip)
    return res


def join_clips(num_clips_in_video=20):
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
            clips = resize_all_clips(clips, minw, minh)
            where_to_ads_i = random.randint(min(2, num_clips_in_video - 1), min(8, num_clips_in_video))
            clips.insert(where_to_ads_i, ads_clip)
            video_tools.join_clips_to_video(clips, os.path.join('results', f'result{video_i}.mp4'))
            video_i += 1
            clips.clear()
            minw = 1000000
            minh = 1000000
