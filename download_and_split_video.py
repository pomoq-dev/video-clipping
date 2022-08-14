import os

from download import download_video_and_audio
from splitter import split_video
from video_tools import add_audio_to_video

SUBCLIP_LEN = 44

video_urls = ['https://www.youtube.com/watch?v=0PvbixQ_tJ0',
              'https://www.youtube.com/watch?v=M8MMTNs9Qss&ab_channel=FunnyTube',
              'https://www.youtube.com/watch?v=IOPxzExwSkU&ab_channel=TrendsChannel',
              'https://www.youtube.com/watch?v=38ahrVGybmY&ab_channel=RarestMemes',
              'https://www.youtube.com/watch?v=1tHct2Er5b0&list=PL-m5JNevmRRxH9qJCZ1WDP9GVtG6kd2U3&ab_channel=BingeCentral',
              'https://www.youtube.com/watch?v=JlBmVwhYCvU&ab_channel=2C1Amemes',
              'https://www.youtube.com/watch?v=H4Kh9KpO-Uk&ab_channel=2C1Amemes',
              'https://www.youtube.com/watch?v=MyGmUJ8TNng',
              'https://www.youtube.com/watch?v=z0eZl0FyHR0&ab_channel=VIDEOHOLIC',
              'https://www.youtube.com/watch?v=4e5GikHICd0']

names = []
for i in range(0, len(video_urls)):
    video_name = os.path.join('source', f'video{i}.mp4')
    audio_name = os.path.join('source', f'audio{i}.m4a')
    names.append((video_name, audio_name))


name_i = 0
for url in video_urls:
    video, audio = names[name_i]
    name_i += 1
    download_video_and_audio(url, video, audio)
    clip = add_audio_to_video(video, audio)

    segments_num = round(clip.duration / SUBCLIP_LEN)
    sub_clips = split_video(clip, segments_num)
    sub_clip_i = 0
    for sub_clip in sub_clips:
        res_name = os.path.join('clips', f'video{name_i}clip{sub_clip_i}.mp4')
        sub_clip.write_videofile(res_name, codec= 'mpeg4', audio_codec='aac')
        sub_clip_i += 1
