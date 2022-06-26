import sys
import json
import datetime
from googlecalendar import GoogleCalendar

calendarId = sys.argv[1]
calendar = GoogleCalendar(calendarId)

timeMin = None
timeMax = None
if len(sys.argv) >= 3:
  timeMin = datetime.datetime.fromisoformat(sys.argv[2])

events = calendar.get_events(timeMin, timeMax)

if not events:
  print('ゴミの収集はありません。')
else:
  print(events[0]['summary'] + 'の日です。')
