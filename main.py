import json
import requests
import time
import led as LED

def getMinutes(steam_id):
  url = 'http://localhost:8003/users/' + steam_id

  response = requests.get(url)
  if response.ok:
    data = json.loads(response.content)
    return data['result']['playtimes']['totals']['two_weeks']

leds = LED.Bar()
while True:
  print('Getting hours for user')
  mins = getMinutes('76561198042101272')
  print('Found {0} mins'.format(mins))
  leds.determine_leds(mins)
  time.sleep(30)

