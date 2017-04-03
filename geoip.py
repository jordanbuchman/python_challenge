import requests
from collections import namedtuple

Geo = namedtuple('Geo',
                 ['country_code',
                  'country_name',
                  'region_code',
                  'region_name',
                  'city',
                  'zip_code',
                  'time_zone',
                  'latitude',
                  'longitude',
                  'metro_code'])


def geoip(ip):
    response = requests.get('https://freegeoip.net/json/{}'.format(ip))
    response.raise_for_status()
    data = response.json()
    del data['ip']
    geo = Geo(**data)
    return geo
