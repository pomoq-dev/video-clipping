import moviepy.editor
import os
import random
import fnmatch

from src.vidliboba import video_tools

directory = '/directory/to/videos/'
xdim = 854
ydim = 480
ext = "*mp4"
length = 10

outputs=[]

# compile list of videos
inputs = [os.path.join(directory,f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and fnmatch.fnmatch(f, ext)]

for i in inputs:

    # import to moviepy
    clip = moviepy.editor.VideoFileClip(i).resize( (xdim, ydim) ) 

    # select a random time point
    start = round(random.uniform(0,clip.duration-length), 2) 

    # cut a subclip
    out_clip = clip.subclip(start,start+length)

    outputs.append(out_clip)

# combine clips from different videos
collage = video_tools.concatenate_videos(outputs)
video_tools.save_video(collage, 'out.mp4')