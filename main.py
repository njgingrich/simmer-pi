import json
import requests

def getHours(steam_id):
  url = 'http://localhost:8003/users/' + steam_id

  response = requests.get(url)
  if response.ok:
    data = json.loads(response.content)
    print(data)

getHours('76561198042101272')