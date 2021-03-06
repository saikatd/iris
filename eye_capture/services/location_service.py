from math import atan2, pi, sin, cos, sqrt

class GeoCalculator():

    @staticmethod
    def distance(p1, p2):
      R = 6378137
      dLat = GeoCalculator.rad(p2.lat - p1.lat)
      dLong = GeoCalculator.rad(p2.long - p1.long)
      a = sin(dLat / 2) * sin(dLat / 2) +\
        cos(GeoCalculator.rad(p1.lat)) * cos(GeoCalculator.rad(p2.lat)) *\
        sin(dLong / 2) * sin(dLong / 2)
      c = 2 * atan2(sqrt(a), sqrt(1 - a))
      d = R * c
      return abs(d)

    @staticmethod
    def rad(x):
      return float(x) * pi / 180

    @staticmethod
    def average_speed(loc_final, loc_initial, delta_time):
        return GeoCalculator.distance(loc_final, loc_initial) / delta_time * 60

class Traffic():

    EYES_PER_MIN = 1/20.0
    GRADIENT_NORMALIZE = 100

    @staticmethod
    def eyes(loc_final, loc_initial, delta_time):
        return (Traffic.EYES_PER_MIN) * Traffic.traffic_factor(loc_final, loc_initial, delta_time)

    @staticmethod
    def traffic_factor(loc_final, loc_initial, delta_time):
        speed = GeoCalculator.average_speed(loc_final, loc_initial, delta_time)
        return abs(100 - speed)


class SessionBreakPoint():

    DELTA_TIME_THRESHOLD = 20
    DISTANCE_PER_MINUTE_UPPER_BOUND = 1.5

    @staticmethod
    def is_session_breakpoint(delta_time, distance):
        return SessionBreakPoint.delta_time_too_large(delta_time) and SessionBreakPoint.distance_too_large(distance) and delta_time != 0

    @staticmethod
    def delta_time_too_large(delta_time):
        return delta_time <= SessionBreakPoint.DELTA_TIME_THRESHOLD

    @staticmethod
    def distance_too_large(distance):
        return distance <= SessionBreakPoint.DISTANCE_PER_MINUTE_UPPER_BOUND

class Point():
    def __init__(self, lat, lng):
        self.lat = lat
        self.long = lng
