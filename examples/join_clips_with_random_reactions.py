import os
import random

from vidlib import files_tools
from vidlib import video_tools

from moviepy import editor as mpe

CLIPS_DIR = '../SHORT_VIDEOS'
REACTIONS_DIR = '../REACTIONS'


random_clips = files_tools.list_full_paths(CLIPS_DIR, only_format='.mp4')
random.shuffle(random_clips)

random_reactions = files_tools.list_full_paths(REACTIONS_DIR, only_format='.mp4')
random.shuffle(random_reactions)

res_clips = []
for clip_path in random_clips:
    clip = mpe.VideoFileClip(clip_path)
    height = clip.size[1]
    res_clips.append(clip)
    reaction_path = random.choice(random_reactions)
    reaction = mpe.VideoFileClip(reaction_path)
    reaction = reaction.resize(height=height)
    res_clips.append(reaction)

video = video_tools.concatenate_videos(res_clips)
video_tools.save_video(video, 'res_video.mp4')
