import os
import random

import moviepy.editor as mpe

import video_tools

ads_clip = mpe.VideoFileClip('ExtensionAds.mp4')

clips_paths = list(filter(lambda f: f.startwith('video'), os.listdir('clips')))
random.shuffle(clips_paths)
clips = []
video_i = 0
for clip_path in clips_paths:
    clip = mpe.VideoFileClip(clip_path)
    clips.append(clip)

    if len(clips) == 20:
        where_to_ads_i = random.randint(2, 8)
        clips.insert(where_to_ads_i, ads_clip)
        video_tools.join_clips_to_video(clips, f'result{video_i}')
        clips.clear()
