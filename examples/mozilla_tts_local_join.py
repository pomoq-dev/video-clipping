import os.path
import subprocess

from vidlib import audio_tools
from vidlib import files_tools

# Run `docker-mozillatts % docker run -it -p 5002:5002 synesthesiam/mozillatts:en` in terminal to start the server (!!!)
# TODO: try custom model

text_files = files_tools.list_full_paths('../txts', '.txt')
text_files.sort()
for text_ind, text_file in enumerate(text_files):
    with open(text_file, 'r') as f:
        cur_text = f.read()
    DIR = "tts_audios"
    SILENT_FILE = 'silent500.wav'

    files_tools.clear_directory(DIR)
    audio_tools.generate_empty_wav(SILENT_FILE, duration=500)

    sentences = cur_text.split('.')
    audio_paths = []
    for ind, sentence in enumerate(sentences):
        if sentence == '':
            continue
        audo_path = os.path.join(DIR, "res_{}.wav".format(ind))
        audio_paths.append(audo_path)
        audio_paths.append(SILENT_FILE)

        text = sentence.replace('""', '\'') + "."
        # os.system("curl -G --output - --data-urlencode \"text={}\" 'http://localhost:5002/api/tts' > {}".format(text, audo_path))
        res = subprocess.run(["curl", "-G", "--output", "-", "--data-urlencode", "text={}".format(text),
                              "http://localhost:5002/api/tts"],
                             capture_output=True)

        with open(audo_path, "wb") as binary_file:
            binary_file.write(res.stdout)
        print(res)

    result_path = 'result_{}_tmp.wav'.format(text_ind)
    audio_tools.join_audios_by_path(audio_paths, result_path)
    audio_tools.change_samplerate_to_16k(result_path, result_path)
