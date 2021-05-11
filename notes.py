import datetime
from pprint import pprint
import lorem

end = '$%$'
end_date = '%$%'

def add_note(text):
    with open('notes.n', 'a') as file:
        date = datetime.datetime.now()

        file.write('Note created: ')
        file.write(date.__str__()+end_date)

        file.write(text+end)

def get_notes():
    notes = {}
    with open('notes.n', 'r') as file:
        text = file.read()
        splitted = text.split(end)
        splitted.remove('')
        for s in splitted:
            time, note = s.split(end_date)
            time = time.replace('Note created: ', '')

            time = datetime.datetime.fromisoformat(time)
            notes[time] = note

    # pprint(notes)
    return notes

def get_notes_between(notes, from_time, to_time):

    for time, note in notes.items():
        if from_time <= time and time <= to_time:
            print(time, note)


def clear_notes():
    with open('notes.n', 'w') as _:
        pass

def main():
    # clear_notes()
    add_note(lorem.sentence())
    notes = get_notes()
    pprint(notes)
    # get_notes_between(notes, datetime.datetime(2021, 5, 11, 14, 30), datetime.datetime(2021, 5, 11, 15, 10))

if __name__ == '__main__':
    main()