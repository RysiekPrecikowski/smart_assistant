from commands import Command, Commands_container as Commands
import speech_recognition as sr
from speaking import read_text

class Recognition_engine:
    def __init__(self, commands: Commands):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.commands = commands



    def recognize(self):
        with self.microphone as source:
            # r.adjust_for_ambient_noise(source) jak tego sie uzywa to na poczatku slucha zeby wylapac tlo
            print("say sth")
            audio = self.recognizer.listen(source)
            print("end")
        try:
            transcript = self.recognizer.recognize_google(audio, language=self.commands.language)
            print(transcript)
            if transcript not in self.commands:
                all = self.recognizer.recognize_google(audio, language=self.commands.language, show_all=True)
                print(all)

                for i in all['alternative']:
                    # for alt in i['transcript']:
                    print(i['transcript'])
                    if i['transcript'] in self.commands:
                        normalized = Command.normalize(i['transcript'])
                        self.commands[normalized].execute()

                read_text("nie rozpoznalem komendy", "pl")

            else:
                # return Command.normalize(transcript)
                normalized = Command.normalize(transcript)
                self.commands[normalized].execute()

        except sr.UnknownValueError:
            pass
