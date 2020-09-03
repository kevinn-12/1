from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from gmail import mail

# If modifying these scopes, delete the file token.pickle.calendar.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def calendar(start, end):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle.calendar stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle.calendar'):
        with open('token.pickle.calendar', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials-calendar.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle.calendar', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    start = str(start)
    end = str(end)

    event = {
           "summary": 'Gym',
           "start": {"dateTime": start, "timeZone": 'Europe/Amsterdam'},
           "end": {"dateTime": end, "timeZone": 'Europe/Amsterdam'}
       }
    service.events().insert(calendarId='primary', body=event).execute()

dates = mail()
for start, end in zip(dates[0::2], dates[1::2]):
    # print(start, end)
    calendar(start, end)

# if __name__ == '__main__':
#     calendar()
