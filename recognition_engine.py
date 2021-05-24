from commands import Command, Commands_container as Commands
import speech_recognition as sr
from speaking import read_text
from typing import Optional



class Recognition_engine:
    def __init__(self, commands: Commands = None):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        if commands is None:
            commands = Commands()
        self.commands = commands

    def get_transcript(self, all=False, text=None):
        with self.microphone as source:
            # r.adjust_for_ambient_noise(source) jak tego sie uzywa to na poczatku slucha zeby wylapac tlo
            if text:
                read_text(text)
            print("say sth")
            audio = self.recognizer.listen(source)
            print("end")
        try:
            # print("language", self.commands.language)
            transcript = self.recognizer.recognize_google(audio, language=self.commands.language, show_all=False)

            print("TRANSCRIPT", transcript)

            if not all:
                return transcript
            else:
                return transcript, self.recognizer.recognize_google(audio, language=self.commands.language, show_all=True)

        except sr.UnknownValueError:
            print("ERROR IN RECOGNIZE")

        if not all:
            return None
        else:
            return None, None

    def recognize_command(self, text: str = None) -> tuple[Optional[Command], Optional[str]]:
        if text:
            if text not in self.commands:
                command = self.commands.get_item(text)
                if command is None:
                    return None, None
                print("COMMAND", command)
                if command.text == text[:len(command.text)]:
                    return command, text[len(command.text) +1:]
                return command, ""
            else:
                command = self.commands[text]
                return command, text[len(command.text)+1:].lower()

        print(text)
        return None, None

    def listen_and_execute(self):
        transcript = self.get_transcript(all=False)
        print(transcript)
        if transcript is None:
            return

        command, text = self.recognize_command(text=transcript)
        if command is not None:
            return command.execute(text)
