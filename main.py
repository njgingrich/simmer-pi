import json
import requests
import time
import led as LED

def getHours(steam_id):
  url = 'http://localhost:8003/users/' + steam_id

  response = requests.get(url)
  if response.ok:
    data = json.loads(response.content)
    return data['result']['playtimes']['totals']['two_weeks']

leds = LED.Bar()
while True:
  print('Getting hours for user')
  hours = getHours('76561198042101272')
  print('Found {0} hours'.format(hours))
  leds.determine_leds()
  time.sleep(30)

