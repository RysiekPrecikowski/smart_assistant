from gtts import gTTS
import playsound


def read_text(text, language):
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("text.mp3")
    playsound.playsound('text.mp3')
