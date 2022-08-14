import moviepy.editor
import os
import random
import fnmatch
from pydub import AudioSegment

PATH = '/Users/andrey.matveev/input.mp4'
SEGMENTS = 10

clip = moviepy.editor.VideoFileClip(PATH)
part_len = clip.duration / SEGMENTS

outputs = []
for i in range(0, SEGMENTS):
    start = round(i * part_len, 2)
    end = round(start + part_len, 2)
    out_clip = clip.subclip(start, end)
    outputs.append(out_clip)

random.shuffle(outputs)
out = moviepy.editor.concatenate_videoclips(outputs)
out.write_videofile('out.mp4')

