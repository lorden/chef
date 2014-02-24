import os
import requests
import subprocess


class TTS:

    def __init__(self):
        self.root = 'http://translate.google.com/translate_tts?tl=en&q='
        self.temp_file = '/tmp/chef.mp3'

    def get_file(self, path):
        # urllib.urlretrieve(path, self.temp_file)
        with open(self.temp_file, 'wb') as handle:
            r = requests.get(path, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                handle.write(block)

    def say(self, text):
        self.get_file(self.root + text)
        subprocess.call(['mplayer', '-really-quiet', self.temp_file],
                        stdout=open(os.devnull, 'wb'),
                        stderr=open(os.devnull, 'wb'))
