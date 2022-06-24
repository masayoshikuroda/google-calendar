from __future__ import print_function
import datetime
import os.path
import sys
from googleapiclient.discovery import build
from google.auth import load_credentials_from_file

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
PWD = os.path.dirname(__file__)

if len(sys.argv) > 1:
    CAL_ID = sys.argv[1]
else:
    with open(PWD + '/calendar_id', 'r', encoding='UTF-8') as f:
        CAL_ID = str.strip(f.read())
 
creds = load_credentials_from_file(PWD + '/credentials.json', SCOPES)[0]
service = build('calendar', 'v3', credentials=creds)

tz = datetime.timezone(datetime.timedelta(hours=9))
now = datetime.datetime.now()
timeMin = datetime.datetime(now.year, now.month, now.day, tzinfo=tz)
timeMax  = timeMin + datetime.timedelta(days=1)

events_result = service.events().list(
        calendarId=CAL_ID,
        timeMin = timeMin.isoformat(),
        timeMax = timeMax.isoformat(),
        timeZone = None,
        maxResults=1,
        singleEvents=True,
        orderBy='startTime',
        ).execute()
events = events_result.get('items', [])


if not events:
    print('ゴミの収集はありません。')
else:
    print(events[0]['summary'] + 'の日です。')

