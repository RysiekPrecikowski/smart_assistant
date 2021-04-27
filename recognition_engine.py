from commands import Command, Commands_container as Commands
import speech_recognition as sr
from speaking import read_text
from typing import Optional


class Recognition_engine:
    def __init__(self, commands: Commands):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.commands = commands

    def get_transcript(self, all=False):
        with self.microphone as source:
            # r.adjust_for_ambient_noise(source) jak tego sie uzywa to na poczatku slucha zeby wylapac tlo
            print("say sth")
            audio = self.recognizer.listen(source)
            print("end")
        try:
            # print("language", self.commands.language)
            transcript = self.recognizer.recognize_google(audio, language=self.commands.language, show_all=False)
            if not all:
                return transcript
            else:
                return transcript, self.recognizer.recognize_google(audio, language=self.commands.language, show_all=True)

        except sr.UnknownValueError:
            pass

        if not all:
            return None
        else:
            return None, None

    def recognize_command(self, text: str = None, options: dict = None) -> tuple[Optional[Command], Optional[str]]:
        if text:
            print("TEXT", text)
            if text in self.commands:
                normalized = Command.normalize(text)
                print("FOUND COMMAND!!!")
                return self.commands[normalized], text
            else:
                for word in text.split(" "):
                    if word in self.commands:
                        print("FOUND COMMAND IN ONE WORD!!!")
                        normalized = Command.normalize(word)
                        return self.commands[normalized], text

        if options:
            print(options)
            for option in options['alternative']:
                print(option['transcript'])
                command = self.recognize_command(option['transcript'])[0]
                if command is not None:
                    return command, option['transcript']

        return None, None

    def listen_and_execute(self):
        transcript, all_transcripts = self.get_transcript(all=True)
        print(transcript)
        if transcript is None:
            return

        command, text = self.recognize_command(text=transcript, options=all_transcripts)
        if command is not None:
            command.execute(text)
