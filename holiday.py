import sys
import json
import datetime
from googlecalendar import GoogleCalendar

calendarId = 'ja.japanese#holiday@group.v.calendar.google.com'
calendar = GoogleCalendar(calendarId)
timeMin = None
timeMax = None

if len(sys.argv) >= 2:
  timeMin = datetime.datetime.fromisoformat(sys.argv[1])
if len(sys.argv) >= 3:
  timeMax  = datetime.datetime.fromisoformat(sys.argv[2])

events = calendar.get_events(timeMin, timeMax)

event = {}
if not events:
  print()
else:
  print(events[0]['summary'])

