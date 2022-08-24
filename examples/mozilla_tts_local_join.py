import os.path
import subprocess
from vidlib import files_tools
from vidlib import audio_tools

TEXT = """Hello. B words will come back with general entry. In this video I would like to show you how to download and install to meeting on your Windows laptop. So let's begin our video. So act fast. You need to open any kind of browser like that. I open my Chrome browser. Okay. Go ahead. Open your Chrome browser. Then go to Searsport and dove for. June just died. June then starts it again after search that you can get a link at first. There you can see. There you can see you can get a link at first. And on there you can see option download. Just click on this download option. Then it screened for download section and there have a option junk claimed for meeting and then have a option download and if your. Laptop is 64 bit. Then you just click it and if your laptop is not 64 bit, your laptop is 32. Then click on this option and you can download also add client. So my laptop is 64 bit. Then I select this download option. Then you need to wait for 100% downloading that you can see by downloading. So there you can see it's already downloaded. Then go on this street or option on the top right corner, then go to Download, then click on show in Florida. Then there you can see. Join in, install our exceptional double click. Then that you can see you're just installing unit weight, guys. So click on. Yes. So select on that. Then there you can see two already installed on your laptop. So you already installed on your laptop, but there had no option. You can see Drew icon is not showing your homepage. So if you want to make it home based, just go to start. Start and then type June that you can see June. Then. Right click on animals, then go to open file location. Then compete. Property. Then based here. Okay, so that you can see you already download and install on your laptop. So in this way you can download and install June on your laptop. So thank you everyone for watching this video."""
DIR = "tts_audios"
files_tools.clear_directory(DIR)


sentences = TEXT.split('.')
audio_paths = []
for ind, sentence in enumerate(sentences):
    if sentence == '':
        continue
    audo_path = os.path.join(DIR, "res_{}.wav".format(ind))
    audio_paths.append(audo_path)

    text = sentence.replace('""', '\'') + "."
    os.system("curl -G --output - --data-urlencode \"text={}\" 'http://localhost:5002/api/tts' > {}".format(text, audo_path))
    # res = subprocess.run(["curl", "-G", "--output", "-", "--data-urlencode", "text={}".format(text),
    #                       "http://localhost:5002/api/tts"],
    #                      capture_output=True)

    # with open(audo_path, "wb") as binary_file:
    #     binary_file.write(res.stdout)
    # print(res)

audio_tools.join_audios_by_path(audio_paths, 'result.wav')


