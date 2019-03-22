# https://www.reddit.com/r/dailyprogrammer/comments/8i5zc3/20180509_challenge_360_intermediate_find_the/

from opensky_api import OpenSkyApi
from scipy.spatial import distance

EIFFEL = (48.8584, 2.2945)
JFK = (40.6413, 73.7781)

api = OpenSkyApi()
states = api.get_states()

dist_Eiffel, dist_jfk = [], []
for s in states.states:
    origin, callsign, identifier, geo_altitude, = s.origin_country, s.callsign, s.icao24, s.geo_altitude
    latitude, longitude = s.latitude, s.longitude
    if latitude and longitude:
        distanceFromEiffel = distance.euclidean(EIFFEL, (latitude, longitude))
        distanceFromJFK = distance.euclidean(JFK, (latitude, longitude))
        dist_Eiffel.append((distanceFromEiffel, origin, callsign, identifier, geo_altitude))
        dist_jfk.append((distanceFromJFK, origin, callsign, identifier, geo_altitude))
print("Closest to the Eifel Tower:", min(dist_Eiffel, key=lambda f: f[0]))
print("Closest to JFK:", min(dist_jfk, key=lambda f: f[0]))