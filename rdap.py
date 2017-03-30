import requests

def rdap(ip):
  response = requests.get('https://rdap.apnic.net/ip/{}'.format(ip))
  response.raise_for_status()
  return response.json()
