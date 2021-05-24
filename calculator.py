import wolframalpha
from recognition_engine import Recognition_engine

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
        text = engine.get_transcript(text="what do you wanna calculate?")

    print(text)
    res = client.query(text)
    answer = ""
    try:
        answer = next(res.results).text
    except Exception as ex:
        print(ex)

    print(answer)
    return answer



if __name__ == '__main__':
    calculator("calculator")
    # test()