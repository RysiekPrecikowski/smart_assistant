import unicodedata
from speaking import read_text
from pprint import pprint
import ast

from collections import Counter
from math import inf

def n_gram(tokens, n):
    res = Counter()

    for i in range(len(tokens) - n + 1):
        if type(tokens) is str:
            seq = tokens[i:i+n]
        elif type(tokens[i]) is str:
            seq = ' '.join(tokens[i:i+n])
        else:
            seq = tuple(tokens[i:i+n])

        res[seq] += 1

    return res

def cosine_metric(x, y, n=2):
    x_n_gram = n_gram(x, n)
    y_n_gram = n_gram(y, n)



    s = sum(x_n_gram[g] * y_n_gram[g] for g in x_n_gram.keys() & y_n_gram.keys())

    _len = lambda ngram: sum(v*2 for v in ngram.values()) ** 0.5

    if _len(x_n_gram) * _len(y_n_gram) == 0:
        return inf

    return 1 - s / (_len(x_n_gram) * _len(y_n_gram))




class Command:
    def __init__(self, text, action=None, action_args=None):
        self.language = None
        self.text = text
        self.description = None
        self.action = action
        self.action_args = action_args
        self.normalized = Command.normalize(self.text)

    def __repr__(self):
        # print(self.text, self.action)
        # return self.text
        return "'"+self.action.__name__+"'"

    def __eq__(self, other):
        return self.normalized == other.normalized

    def __hash__(self):
        return hash(self.normalized)

    def execute(self, *args):
        # text = "you said " + self.text
        # read_text(text, self.language)

        # print("ARGS", *args)

        if self.action_args is None:
            if len(args) == 0:
                res = self.action()
            else:
                res = self.action(*args)
        else:
            res = self.action(self.action_args)

        if type(res) == str:
            read_text(res)
        return res
    @staticmethod
    def normalize(text):
        if text is not None:
            # print("NORMALIZED: ", unicodedata.normalize('NFKD', text).lower().replace(u'ł', 'l').encode('ASCII', 'ignore').decode("utf-8"))
            return str(unicodedata.normalize('NFKD', text).lower().replace(u'ł', 'l').encode('ASCII', 'ignore').decode("utf-8"))

    def normalize_with_accuracy(self, text, max_diff=0.5):
        text = Command.normalize(text)

        if len(text) >= len(self.text):
            compare_to = text[:len(self.text) +1]
            compare_with = self.text
        else:
            compare_to = text
            compare_with = self.text[:len(text) +1]


        diff = cosine_metric(compare_to, compare_with)
        print(self, diff)
        if diff <= max_diff:
            return self.text, compare_to
        else:
            return None, None



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

    def check_accuracy(self, text, max_diff=0.6):
        for command in self.commands.values():
            matched, modified = command.normalize_with_accuracy(text, max_diff)
            if matched is not None:
                return matched, modified
        return None, None

    def get_item(self, key):
        if Command.normalize(key) not in self.commands:
            print("NO")
            matched = self.check_accuracy(key)[0]
            if matched is not None:
                print("FOUND!!!!")
                return self.commands[matched]
            return None

    def __getitem__(self, key) -> Command:
        return self.commands[Command.normalize(key)]

    def __contains__(self, item):
        if type(item) == str:
            return Command.normalize(item) in self.commands

        return item in self.commands





    def save_to_file(self, name='commands'):
        with open(name, 'w') as f:
            f.write(self.commands.__str__())

    def read_from_file(self, name='commands', module='commands_lib'):
        with open(name, 'r') as f:
            text = f.read()

            mod = __import__(module)

            self.commands = ast.literal_eval(text)

            for key in self.commands.keys():
                self.commands[key] = Command(key, getattr(mod, self.commands[key]))

