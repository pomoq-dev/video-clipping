import moviepy.editor as mpe
from moviepy.video.VideoClip import ColorClip
from tqdm import tqdm

import vidlib.mylog


def add_audio_to_video(path_video, path_audio):
    init_clip = mpe.VideoFileClip(path_video)
    audio_background = mpe.AudioFileClip(path_audio)
    # final_audio = mpe.CompositeAudioClip([clip.audio, audio_background])
    final_clip = init_clip.set_audio(audio_background)
    return final_clip


def split_video_segments_num(clip, segments_num):
    part_len = clip.duration / segments_num
    return split_video(clip, part_len, segments_num)


def split_video_part_len(clip, part_len):
    segments_num = round(clip.duration / part_len)
    return split_video(clip, part_len, segments_num)


def split_video(clip, part_len, segments_num):
    vidlib.mylog.log_message('Splitting video...')
    outputs = []
    for i in tqdm(range(0, segments_num)):
        start = round(i * part_len, 2)
        end = round(start + part_len, 2)
        out_clip = clip.subclip(start, end)
        outputs.append(out_clip)
    return outputs


def save_video(video, file_path):
    video.write_videofile(file_path, audio_codec='aac', codec='h264')


def concatenate_videos(videos):
    return mpe.concatenate_videoclips(videos, method='compose')


def get_video_duration_by_path(video_path):
    video = mpe.VideoFileClip(video_path)
    duration = video.duration
    video.close()
    return duration


def crop_center_square_video(video_clip):
    w = video_clip.size[0]
    h = video_clip.size[1]
    if w == h:
        return video_clip

    if w > h:
        start_w = (w - h) / 2
        end_w = w - (w - h) / 2
        return video_clip.crop(x1 = start_w, y1 = 0, x2 = end_w, y2 = h)
    else:
        start_h = (h - w) / 2
        end_h = h - (h - w) / 2
        return video_clip.crop(x1=0, y1=start_h, x2=w, y2=end_h)
