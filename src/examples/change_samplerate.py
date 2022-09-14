from src.vidliboba import audio_tools

audio_tools.m4a2wav('audio0.m4a', 'audio0.wav')
audio_tools.change_samplerate_to_16k('audio0.wav', 'audio0_16000.wav')
