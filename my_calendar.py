from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build, Resource
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pytz

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = None

def prepare_service():
    """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    global service
    service = build('calendar', 'v3', credentials=creds)


def add_event():
    if service is None:
        prepare_service()
    summary = 'testowy event'
    location = None
    description = 'opis testowego eventu'

    date = datetime.datetime(2021, 5, 11, 18, 10)
    change = datetime.timedelta(minutes=25)

    timezone = 'Poland'
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': date.isoformat(),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': (date + change).isoformat(),
            'timeZone': timezone,
        },
        'colorId': 1,
    }

    event = service.events().insert(
        calendarId='smart.assistant.python@gmail.com',
        body=event,

    ).execute()
    print(event)

def list_events(n=5):
    if service is None:
        prepare_service()
    # Call the Calendar API
    now = datetime.datetime.now().astimezone(pytz.timezone('Europe/Warsaw')).isoformat()


    events_result = service.events().list(calendarId='smart.assistant.python@gmail.com', timeMin=now,
                                          maxResults=n, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    print('Upcoming', len(events), 'events')
    for event in events:
        start = datetime.datetime.fromisoformat(event['start'].get('dateTime', event['start'].get('date')))
        print(start, event['summary'])


def main():
    prepare_service()

    add_event()

    list_events(2)



if __name__ == '__main__':
    main()