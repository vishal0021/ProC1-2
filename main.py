from skyfield.api import load, wgs84

stations_url = 'http://celestrak.com/NORAD/elements/active.txt'
satellites = load.tle_file(stations_url,reload=True)
print('Loaded', len(satellites), 'satellites')

for i in satellites:
  print(i)

by_name = {sat.name: sat for sat in satellites}
satellite = by_name['SPACEBEE-136']
print(satellite)

"""by number"""

by_number = {sat.model.satnum: sat for sat in satellites}
satellite = by_number[52164]
print(satellite)

# Printing all the details about the satellite
#1 NORAD ID and Name

norad_id=satellite.model.satnum
print("NORAD ID: ",norad_id)
name=satellite.name
print("SATELLITE NAME: ",name)

#2 UTC Time

utc_time=satellite.epoch.utc_jpl()
print("UTC TIME: ")
print(utc_time)

#3. Local Time

import datetime
TimeDelta = datetime.timedelta(hours=5,minutes=30)
TZObject = datetime.timezone(TimeDelta,name="IST")
print("LOCAL TIME: ")
local_time=satellite.epoch.astimezone(TZObject)
print(local_time)

#4. LATITUDE, LONGITUDE"""
ts = load.timescale()
t=ts.now()
geocentric = satellite.at(t)
# print(geocentric.position.km) #returns the Cartesian x,y,z coordinates

lat, lon = wgs84.latlon_of(geocentric)
print('LATITUDE:', lat)
print('LONGITUDE:', lon)

#5. SPEED

speed=geocentric.speed()
print("SPEED: ",speed)
print(geocentric.velocity.km_per_s)

