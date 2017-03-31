import requests
from collections import namedtuple, defaultdict

Entity = namedtuple('Entity',['handle','roles','person','email','address','phone'])

def rdap(ip):
  response = requests.get('http://rdap.apnic.net/ip/{}'.format(ip))
  response.raise_for_status()
  data = response.json()
  entities = []
  entities.append(parse(data['entities'][0]))
  try:
    for entity in data['entities'][0]['entities']:
      entities.append(parse(entity))
  except KeyError:
    pass
  return entities

def parse(entity):
  collected = defaultdict(str)
  collected['handle'] = entity['handle']
  collected['roles'] = entity['roles']
  for item in entity['vcardArray'][1]:
    if item[0] == 'fn':
      collected['person'] = item[3]
    elif item[0] == 'adr':
      collected['address'] = item[1]['label']
    elif item[0] == 'email':
      collected['email'] = item[3]
    elif item[0] == 'tel':
      collected['phone'] = item[3]
  parsed = Entity(handle=collected['handle'],roles=collected['roles'],person=collected['person'],email=collected['email'],address=collected['address'],phone=collected['phone'])
  return parsed

