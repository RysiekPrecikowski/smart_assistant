import datetime
from pprint import pprint
from recognition_engine import Recognition_engine
import lorem

end = '$%$'
end_date = '%$%'

def add_note(text):
    print(text)

    if len(text) < 2:
        engine = Recognition_engine()
        text = engine.get_transcript(text="dictate the note")

    if text is None:
        return

    with open('notes.n', 'a') as file:
        date = datetime.datetime.now()

        file.write('Note created: ')
        file.write(date.__str__()+end_date)

        file.write(text+end)

def get_notes(n):
    notes = {}

    try:
        if len(n) > 0:
            n = int(n)
        else:
            n = 1
    except:
        n = 1

    with open('notes.n', 'r') as file:
        text = file.read()
        splitted = text.split(end)
        splitted.remove('')

        print("N", type(n))

        for s in splitted[::-1][:n]:
            print(s)
            time, note = s.split(end_date)
            time = time.replace('Note created: ', '')

            time = datetime.datetime.fromisoformat(time)
            notes[time] = note

    res = ""
    for date, note in notes.items():
        res += "Time: {}-{}-{} {:d}:{:02d}\nNote: {}\n".format(date.year, date.month, date.day, date.hour, date.minute, note)
    return res

def get_notes_between(notes, from_time, to_time):

    for time, note in notes.items():
        if from_time <= time and time <= to_time:
            print(time, note)


def clear_notes():
    with open('notes.n', 'w') as _:
        pass

def main():
    # clear_notes()
    add_note("create new note" + lorem.sentence())
    notes = get_notes("")
    pprint(notes)
    # get_notes_between(notes, datetime.datetime(2021, 5, 11, 14, 30), datetime.datetime(2021, 5, 11, 15, 10))

if __name__ == '__main__':
    main()

# if __name__ == '__main__':
#     clear_notes()