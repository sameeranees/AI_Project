import os
import sys
import time
with open(os.devnull, 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    from pygame import mixer
    sys.stdout = oldstdout
def Call(txt):
    from gtts import gTTS
    tts = gTTS(text=txt, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
    for i in range(5):
        mixer.init()
        mixer.music.load('good.mp3')
        mixer.music.play()
        time.sleep(1.5)
        mixer.music.stop()
        mixer.quit()
    delete()
def delete():
    time.sleep(2)
    mixer.init()
    mixer.music.load("hello.mp3")
    os.remove("good.mp3")
