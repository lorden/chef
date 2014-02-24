from tts import TTS
if __name__ == '__main__':
    tts = TTS()
    text = raw_input('Say:')
    while text:
        tts.say(text)
        text = raw_input('Say:')
