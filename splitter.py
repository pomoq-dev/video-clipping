def split_video(clip, segments_num):
    part_len = clip.duration / segments_num
    outputs = []
    for i in range(0, segments_num):
        start = round(i * part_len, 2)
        end = round(start + part_len, 2)
        out_clip = clip.subclip(start, end)
        outputs.append(out_clip)
    return outputs