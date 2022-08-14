import moviepy.editor as mpe
from tqdm import tqdm

import src.mylog


def add_audio_to_video(path_video, path_audio):
    init_clip = mpe.VideoFileClip(path_video)
    audio_background = mpe.AudioFileClip(path_audio)
    # final_audio = mpe.CompositeAudioClip([clip.audio, audio_background])
    final_clip = init_clip.set_audio(audio_background)
    return final_clip


def join_clips_to_video(clips):
    out = mpe.concatenate_videoclips(clips)
    return out


def split_video_segments_num(clip, segments_num):
    part_len = clip.duration / segments_num
    return split_video(clip, part_len, segments_num)


def split_video_part_len(clip, part_len):
    segments_num = round(clip.duration / part_len)
    return split_video(clip, part_len, segments_num)


def split_video(clip, part_len, segments_num):
    src.mylog.log_message('Splitting video...')
    outputs = []
    for i in tqdm(range(0, segments_num)):
        start = round(i * part_len, 2)
        end = round(start + part_len, 2)
        out_clip = clip.subclip(start, end)
        outputs.append(out_clip)
    return outputs


def save_video(video, file_path):
    video.write_videofile(file_path, codec='h264', audio_codec='aac')
