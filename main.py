import unicodedata

import speech_recognition as sr
from time import sleep
from pprint import pprint
import os

from gtts import gTTS
import playsound
from speaking import read_text


from commands import Command, Commands_container as Commands



def shutdown():
    print("shutdown")
    # os.system("shutdown /s /t 1") #windows
    # os.system("shutdown now -h") #linux



language = "pl-PL"

def listen(commands):
    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        # r.adjust_for_ambient_noise(source) jak tego sie uzywa to na poczatku slucha zeby wylapac tlo
        print("say sth")
        audio = r.listen(source)
        # r.listen_in_background(source)
        print("end")
    try:
        transcript = r.recognize_google(audio, language=commands.language)
        print(transcript)
        if transcript not in commands:
            all = r.recognize_google(audio, language=commands.language, show_all=True)
            print(all)

            for i in all['alternative']:
                # for alt in i['transcript']:
                print(i['transcript'])
                if i['transcript'] in commands:
                    return Command.normalize(i['transcript'])

            read_text("nie rozpoznalem komendy", "pl")

            return None

    except sr.UnknownValueError:
        return None

    return Command.normalize(transcript)




def main():
    commands = Commands()

    commands.add_command(Command("Wyłącz komputer", shutdown))
    commands.add_command(Command("Zrestartuj komputer", "dziala restart"))

    print(commands)
    while True:
        idk = listen(commands)
        print(idk)

        if idk is not None:
            commands[idk].execute()



if __name__ == '__main__':
    main()
