import os
import random

from moviepy import editor as mpe
from pydub import AudioSegment
from tqdm import tqdm


def split_audio_to_parts(audio, piece_duration=3):
    sub_audios = []
    piece_cnt = round(audio.duration / piece_duration)
    for i in range(0, piece_cnt + 1):
        start = i * piece_duration
        if start >= audio.duration:
            break
        end = start + piece_duration
        if end >= audio.duration:
            break
        sub_audio = audio.subclip(start, end)
        sub_audios.append(sub_audio)
    return sub_audios


def audio_change_for_video(source_audio, piece_duration=3, video=None):
    audio = source_audio
    if video != None:
        audio = source_audio.subclip(0, video.duration)

    sub_audios = split_audio_to_parts(audio, piece_duration)
    return mpe.concatenate_audioclips(sub_audios)


def save_audio(audio, path):
    audio.write_audiofile(path, codec='aac')


def mp32wav(mp3_path, wav_path, remove_original=False):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
    if remove_original:
        os.remove(mp3_path)


def m4a2wav(m4a_path, wav_path, remove_original=False):
    sound = AudioSegment.from_file(m4a_path, format='m4a')
    sound.export(wav_path, format='wav')
    if remove_original:
        os.remove(m4a_path)


def join_audios_by_path(audio_clip_paths, output_path, verbose=1):
    """
        Concatenates two or more audio files into one audio file using PyDub library
        and save it to `output_path`. A lot of extensions are supported, more on PyDub's doc.
        """

    def get_file_extension(filename):
        """A helper function to get a file's extension"""
        return os.path.splitext(filename)[1].lstrip(".")

    clips = []
    # wrap the audio clip paths with tqdm if verbose
    audio_clip_paths = tqdm(audio_clip_paths, "Reading audio file") if verbose else audio_clip_paths
    for clip_path in audio_clip_paths:
        # get extension of the audio file
        extension = get_file_extension(clip_path)
        # load the audio clip and append it to our list
        clip = AudioSegment.from_file(clip_path, extension)
        clips.append(clip)

    final_clip = clips[0]
    range_loop = tqdm(list(range(1, len(clips))), "Concatenating audio") if verbose else range(1, len(clips))
    for i in range_loop:
        # looping on all audio files and concatenating them together
        # ofc order is important
        final_clip = final_clip + clips[i]
    # export the final clip
    final_clip_extension = get_file_extension(output_path)
    if verbose:
        print(f"Exporting resulting audio file to {output_path}")
    final_clip.export(output_path, format=final_clip_extension)
