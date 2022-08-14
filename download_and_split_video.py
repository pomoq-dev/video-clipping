from download import download_video_and_audio
from splitter import split_video
from video_tools import add_audio_to_video

SUBCLIP_LEN = 30

video_urls = ['https://www.youtube.com/watch?v=0PvbixQ_tJ0']

names = []
for i in range(0, len(video_urls)):
    video_name = f'video{i}.mp4'
    audio_name = f'audio{i}.m4a'
    names.append((video_name, audio_name))


name_i = 0
sub_clip_i = 0
for url in video_urls:
    video, audio = names[name_i]
    download_video_and_audio(url, video, audio)
    clip = add_audio_to_video(video, audio)

    segments_num = round(clip.duration / SUBCLIP_LEN)
    sub_clips = split_video(clip, segments_num)
    for sub_clip in sub_clips:
        res_name = f'subclip{sub_clip_i}.mp4'
        sub_clip.write_videofile(res_name, codec= 'mpeg4', audio_codec='aac')
        sub_clip_i += 1
