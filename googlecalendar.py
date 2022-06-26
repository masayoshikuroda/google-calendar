from __future__ import print_function
import os.path
import sys
import datetime
from googleapiclient.discovery import build
from google.auth import load_credentials_from_file

class GoogleCalendar:
  BASE_PATH = os.path.dirname(os.path.abspath(__file__))
  scopes = ['https://www.googleapis.com/auth/calendar.readonly']
  credentials = load_credentials_from_file(os.path.join(BASE_PATH, 'credentials.json'), scopes)[0]
  service = build('calendar', 'v3', credentials=credentials)

  def __init__(self, calendarId):
    self.calendarId = calendarId 

  def get_events(self, timeMin=None, timeMax=None):
    tz = datetime.timezone(datetime.timedelta(hours=9))
    now = datetime.datetime.now(tz)
    if timeMin is None:
      timeMin = datetime.datetime(now.year, now.month, now.day, tzinfo=tz)
    if timeMax is None:
      timeMax  = timeMin + datetime.timedelta(days=1)

    events_result = self.service.events().list(
      calendarId = self.calendarId,
      timeMin = timeMin.isoformat(),
      timeMax = timeMax.isoformat(),
      timeZone = None,
      maxResults = 1,
      singleEvents = True,
      orderBy = 'startTime',
    ).execute()
    return events_result.get('items', [])

if __name__ == '__main__':
  calendar = GoogleCalendar(sys.argv[1])
  timeMin = None
  timeMax = None
  if len(sys.argv) >= 3:
    # iso format with timezone. ex) 2022-06-27T00:00:00+09:00
    timeMin = datetime.datetime.fromisoformat(sys.argv[2])
  if len(sys.argv) >= 4:
    timeMax  = datetime.datetime.fromisoformat(sys.argv[3])

  events = calendar.get_events(timeMin, timeMax)
  print(events)

