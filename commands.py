import unicodedata
from speaking import read_text

class Command:
    def __init__(self, text, action=None):
        self.language = None
        self.text = text
        self.action = action
        self.normalized = Command.normalize(self.text)

    def __repr__(self):
        # print(self.text, self.action)
        return self.text

    def __eq__(self, other):
        return self.normalized == other.normalized

    def __hash__(self):
        return hash(self.normalized)

    def execute(self, *args):
        text = "you said " + self.text
        # read_text(text, self.language)

        # print("ARGS", *args)
        if len(args) == 0:
            return self.action()
        else:
            return self.action(*args)

    @staticmethod
    def normalize(text):
        if text is not None:
            # print("NORMALIZED: ", unicodedata.normalize('NFKD', text).lower().replace(u'ł', 'l').encode('ASCII', 'ignore').decode("utf-8"))
            return str(unicodedata.normalize('NFKD', text).lower().replace(u'ł', 'l').encode('ASCII', 'ignore').decode("utf-8"))




class Commands_container:
    def __init__(self, language="en-US", language_for_speech=None):
        self.language = language
        if language_for_speech is None:
            self.language_for_speech = language.split("-")[0]
        else:
            self.language_for_speech = language_for_speech
        self.commands = {}  # type: dict[Command]

    def add_command(self, command: Command):
        if command in self.commands:
            print("command already exists")
            return
        self.commands[command.normalized] = command
        command.language = self.language_for_speech

    def __getitem__(self, key) -> Command:
        return self.commands[Command.normalize(key)]

    def __contains__(self, item):
        if type(item) == str:
            return Command.normalize(item) in self.commands

        return item in self.commands

