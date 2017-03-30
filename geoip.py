import requests

def geoip(ip):
  response = requests.get('https://freegeoip.net/json/{}'.format(ip))
  response.raise_for_status()
  return response.json()
