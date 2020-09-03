from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import re
from datetime import datetime

SCOPES = 'https://www.googleapis.com/auth/gmail.modify'

def mail():

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API to fetch INBOX
    querry = "from:no-reply@tilburguniversity.edu is:unread subject:Tilburg University Sports Center Online booking"

    results = service.users().messages().list(userId='me',labelIds = ['INBOX'], q = querry).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No messages found.")
    else:
        for message in messages:
            service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            date_time = re.findall("\d{2}[-/]\d{2}[-/]\d{4}\s\d{2}[:/]\d{2}", str(msg))
            start = datetime.strptime(date_time[0], '%d-%m-%Y %H:%M').isoformat()
            end = datetime.strptime(date_time[1], '%d-%m-%Y %H:%M').isoformat()
            # print(start, end)
            return start, end
print(mail())
# if __name__ == '__main__':
#     mail()
