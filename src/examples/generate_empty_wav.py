from pydub import AudioSegment

one_sec_segment = AudioSegment.silent(duration=400)
one_sec_segment.export('silent400.wav', format='wav')