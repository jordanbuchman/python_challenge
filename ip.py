import geoip
import rdap
import math

class IP(object):
  def __init__(self,address):
    self.address = address
    self.geo = geoip.geoip(self.address)
    self.entities = rdap.rdap(self.address)

  def in_bbox(self,upper_right, bottom_left):
    return  self.geo.latitude <= upper_right[0] and self.geo.latitude >= bottom_left[0]and self.geo.longitude <= upper_right[1] and self.geo.longitude>= bottom_left[1]

  def in_radius(self,center,radius):
    return math.sqrt(math.pow(center[0]-self.geo.latitude,2)+math.pow(center[1]-self.geo.longitude,2)) <= radius

