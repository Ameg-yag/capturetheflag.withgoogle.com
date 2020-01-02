#!/usr/bin/python
import requests
import time
from bs4 import BeautifulSoup as bs

url = "https://drivetothetarget.web.ctfcompetition.com/"

r = requests.get(url)
b = bs(r.text, "html.parser")

step = 0.0001
lat = float(b.find(attrs={"name": "lat"})["value"])
lon = float(b.find(attrs={"name": "lon"})["value"])
token = b.find(attrs={"name": "token"})["value"]

#lon = 0.094000
#time.sleep(.5)

xinc = False
yinc = False

xy = True

while True:
    time.sleep(.4)
    try:
        lat -= step
        
        params = {"lat": lat, "lon": lon, "token": token}
        r = requests.get(url, params=params)
        b = bs(r.text, "html.parser")
        token = b.find(attrs={"name": "token"})["value"]

        if "You are getting closer" in r.text:
            print "closer latitude(x, y): %f : %f" % (lat, lon)
        elif "You are getting away" in r.text:
            lat = float(b.find(attrs={"name": "lat"})["value"])
            lon = float(b.find(attrs={"name": "lon"})["value"])
            print b.p.p.text
            break
        else:
            print r.text
            break
    except:
        lat += step
        pass

while True:
    time.sleep(.4)
    try:
        lon -= step

        params = {"lat": lat, "lon": lon, "token": token}
        r = requests.get(url, params=params)
        b = bs(r.text, "html.parser")
        token = b.find(attrs={"name": "token"})["value"]

        if "You are getting closer" in r.text:
            print "closer longitude(x, y): %f : %f" % (lat, lon)
        elif "You are getting away" in r.text:
            lat = float(b.find(attrs={"name": "lat"})["value"])
            lon = float(b.find(attrs={"name": "lon"})["value"])
            print b.p.p.text
            break
        else:
            r.text
            break
    except:
        lon += step
        pass

print "%f : %f" % (lat, lon)
print r.text
