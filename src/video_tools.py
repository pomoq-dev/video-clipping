import moviepy.editor as mpe


def add_audio_to_video(path_video, path_audio):
    init_clip = mpe.VideoFileClip(path_video)
    audio_background = mpe.AudioFileClip(path_audio)
    # final_audio = mpe.CompositeAudioClip([clip.audio, audio_background])
    final_clip = init_clip.set_audio(audio_background)
    return final_clip


def join_clips_to_video(clips):
    out = mpe.concatenate_videoclips(clips)
    return out


def split_video(clip, segments_num):
    part_len = clip.duration / segments_num
    outputs = []
    for i in range(0, segments_num):
        start = round(i * part_len, 2)
        end = round(start + part_len, 2)
        out_clip = clip.subclip(start, end)
        outputs.append(out_clip)
    return outputs
