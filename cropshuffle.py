import random
import subprocess
from subprocess import run

import moviepy.editor as mpe

PATH = '/Users/andrey.matveev/VIDEO/input.mp4'
PATH_AUDIO = '/Users/andrey.matveev/VIDEO/input.m4a'
SOURCE_VIDEO_NAME = 'sourcevideo.mp4'
SOURCE_AUDIO_NAME = 'sourceaudio.m4a'
SEGMENTS = 100


def print_subprocess_output(proc):
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        print(line)
        line = proc.stderr.readline()
        if not line:
            break
        print(line)


def download_video_and_audio(yt_url):
    text = run(['yt-dlp', '-F', f"{yt_url}", '-o', SOURCE_VIDEO_NAME], capture_output=True).stdout
    lines = str(text).split(sep="\\n")
    dl_video_id = ''
    dl_audio_id = ''
    for line in lines:
        print(line)
        spl = line.split()
        if len(spl) < 2:
            continue
        id = spl[0]
        format = spl[1]
        if format == 'mp4':
            dl_video_id = id
        elif format == 'm4a':
            dl_audio_id = id
    print('Downloading video...')
    subprocess.run(['yt-dlp', '-f', dl_video_id, f"{yt_url}", '-o', SOURCE_VIDEO_NAME], stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    print('Downloading audio...')
    subprocess.run(['yt-dlp', '-f', dl_audio_id, f"{yt_url}", '-o', SOURCE_AUDIO_NAME], stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    print('Completed')


def download_video_with_audio(yt_url):
    p = subprocess.Popen(['yt-dlp', '-f', 'best', f"{yt_url}", '-o', SOURCE_VIDEO_NAME], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    print_subprocess_output(p)
    print(42)


def add_audio_to_video(path_video, path_audio):
    init_clip = mpe.VideoFileClip(path_video)
    audio_background = mpe.AudioFileClip(path_audio)
    # final_audio = mpe.CompositeAudioClip([clip.audio, audio_background])
    final_clip = init_clip.set_audio(audio_background)
    return final_clip


download_video_and_audio('https://www.youtube.com/watch?v=0PvbixQ_tJ0')
clip = add_audio_to_video(SOURCE_VIDEO_NAME, SOURCE_AUDIO_NAME)
part_len = clip.duration / SEGMENTS

outputs = []
for i in range(0, SEGMENTS):
    start = round(i * part_len, 2)
    end = round(start + part_len, 2)
    out_clip = clip.subclip(start, end)
    outputs.append(out_clip)

random.shuffle(outputs)
out = mpe.concatenate_videoclips(outputs)
out.write_videofile('out.mp4', codec= 'mpeg4', audio_codec='aac')
