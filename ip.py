import geoip
import rdap
from requests import HTTPError
from haversine import haversine
import copy


class IP(object):

    def __init__(self, address):
        self.address = address
        try:
            self.geo = geoip.geoip(self.address)
        except HTTPError:
            self.geo = Geo('', '', '', '', '', '', '', '', '', '')
        try:
            self.entities = rdap.rdap(self.address)
        except HTTPError:
            self.entities = []

    def in_bbox(self, upper_right, bottom_left):
        return bottom_left[0] <= self.geo.latitude <= upper_right[0] and bottom_left[1] <= self.geo.longitude <= upper_right[1]

    def in_radius(self, center, radius):
        return haversine((self.geo.latitude, self.geo.longitude), center, miles=True) <= radius

    def field_match(self, field, pattern):
        return pattern == self.geo._asdict()[field]

    def check_roles(self, roles):
        rolelist = [entity.roles for entity in self.entities]
        rolelist = [item for sublist in rolelist for item in sublist]
        rolelist = set(rolelist)
        roles = set(roles)
        return roles.issubset(rolelist)

    def only_roles(self, roles):
        roles = set(roles)
        self.entities = list(filter(lambda entity: not set(
            entity.roles).isdisjoint(roles), self.entities))
        return True
