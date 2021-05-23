import wolframalpha
from recognition_engine import Recognition_engine
from commands import Commands_container as Commands, Command
from math import sqrt
from speaking import read_text
import word2number as w2n


def calculator_old(args):
    #TODO zamiast wolframa?
    def add(numbers):
        if len(numbers) == 0:
            return None
        res = 0
        print(numbers)
        for a in numbers:
            res += a
        return res

    def subtract(numbers):
        if len(numbers) != 2:
            return None
        return numbers[1] - numbers[0]

    def multiply(numbers):
        if len(numbers) == 0:
            return None
        res = 1
        print(numbers)
        for a in numbers:
            res *= a
        return res

    def divide(numbers):
        if len(numbers) != 2:
            return None
        return numbers[0] / numbers[1]

    def square_root(number):
        print(number[0])
        return sqrt(number[0])

    def prepare(text, command):
        if command is not None and text is not None:
            text = text.replace(command.normalized, "")
            print(text)
            if command.action == add or command.action == multiply:
                text = text.replace("+", "and")

                numbers = text.split("and")

            if command.action == subtract:
                numbers = text.split("from")

            if command.action == divide:
                numbers = text.split("by")

            if command.action == square_root:
                numbers = [text.split("of")[1]]

            print(numbers)
            numbers = [w2n.word_to_num(number) for number in numbers]
            print(numbers)
            return numbers
        else:
            return None

    print("calculator")

    commands = Commands()
    commands.add_command(Command("add", add))
    commands.add_command(Command("subtract", subtract))
    commands.add_command(Command("multiply", multiply))
    commands.add_command(Command("divide", divide))
    commands.add_command(Command("root", square_root))

    test_cases = ["add twenty three and one",
                  "subtract two from twenty one",
                  "multiply two and three and twenty one",
                  "divide six by two",
                  "root of thirty six"]

    engine = Recognition_engine(commands)

    transcript, options = engine.get_transcript(all=True)
    #
    # transcript = "add one and two"

    print("TRANSCRIPT", transcript)
    print("OPTIONS", options)

    def xd(transcript):
        transcript = transcript.replace("+", "and +")
        return transcript

    if transcript is not None:
        transcript = xd(transcript)
        command, transcript = engine.recognize_command(text=transcript, options=options)

        print("XD", transcript, command)
        if command is not None:
            transcript = xd(transcript)
            print(transcript)
            normalized = Command.normalize(transcript)
            print("COMMAND", command)

            res = command.execute(prepare(normalized, command))
            read_text("result of " + transcript + " is " + str(res), language="en-US")  # TODO language :c





def test():
    test_cases = ["add twenty three and one",
                  "subtract two from twenty one",
                  "multiply two and three and twenty one",
                  "divide six by two",
                  "root of thirty six"]

    test_cases = ["calculator " + test_cases[i] for i in range(len(test_cases))]

    test_ans = ['24', '19', '126', '3', '6']

    for test, ans in zip(test_cases, test_ans):


        res = calculator(test)

        print(ans == res)


def calculator(text):
    client = wolframalpha.Client('4QAX6Y-3UTUETXHRV')

    print(text)

    if len(text) < 1:
        engine = Recognition_engine()
        text = engine.get_transcript()


    res = client.query(text)

    answer = next(res.results).text

    print(answer)
    return answer



if __name__ == '__main__':
    calculator("calculator")
    # test()