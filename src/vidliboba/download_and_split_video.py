import os

from tqdm import tqdm

import src.vidliboba.files_tools
from src.vidliboba.download import download_video_and_audio_using_lib
from src.vidliboba import video_tools
from moviepy import editor as mpe

old_video_urls = ['https://www.youtube.com/watch?v=0PvbixQ_tJ0',
                  'https://www.youtube.com/watch?v=M8MMTNs9Qss&ab_channel=FunnyTube',
                  'https://www.youtube.com/watch?v=IOPxzExwSkU&ab_channel=TrendsChannel',
                  'https://www.youtube.com/watch?v=38ahrVGybmY&ab_channel=RarestMemes',
                  'https://www.youtube.com/watch?v=1tHct2Er5b0&list=PL-m5JNevmRRxH9qJCZ1WDP9GVtG6kd2U3&ab_channel=BingeCentral',
                  'https://www.youtube.com/watch?v=JlBmVwhYCvU&ab_channel=2C1Amemes',
                  'https://www.youtube.com/watch?v=H4Kh9KpO-Uk&ab_channel=2C1Amemes',
                  'https://www.youtube.com/watch?v=MyGmUJ8TNng',
                  'https://www.youtube.com/watch?v=z0eZl0FyHR0&ab_channel=VIDEOHOLIC',
                  'https://www.youtube.com/watch?v=4e5GikHICd0']


def download_and_split_by_clips(video_urls, source_dir='../source', out_dir='../clips', subclip_len=44, skip_first=0, add_audio=True):
    src.vidlib.files_tools.clear_directory(out_dir)
    src.vidlib.files_tools.clear_directory(source_dir)

    names = []
    for i in range(0, len(video_urls)):
        video_name = os.path.join(source_dir, f'video{i}.mp4')
        audio_name = os.path.join(source_dir, f'audio{i}.m4a')
        names.append((video_name, audio_name))

    for name_i, url in tqdm(enumerate(video_urls)):
        video, audio = names[name_i]

        download_video_and_audio_using_lib(url, video, audio)
        if add_audio:
            clip = video_tools.add_audio_to_video(video, audio)
        else:
            clip = mpe.VideoFileClip(video)
        clip = clip.subclip(skip_first, clip.duration)

        sub_clips = video_tools.split_video_part_len(clip, subclip_len)
        for sub_clip_i, sub_clip in enumerate(sub_clips):
            res_path = os.path.join(out_dir, f'video{name_i}clip{sub_clip_i}.mp4')
            try:
                video_tools.save_video(sub_clip, res_path)
            except Exception as ex:
                pass
            sub_clip_i += 1
