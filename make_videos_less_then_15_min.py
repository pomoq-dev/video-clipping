import os
import random

import moviepy.editor as mpe

RESULTS_DIR = 'results'


videos_paths = list(filter(lambda f: f.startswith('result') and '_15.' not in f, os.listdir(RESULTS_DIR)))
for video_path in videos_paths:
    video = mpe.VideoFileClip(os.path.join(RESULTS_DIR, video_path))
    rnd = random.randint(0, 7)
    max_duration = 890 + rnd
    if video.duration > max_duration:
        new_video = video.subclip(0, max_duration)
        name = video_path.split('.mp4')[0]
        new_path = f'{name}_15.mp4'
        new_video.write_videofile(os.path.join(RESULTS_DIR, new_path), codec= 'mpeg4', audio_codec='aac')
