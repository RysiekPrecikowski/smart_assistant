from gtts import gTTS
import playsound
import os


def read_text(text, language):
    speech = gTTS(text=text, lang=language, slow=False)
    print("speaking:", text)
    speech.save("text.mp3")
    playsound.playsound('text.mp3')
    os.remove("text.mp3")
