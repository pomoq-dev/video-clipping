import random
import subprocess
from subprocess import run


def download_video_and_audio(yt_url, res_video_path, res_audio_path):
    text = run(['yt-dlp', '-F', f"{yt_url}"], capture_output=True).stdout
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
    subprocess.run(['yt-dlp', '-f', dl_video_id, f"{yt_url}", '-o', res_video_path], stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    print('Downloading audio...')
    subprocess.run(['yt-dlp', '-f', dl_audio_id, f"{yt_url}", '-o', res_audio_path], stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    print('Completed')


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


def download_video_with_audio(yt_url):
    p = subprocess.Popen(['yt-dlp', '-f', 'best', f"{yt_url}", '-o', SOURCE_VIDEO_NAME], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    print_subprocess_output(p)
    print(42)