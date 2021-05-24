from gtts import gTTS
import playsound
import os
from threading import Thread

n=0
def run(text, language):
    global n
    n += 1
    speech = gTTS(text=text, lang=language, slow=False)
    print("speaking:", text)
    speech.save("text{}.mp3".format(n))
    playsound.playsound("text{}.mp3".format(n))
    os.remove("text{}.mp3".format(n))


def read_text(text, language = "en"):
    t = Thread(target=run, kwargs={'text': text, 'language': language})
    t.start()
    # t.join()
